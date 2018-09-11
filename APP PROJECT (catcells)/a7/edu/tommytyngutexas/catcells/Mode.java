package edu.tommytyngutexas.catcells;


import android.content.Context;


public enum Mode {

    Endless   (10, -1, .5f, -1, R.string.level_endless, R.integer.level_kitten),
    Kitten  (25, 120, 2, 15, R.string.level_kitten, R.integer.level_kitten),
    Lion  (50, 120, 3, 5, R.string.level_lion, R.integer.level_lion)
    ;


    Mode(int numIcons, int timeAllowed, float overLap, int hints, int stringRes, int iconRes) {
        this.numIcons = numIcons;
        this.timeAllowed = timeAllowed;
        this.overLap = overLap;
        this.hints = hints;
        this.string = stringRes;
        this.icon = iconRes;
    }



    public int getNumIcons() {
        return numIcons;
    }

    public int getTimeAllowed() {
        return timeAllowed;
    }

    public boolean isTimed() {
        return timeAllowed>0;
    }

    public boolean showLevelComplete() {
        return timeAllowed!=-1;
    }

    public int getIconSize(int maxwidth){
        return  Math.max(maxwidth/16, Math.min(maxwidth/numIcons, 100));
    }

    public int getMinIconSize(int maxwidth) {
        return (int)(getIconSize(maxwidth)  *3.0/4);
    }

    public int getMaxIconSize(int maxwidth) {
        return getIconSize(maxwidth);
    }


    public int getMargin(int maxwidth) {
        return (int)(getIconSize(maxwidth) * 2.5);
    }

    public float getOverLap() {
        return overLap;
    }

    public int getHints() {
        return hints;
    }

    public boolean limitHints() {
        return hints>-1;
    }

    public String toString(Context context) {
        return new String(Character.toChars(context.getResources().getInteger(icon))) + "   " + context.getString(string);
    }


    private int numIcons;
    private float overLap;
    private int hints;
    private int timeAllowed;

    private int string;
    private int icon;




}