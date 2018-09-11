package edu.tommytyngutexas.catcells;

import android.app.ActionBar;
import android.app.Activity;
import android.app.FragmentManager;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.ActivityInfo;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Point;
import android.media.AudioManager;
import android.media.MediaPlayer;
import android.os.Build;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.Display;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends Activity implements CatView.OnItemTouchListener {

    public static final int START_DURATION = 2000;
    private CatView mMainScreen;
    private MediaPlayer mPlayer;
    private LinearLayout mGameOverScreen;

    private LinearLayout mLevelCompleteScreen;

    private String currentWid = null;
    private TextView currentLookForWid = null;
    private TextView score1 = null;
    private TextView score2 = null;
    private TextView score3 = null;

    private int hints;

    private Mode mMode;

    private int bsize;

    //private long startTime;
    private int timeAllowed;
    private int ticksTaken;

    private long findTime;
    private long score;

    Timer timer;

    private SoundEffects mSoundEffects;

    private boolean backgroundImage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        setTheme(R.style.AppTheme);
        super.onCreate(savedInstanceState);
        setTheme(R.style.AppTheme);
        setContentView(R.layout.activity_main);


        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_NOSENSOR);
        setVolumeControlStream(AudioManager.STREAM_MUSIC);

        Intent intent = getIntent();
        if (intent!=null) {
            String modestr = intent.getStringExtra("mode");
            if (modestr!=null) {
                mMode = Mode.valueOf(modestr);
            }
        }

        if (mMode==null) {
            mMode = Mode.Endless;
        }

        timeAllowed = mMode.getTimeAllowed();


        SharedPreferences appPreferences = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        backgroundImage = appPreferences.getBoolean("use_back_image", false);

        mMainScreen = findViewById(R.id.main_screen);
        mLevelCompleteScreen = findViewById(R.id.level_complete_screen);
        mGameOverScreen = findViewById(R.id.game_over_screen);

        currentLookForWid = findViewById(R.id.looking_for);
        score1 = findViewById(R.id.score1);
        score2 = findViewById(R.id.score2);
        score3 = findViewById(R.id.score3);



        bsize = getSmallestDim();


        Log.d("Catcells", mMode.getIconSize(bsize) + " " + bsize);

        currentLookForWid.setTextSize(Math.max(mMode.getMinIconSize(bsize), 40));


        mMainScreen.setOnItemTouchListener(this);


        mMainScreen.postDelayed(new Runnable() {
            @Override
            public void run() {
                start();
            }
        }, 100);


        View.OnClickListener hintClick = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (currentWid!=null && (!mMode.limitHints() || hints<mMode.getHints())) {
                    hints++;
                    mMainScreen.highlightTop();
                    updateScoreBoard();
                }
            }
        };

        currentLookForWid.setOnClickListener(hintClick);
        score3.setOnClickListener(hintClick);

        findViewById(R.id.menu_button).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                returnToMenu();
            }
        });

        findViewById(R.id.menu_button2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                returnToMenu();
            }
        });

        findViewById(R.id.next_button).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                start();
            }
        });
    }



    @Override
    protected void onResume() {
        super.onResume();
        mSoundEffects = new SoundEffects(this);
        mPlayer = MediaPlayer.create(MainActivity.this,R.raw.catmojo);
        //mPlayer.setLooping(true);
        mPlayer.start();
    }

    @Override
    protected void onPause() {
        if (timer!=null) {
            timer.cancel();
        }
        mSoundEffects.release();
        super.onPause();
    }

    private void returnToMenu() {
        Intent intent = new Intent(this, EntryActivity.class);
        startActivity(intent);
        finish();
    }


    private void endGame() {

        mMainScreen.removeAllItems();


        mMainScreen.postDelayed(new Runnable() {
            @Override
            public void run() {

                mGameOverScreen.setVisibility(View.VISIBLE);
                mMainScreen.setVisibility(View.GONE);

            }
        },500);


    }

    private void levelComplete() {
        if (timer!=null) {
            timer.cancel();
        }
        if (timeAllowed>5) timeAllowed *= .92;

        score2.setText(getString(R.string.score_time,  timeAllowed));

        updateScoreBoard();

        mMainScreen.postDelayed(new Runnable() {
            @Override
            public void run() {
                currentLookForWid.setText("");
                TextView faster = mLevelCompleteScreen.findViewById(R.id.faster);

                faster.setVisibility(mMode.isTimed()? View.VISIBLE : View.GONE);

                mLevelCompleteScreen.setVisibility(View.VISIBLE);
                mMainScreen.setVisibility(View.GONE);

            }
        },200);


    }


    private void updateScoreBoard() {
        score1.setText(getString(R.string.score_found, mMainScreen.count(), mMode.getNumIcons(), score));
        if (mMode.limitHints()) {
            score3.setText(getString(R.string.score_hints, mMode.getHints() - hints));
        }
    }

    private void showNext(boolean wiggle) {
        currentWid = mMainScreen.peek(!mMode.limitHints() || hints<mMode.getHints());
        if (currentWid != null) {

            currentLookForWid.setText(currentWid);

            if (wiggle) {
                scheduleHint(2000);
                scheduleHint(5000);
            }
            scheduleHint(30000);

            findTime = System.currentTimeMillis();

        } else {
            if (timer!=null) {
                timer.cancel();
            }

            int delaytime = 1000;
            String message = "";

            if (mMode.limitHints()) {
                int bonus =(mMode.getHints() - hints)*1000;
                score += bonus;

                message += getString(R.string.hint_bonus, bonus);
                delaytime = 2500;
            }

            if (mMode.isTimed() && ticksTaken<timeAllowed) {
                long bonus = (timeAllowed - ticksTaken)*1000;
                score += bonus;
                delaytime = 2500;

                if (!message.equals("")) message += "\n";
                message += getString(R.string.time_bonus,  bonus);
            }

            showMessage(message);

            mMainScreen.postDelayed(new Runnable() {
                @Override
                public void run() {
                    if (mMode.showLevelComplete()) {
                        levelComplete();
                    } else {
                        start();
                    }
                }
            },delaytime);
        }

        updateScoreBoard();
    }



    private void scheduleHint(int time) {
        final String currentWidThen = currentWid;
        mMainScreen.postDelayed(new Runnable() {
            @Override
            public void run() {
                if (currentWidThen.equals(currentWid)) {
                    mMainScreen.highlightTop();
                }
            }
        }, time);
    }

    @Override
    public void onItemClick(String text) {
        //Log.d("Catcells", "touched '" + text +"'");

        if (currentLookForWid.getText().equals(" ")) {
            return;
        }

        if (currentWid==null || text==null) return;

        if (currentWid.equals(text)) {

            Log.d("Catcells", "Found " + currentWid.codePointAt(0));

            score += Math.max(100, 5000 - (System.currentTimeMillis() - findTime)) * (backgroundImage?1.5:1);

            mSoundEffects.playMeow();
            mMainScreen.startMeow();

            mMainScreen.pop();

            showNext(false);

        } else {
            mSoundEffects.playMiss();
            mMainScreen.highlight(text);

            switch (mMode) {
                case Lion:
                    score -= 100;
                    break;
                case Kitten:
                    score -= 25;
                    break;
            }
            if (mMode.isTimed() && mMode==Mode.Lion) {
                ticksTaken += 5;
                showMessage(getString(R.string.miss_penalty));
            }
        }
        updateScoreBoard();

    }

    private void showMessage(String message) {
        final TextView t = findViewById(R.id.message_text);
        t.setTextSize(36);
        t.setShadowLayer(16, 2, 2, Color.WHITE);
        t.setText(message);
        t.setTextColor(Color.BLACK);
        t.setBackgroundColor(Color.argb(127,64,64,64));
        t.setVisibility(View.VISIBLE);

        mMainScreen.postDelayed(new Runnable() {
            @Override
            public void run() {
                t.setVisibility(View.GONE);
            }
        }, 2000);

    }

    private void start() {

        currentWid = null;
        mMainScreen.removeAllItems();
        mMainScreen.setVisibility(View.VISIBLE);
        mLevelCompleteScreen.setVisibility(View.GONE);
        mGameOverScreen.setVisibility(View.GONE);

        currentLookForWid.setText(" ");

        if (backgroundImage) {
            int[] backs = SoundEffects.getResIdArray(this, R.array.pics);

            mMainScreen.setBackgroundResource(backs[(int) (backs.length * Math.random())]);
        }

        hints = 0;
        ticksTaken = 0;
        if (timer!=null) {
            timer.cancel();
        }


        long ttime = START_DURATION / mMode.getNumIcons();
        Set<Integer> actives = new HashSet<>();
        int bail = syms.length * 2;
        for (int j = 0; j < mMode.getNumIcons(); j++) {

            int symind;
            String sym;
            int tries = 0;
            do {
                int triesInner = 0;
                do {
                    symind = getRandomInt(syms.length);
                } while (actives.contains(symind) && triesInner++<bail);

                sym = syms[symind];
            } while (!hasGlyph(sym) && tries++<bail);
            actives.add(symind);

            addSymToScreen(sym, ttime*j, j == mMode.getNumIcons()-1);

        }


    }

    private void startDone() {
        mMainScreen.postDelayed(new Runnable() {
            @Override
            public void run() {
                showNext(true);
                updateScoreBoard();
            }
        }, 200);

        mMainScreen.postDelayed(new Runnable() {
            @Override
            public void run() {
                ticksTaken = 0;

                updateScoreBoard();

                if (mMode.isTimed()) {
                    score2.setVisibility(View.VISIBLE);
                    if (timer!=null) {
                        timer.cancel();
                    }
                    timer = new Timer();
                    timer.schedule(new TimerTask() {
                        @Override
                        public void run() {

                            score2.post(new Runnable() {
                                @Override
                                public void run() {
                                    ticksTaken++;
                                    int timeleft = timeAllowed - ticksTaken;
                                    score2.setText(getString(R.string.score_time,  timeleft));
                                    if (timeleft <= 0) {
                                        timer.cancel();
                                        endGame();
                                    }
                                }
                            });
                        }
                    }, 1000, 1000);
                } else {
                    score2.setVisibility(View.GONE);
                }

            }
        }, 350);
    }


    private void addSymToScreen(final String sym, long delay, final boolean isLast) {
        Point location;
        boolean done;
        final int size = (getRandomInt(mMode.getMaxIconSize(bsize) - mMode.getMinIconSize(bsize))+mMode.getMinIconSize(bsize))*2;

        mMainScreen.postDelayed(new Runnable() {
            @Override
            public void run() {
                mMainScreen.addText(size, sym);
                if (isLast) {
                    startDone();
                }
            }
        }, delay);

    }

    private static int getRandomInt(int max) {
        return (int)(Math.random()*max);

    }

    private int getSmallestDim() {
        Display display = getWindowManager().getDefaultDisplay();
        Point size = new Point();
        display.getSize(size);
        return Math.min(size.x, size.y);
    }

    private int spToPx(int px) {
        return (int)(px * getResources().getDisplayMetrics().density + 0.5f);
    }


    private static final Paint hasGlyphTester = new Paint();
    private static final String basicSmiley = new String(Character.toChars(0x1F638));
    private static boolean hasGlyph(String sym) {
        try {
            if (Build.VERSION.SDK_INT >= 23) {
                return hasGlyphTester.hasGlyph(sym);
            } else {

                float testW = hasGlyphTester.measureText(sym);
                float knownW = hasGlyphTester.measureText(basicSmiley);
                return testW > knownW * .5;
            }
        } catch (Exception e) {
            Log.e("Catcells", e.getMessage(), e);
        }

        return false;
    }


    public final static String[] syms;
    private static final int[] symsHex = {
            0x1F638, //grinning cat face with smiling eyes
            0x1F639, //cat face with tears of joy
            0x1F63A, //smiling cat face with open mouth
            0x1F63B, //smiling cat face with heart-shaped eyes
            0x1F63C, //cat face with wry smile
            0x1F63D, //kissing cat face with closed eyes
            0x1F63E, //pouting cat face
            0x1F63F, //crying cat face
            0x1F640, //weary cat face




    };

    static {
        syms = new String[symsHex.length];
        for (int i = 0; i < symsHex.length; i++) {
            syms[i] = new String(Character.toChars(symsHex[i]));
            if (!hasGlyph(syms[i])) {
                Log.d("Catcells", "No glyph for " + i + " " + symsHex[i]);
            }

        }
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.in_game_menu, menu);
        return super.onCreateOptionsMenu(menu);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        FragmentManager fm = getFragmentManager();
        switch (item.getItemId()) {
            case R.id.about_game:
                startActivity(new Intent(this, AboutActivity.class));
                return true;
            case R.id.quit:
                QuitDialogFragment quitDialogFragment = new QuitDialogFragment();
                quitDialogFragment.show(fm, "quit");
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }

}
