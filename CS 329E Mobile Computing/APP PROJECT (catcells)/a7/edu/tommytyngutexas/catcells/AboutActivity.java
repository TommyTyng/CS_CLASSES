package edu.tommytyngutexas.catcells;

import android.app.Activity;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;
import android.text.Html;
import android.text.method.LinkMovementMethod;
import android.widget.TextView;


public class AboutActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_about);


        try {
            PackageInfo pInfo = getPackageManager().getPackageInfo(getPackageName(), 0);
            String version = pInfo.versionName;

            TextView txtappname = findViewById(R.id.txtappname);
            txtappname.setText(getString(R.string.app_name) + " " + version);

        } catch (PackageManager.NameNotFoundException e) {
            e.printStackTrace();
        }

        TextView txtAbout = findViewById(R.id.txtAbout);
        txtAbout.setMovementMethod(LinkMovementMethod.getInstance());
        if (Build.VERSION.SDK_INT >= 24) {
            txtAbout.setText(Html.fromHtml(getString(R.string.about_app), 0));
        } else {
            txtAbout.setText(Html.fromHtml(getString(R.string.about_app)));

        }
    }

    @Override
    public void onBackPressed() {
        setResult(RESULT_OK);
        finish();
        //super.onBackPressed();
    }


}
