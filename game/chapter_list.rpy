screen chapter_list:
    tag menu
    add "ward.jpg"
    use navigation
    imagemap:
        ground "Menu Idle.png"
        idle "Menu Idle.png"
        hover "Menu Idle.png"
        alpha False
        if persistent.Hagman:
            hotspot() action Showmenu() activate_sound
        if persistent.Sadman:
            pass
        if persistent.Fat_Lady_1:
            pass
        if persistent.Fat_Lady_2:
            pass
        if persistent.Damsel_Distress:
            pass
        if persistent.Mad_Man:
            pass
        if persistent.Big_belly_boy:
            pass
        if persistent.Slow_Girl:
            pass
init -2 python:
    style.gm_nav_button.size_group= "gm_nav"