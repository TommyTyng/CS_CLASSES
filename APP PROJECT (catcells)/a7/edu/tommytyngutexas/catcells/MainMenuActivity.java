package edu.tommytyngutexas.catcells;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.os.Handler;
import android.preference.PreferenceManager;
import android.view.View;

public class MainMenuActivity extends Activity implements View.OnClickListener{

    private MediaPlayer mPlayer;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        setTheme(R.style.AppTheme);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_mainmenu);


        findViewById(R.id.go_button).setOnClickListener(this);
        findViewById(R.id.go_imageView).setOnClickListener(this);

        findViewById(R.id.about_button).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainMenuActivity.this, AboutActivity.class);
                startActivity(intent);
            }
        });
    }

    @Override
    public void onClick(View v) {
        Intent intent = new Intent(this, EntryActivity.class);
        startActivity(intent);
        finish();
    }


    @Override
    protected void onResume() {
        super.onResume();
        //new Handler().post(new Runnable() {
          //  @Override
            //public void run() {
              //  SharedPreferences appPreferences = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                //mPlayer = MediaPlayer.create(MainMenuActivity.this,R.raw.catmojo);
               // mPlayer.setLooping(true);
                //float vol = appPreferences.getInt("sound_effects_volume", 100) / 100.0f;;
                //mPlayer.setVolume(vol,vol);
                //mPlayer.start();

            //}
       // });
    }

    @Override
    protected void onPause() {
        super.onPause();
        //if(mPlayer!=null) {
          //  mPlayer.release();
        //}
    }
}
