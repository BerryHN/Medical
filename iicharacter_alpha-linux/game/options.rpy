image lk = im.Crop(Image('lurkmoar.png'),0,0,600,600)
image white = "#FFFFFF"
image futaba_bg = "#FFFFEE"

init python:
    lk = Character(u"Луркмор-кун",show_two_window=True)
    avaframe = Frame("avaframe.png", 5, 5)


init -1 python hide:

    #########################################
#ВНИМАНИЕ!!!
#Заменить на False в релизе!!!
    config.developer = True

    config.old_substitutions = True
    config.new_substitutions = False

    #########################################
#Не меняем эти числа, т.к. на них завязана вся игра.
#Если хотим поменять разрешение, юзаем перед запуском "set RENPY_SCALE_FACTOR=..."
    config.screen_width = 1280
    config.screen_height = 768


    #########################################
#Окно, название, иконка, мышь
    config.window_title = u"IIcharacter (Alpha)"
    config.menu_window_subtitle = u" - Меню"
    config.window_icon = "icon.png"
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    #########################################
#Лэйауты сейчас стандартные, но скорее всего будут изменены
    layout.button_menu()
    layout.scrolling_load_save()
    layout.one_column_preferences()

#Меню настроек 
    config.has_transitions = False
    config.has_joystick = False

#Параметры главного меню

    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
#Тема с розовыми заклугленными прямоугольниками.
#Чуть-чуть допиленная в плане неактивных элементов стандартная.
    theme.bordered(
        # Color scheme: Cotton Candy
                                    
        ## The color of an idle widget face.
        widget = "#EEAA88",

        ## The color of a focused widget face.
        widget_hover = "#ED7842",

        ## The color of the text in a widget.
        widget_text = "#800000",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#800000",

        ## The color of a disabled widget face. 
        disabled = "#F0D0B6",

        ## The color of disabled widget text.
        disabled_text = "#800000",

        ## The color of informational labels.
        label = "#800000",

        ## The color of a frame containing widgets.
        frame = "#F0E0D6",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "#FFFFEE",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "#FFFFEE",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.            
        )


    #########################################
#Стили окошек
    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.
    ## Margin is space surrounding the window, where the background is not drawn.
    ## *padding is space inside the window, where the background is drawn.
    ## yminimum - minimum height of the window, including the margins and padding.
#Диалоги
    style.window.background = Frame("frame.png", 20, 20)
    style.window.left_margin = 5
    style.window.right_margin = 5
    style.window.top_margin = 0
    style.window.bottom_margin = 5
    style.window.left_padding = 15
    style.window.right_padding = 15
    style.window.top_padding = 10
    style.window.bottom_padding = 10
    style.button.left_margin = 2
    style.button.right_margin = 1
    style.button.top_margin = 3
    style.button.bottom_margin = 1

#FIXME меняйте это значение для регулирования стандартной высоты окошка диалога
#      (если не влезает, оно растягивается, но лучше этого не допускать)
    style.window.yminimum = 128

#NVL
    style.nvl_window.background = Frame("frame.png", 20, 20)
    style.nvl_window.left_margin = 60
    style.nvl_window.right_margin = 60
    style.nvl_window.top_margin = 60
    style.nvl_window.bottom_margin = 60
    style.nvl_window.left_padding = 15
    style.nvl_window.right_padding = 15
    style.nvl_window.top_padding = 10
    style.nvl_window.bottom_padding = 10


    #########################################
#Шрифты
#Стандартный
    style.label_text.size = 17
    style.button_text.size = 17
    style.header = Style(style.default)
    style.header_label_text.color = (17,119,67,255)
    style.header_label_text.size = 17
    style.header_label_text.bold = True
    style.hyperlink_text.color = (0,0,255,255)
    style.hyperlink_text.size = 17

#Новый стиль - шрифт с тенью, для использования в диалогах и NVL.
    style.default_plus_shadow = Style(style.default)
    style.default_plus_shadow.drop_shadow=(2, 2)
    style.default_plus_shadow.color=(128,0,0,0)
    style.say_dialogue = Style(style.default_plus_shadow)
    style.say_label = Style(style.default_plus_shadow)
    style.narrator = Style(style.default_plus_shadow)
    style.narrator.italic = True
    style.input_text_inverted = Style(style.input_text)
    style.input_text_inverted.color = (255,255,238,255)

    style.say_window = Style(style.window)

    def img_bar(name, color, x, y):
        rv = theme.OneOrTwoColor("_theme_bordered/br" + name + ".png", color)
        if x is not None:
            rv = Frame(rv, x, y, tile=True)
        return rv

    sla = 100
    slb = 19
    slc = 164
    sld = 255
    slt = 150

    style.red_slider = Style(style.slider)
    style.red_slider.left_bar          = img_bar("slider_full",  [(slc,0,0,slt),(sla,0,0,slt)], 12, 0)
    style.red_slider.right_bar         = img_bar("slider_empty", [(slc,0,0,slt),(sla,0,0,slt)], 12, 0)
    style.red_slider.thumb             = img_bar("slider_thumb",  (sla,0,0,slt), None, None)
    style.red_slider.hover_left_bar    = img_bar("slider_full",  [(sld,0,0,slt),(slb,0,0,slt)], 12, 0)
    style.red_slider.hover_right_bar   = img_bar("slider_empty", [(sld,0,0,slt),(slb,0,0,slt)], 12, 0)
    style.red_slider.hover_thumb       = img_bar("slider_thumb",  (slb,0,0,slt), None, None)

    style.green_slider = Style(style.slider)
    style.green_slider.left_bar        = img_bar("slider_full",  [(0,slc,0,slt),(0,sla,0,slt)], 12, 0)
    style.green_slider.right_bar       = img_bar("slider_empty", [(0,slc,0,slt),(0,sla,0,slt)], 12, 0)
    style.green_slider.thumb           = img_bar("slider_thumb",  (0,sla,0,slt), None, None)
    style.green_slider.hover_left_bar  = img_bar("slider_full",  [(0,sld,0,slt),(0,slb,0,slt)], 12, 0)
    style.green_slider.hover_right_bar = img_bar("slider_empty", [(0,sld,0,slt),(0,slb,0,slt)], 12, 0)
    style.green_slider.hover_thumb     = img_bar("slider_thumb",  (0,slb,0,slt), None, None)

    style.blue_slider = Style(style.slider)
    style.blue_slider.left_bar         = img_bar("slider_full",  [(0,0,slc,slt),(0,0,sla,slt)], 12, 0)
    style.blue_slider.right_bar        = img_bar("slider_empty", [(0,0,slc,slt),(0,0,sla,slt)], 12, 0)
    style.blue_slider.thumb            = img_bar("slider_thumb",  (0,0,sla,slt), None, None)
    style.blue_slider.hover_left_bar   = img_bar("slider_full",  [(0,0,sld,slt),(0,0,slb,slt)], 12, 0)
    style.blue_slider.hover_right_bar  = img_bar("slider_empty", [(0,0,sld,slt),(0,0,slb,slt)], 12, 0)
    style.blue_slider.hover_thumb      = img_bar("slider_thumb",  (0,0,slb,slt), None, None)

    style.rainbow_slider = Style(style.slider)
    style.rainbow_slider.ymaximum         = 21
    style.rainbow_slider.left_bar         = Frame(myRainbow("brslider_full.png",sla,slt), 12, 0, tile=False)
    style.rainbow_slider.right_bar        = Frame(myRainbow("brslider_empty.png",sla,slt), 12, 0, tile=False)
    style.rainbow_slider.thumb            = img_bar("slider_thumb",  (sla,sla,sla,slt), None, None)
    style.rainbow_slider.hover_left_bar   = Frame(myRainbow("brslider_full.png",slb,slt), 12, 0, tile=False)
    style.rainbow_slider.hover_right_bar  = Frame(myRainbow("brslider_empty.png",slb,slt), 12, 0, tile=False)
    style.rainbow_slider.hover_thumb      = img_bar("slider_thumb",  (slb,slb,slb,slt), None, None)

    style.saturation_slider = Style(style.slider)
    style.saturation_slider.ymaximum         = 21
    style.saturation_slider.left_bar         = Frame(mySaturation("brslider_full.png",sla,slt), 12, 0, tile=False)
    style.saturation_slider.right_bar        = Frame(mySaturation("brslider_empty.png",sla,slt), 12, 0, tile=False)
    style.saturation_slider.thumb            = img_bar("slider_thumb",  (sla,sla,sla,slt), None, None)
    style.saturation_slider.hover_left_bar   = Frame(mySaturation("brslider_full.png",slb,slt), 12, 0, tile=False)
    style.saturation_slider.hover_right_bar  = Frame(mySaturation("brslider_empty.png",slb,slt), 12, 0, tile=False)
    style.saturation_slider.hover_thumb      = img_bar("slider_thumb",  (slb,slb,slb,slt), None, None)

    style.brightness_slider = Style(style.slider)
    style.brightness_slider.ymaximum         = 21
    style.brightness_slider.left_bar         = Frame(myBrightness("brslider_full.png",sla,slt), 12, 0, tile=False)
    style.brightness_slider.right_bar        = Frame(myBrightness("brslider_empty.png",sla,slt), 12, 0, tile=False)
    style.brightness_slider.thumb            = img_bar("slider_thumb",  (sla,sla,sla,slt), None, None)
    style.brightness_slider.hover_left_bar   = Frame(myBrightness("brslider_full.png",slb,slt), 12, 0, tile=False)
    style.brightness_slider.hover_right_bar  = Frame(myBrightness("brslider_empty.png",slb,slt), 12, 0, tile=False)
    style.brightness_slider.hover_thumb      = img_bar("slider_thumb",  (slb,slb,slb,slt), None, None)

    style.black_slider = Style(style.slider)
    style.black_slider.left_bar        = img_bar("slider_full",  [(slc,slc,slc,slt),(sla,sla,sla,slt)], 12, 0)
    style.black_slider.right_bar       = img_bar("slider_empty", [(slc,slc,slc,slt),(sla,sla,sla,slt)], 12, 0)
    style.black_slider.thumb           = img_bar("slider_thumb",  (sla,sla,sla,slt), None, None)
    style.black_slider.hover_left_bar  = img_bar("slider_full",  [(sld,sld,sld,slt),(slb,slb,slb,slt)], 12, 0)
    style.black_slider.hover_right_bar = img_bar("slider_empty", [(sld,sld,sld,slt),(slb,slb,slb,slt)], 12, 0)
    style.black_slider.hover_thumb     = img_bar("slider_thumb",  (slb,slb,slb,slt), None, None)


    #########################################
#Звуки
    config.has_sound = False
    config.has_music = False
    config.has_voice = False


    #########################################
#Хэлп
    config.help = None


    #########################################
#Транзишоны
    config.enter_transition = None
    config.exit_transition = None
    config.intra_transition = None
    config.main_game_transition = None
    config.game_main_transition = None
    config.end_splash_transition = None
    config.end_game_transition = None
    config.after_load_transition = None

    
    #########################################
#Настройки по умолчанию
    config.default_fullscreen = False
    config.default_text_cps = 0
    config.use_cpickle = False
    config.has_autosave = False

#Key map
    for key in ["skip", "toggle_skip", "fast_skip"]:
        config.keymap[key] = []
                         
## This section contains information about how to build your project into 
## distribution files.
init python:
    
    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "iicharacter_alpha"
    
    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "iicharacter_alpha"
    
    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False
    
    ## File patterns:
    ## 
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##    
    ##
    ## In a pattern:
    ##
    ## / 
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    
    ## To archive files, classify them as 'archive'.
    
    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    