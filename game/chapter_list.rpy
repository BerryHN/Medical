screen chapter_list:
    tag menu
    window:
        style "gm_root"
    
    add  "background.png"
    
    imagemap:
        if persistent.Fat_Lady_2:
            ground "Menu Idle.png"
            hover "Menu Idle.png"
            idle "Menu Idle.png"
        if persistent.Fat_Lady_1:
            ground "Menu Fat_Lady_1.png"
            hover "Menu Fat_Lady_1.png"
            idle "Menu Fat_Lady_1.png"
        if persistent.Big_belly_boy:
            ground "Menu Big_belly_boy.png"
            hover "Menu Big_belly_boy.png"
            idle "Menu Big_belly_boy.png"
        if persistent.Mad_Man:
            ground "Menu Mad_Man.png"
            hover "Menu Mad_Man.png"
            idle "Menu Mad_Man.png"
        if persistent.Damsel_Distress:
            ground "Menu Damsel_Distress.png"
            hover "Menu Damsel_Distress.png"
            idle "Menu Damsel_Distress.png"
        if persistent.Slow_Girl:
            ground "Menu Slow_Girl.png"
            hover "Menu Slow_Girl.png"
            idle "Menu Slow_Girl.png"
        if persistent.Sadman:
            ground "Menu Sadman.png"
            hover "Menu Sadman.png"
            idle "Menu Sadman.png"
        
        ground "Menu hagman.png"
        hover "Menu hagman.png"
        idle "Menu hagman.png"
        if persistent.Sadman:
            hotspot(50,305,200,360) action ShowMenu('sadman')
        if persistent.Fat_Lady_1:
            hotspot(484,209,650,267) action ShowMenu('fat1')
        if persistent.Fat_Lady_2:
            hotspot(488,423,649,476) action ShowMenu('fat2')
        if persistent.Damsel_Distress:
            hotspot(218,350,370,400) action ShowMenu('damsel')
        if persistent.Mad_Man:
            hotspot(484,48,634,104) action ShowMenu('madman')
        if persistent.Big_belly_boy:
            hotspot(482,128,690,188) action ShowMenu('bigBoy')
        if persistent.Slow_Girl:
            hotspot(56,395,210,450) action ShowMenu('slowGirl')
        hotspot(56,46,235,101) action ShowMenu('hangman')
        frame:
            style_group "gm_nav"
            xalign .5
            yalign .98

            has hbox
            
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("Quit") action Quit(False)
#init -2 python:
    #style.gm_nav_button.size_group= "gm_nav"
     #This ensures that any other menu screen is replaced.
label preference_screen:
    call screen preferences()