
# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what, side_image=None, two_window=True):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu
label main_menu:

    # This ensures that any other menu screen is replaced.
    #tag menu
    call screen chapter_list

#label main_menu:
    
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
        elif persistent.Fat_Lady_1:
            ground "Menu Fat_Lady_1.png"
            hover "Menu Fat_Lady_1.png"
            idle "Menu Fat_Lady_1.png"
        elif persistent.Big_belly_boy:
            ground "Menu Big_belly_boy.png"
            hover "Menu Big_belly_boy.png"
            idle "Menu Big_belly_boy.png"
        elif persistent.Mad_Man:
            ground "Menu Mad_Man.png"
            hover "Menu Mad_Man.png"
            idle "Menu Mad_Man.png"
        elif persistent.Damsel_Distress:
            ground "Menu Damsel_Distress.png"
            hover "Menu Damsel_Distress.png"
            idle "Menu Damsel_Distress.png"
        elif persistent.Slow_Girl:
            ground "Menu Slow_Girl.png"
            hover "Menu Slow_Girl.png"
            idle "Menu Slow_Girl.png"
        elif persistent.Sadman:
            ground "Menu Sadman.png"
            hover "Menu Sadman.png"
            idle "Menu Sadman.png"
        else:
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


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():
    # The background of the game menu.
    modal False
    window:
        style "gm_root"
    
    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
       # textbutton _("Save Game") action ShowMenu("save")
        #textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action ShowMenu('start')
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 2 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

           # frame:
            #    style_group "pref"
             #   has vbox

              #  label _("Transitions")
               # textbutton _("All") action Preference("transitions", "all")
               # textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            #frame:
             #   style_group "pref"
              #  has vbox

               # textbutton _("Joystick...") action Preference("joystick")


       # vbox:
        #    frame:
         #       style_group "pref"
          #      has vbox

           #     label _("Skip")
            #    textbutton _("Seen Messages") action Preference("skip", "seen")
             #   textbutton _("All Messages") action Preference("skip", "all")

     #       frame:
      #          style_group "pref"
       #         has vbox

        #        textbutton _("Begin Skipping") action Skip()

         #   frame:
          #      style_group "pref"
           #     has vbox
#
 #               label _("After Choices")
  #              textbutton _("Stop Skipping") action Preference("after choices", "stop")
   #             textbutton _("Keep Skipping") action Preference("after choices", "skip")
#
 #           frame:
  #              style_group "pref"
   #             has vbox
#
 ##               label _("Auto-Forward Time")
   #             bar value Preference("auto-forward time")

    #            if config.has_voice:
     #               textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        #textbutton _("Save") action ShowMenu('save')
        #textbutton _("Q.Save") action QuickSave()
        #textbutton _("Q.Load") action QuickLoad()
       # textbutton _("Skip") action Skip()
       # textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        #textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 18
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


#Health bar
screen health_bar:
    hbox:
         xalign 0.0 yalign 0.0
         text _("Karma: [dr.life] points")
         bar value AnimatedValue(dr.life, range=7.0)


transform rotating:
    xpos 0.5
    ypos 0.3
    xalign 0.5
    yalign 0.5
    #linear deflate 
    rotate (needle)

transform x:
    xpos 0.5
    ypos 0.3
    xalign 0.5
    yalign 0.5

    
screen gauge:
    frame:
        xmaximum 300# X size of clock graphic
        ymaximum 300 # Y size of clock graphic
        xalign 0.85      # X placement on screen
        yalign 0.30 # Y placement on screen
        
        imagemap:
            ground "blood_back" at x
            
            hotspot(0,0,74,24) clicked Return('1')
            hotspot(0,272,115,300) clicked Return('2')
            hotspot(185,272,300,300) clicked Return('3')
            hotspot(146,0,300,24) clicked Return('4')
        add "pointer" at rotating
        
#screen chart_button:
 #   textbutton "Show Chart" action [ Show("chart_screen"), Hide("chart_button")] align (.95,.04)
#screen chart_screen:
 #   modal True
  #  $ rows=len(chart)
   # $ remain=chart % 3
    #if remain > 0 and len(chart) > 3:
    #    $rows += 1
#    $ ui.grid(3, rows)
    #for item in chart:
     #   imagebutton item.image action item.action
 #   $ ui.close()
        
        

        