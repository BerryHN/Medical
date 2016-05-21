init python:
    def get_render_info():
        import renpy.display.swdraw
        fs = "fullscreen" if renpy.game.preferences.fullscreen else "window"
        rn = "software" if isinstance(renpy.display.draw, renpy.display.swdraw.SWDraw) else "GL"
        mod = renpy.display.draw.__class__.__module__
        return (rn,mod,fs)

    def get_all_info():
        import platform
        import locale
        import os
        import os.path
        import sys
        system  = platform.uname()
        renderinfo  = get_render_info()
        loc = locale.getdefaultlocale()
        deflocale = (loc[0] if loc[0] else "", loc[1] if loc[1] else "")
        cmdline = (sys.executable," ".join(sys.argv))
        return system, renderinfo, deflocale, cmdline

    def ui_folder_button(descr, path):
        import os
        wrong_sep = "\\" if os.sep == "/" else "/"
        path = path.replace(wrong_sep,os.sep)
        ui_imagebutton_with_text("icons/32x32/folder.png", ["plugin", ("dir",path)], descr, path)


    def about_iface():
        import pygame.version
        ui.vbox()
        ui_header(u"Framework information:")
        ui_imagebutton_with_text("icons/32x32/renpy.png",  ["plugin", "renpy"],  u"RenPy "  + renpy.version())
        ui_imagebutton_with_text("icons/32x32/pygame.png", ["plugin", "pygame"], u"PyGame " + pygame.version.ver)
        ui_imagebutton_with_text("icons/32x32/python.png", ["plugin", "python"], u"Python " + sys.version)
        ui_header(u"Avaliable modules:")
        if  version_history != None:
            ui_imagebutton_with_text("icon.png", ["plugin", version_history], u"Viewer " + version)
        else:
            ui_imagebutton_with_text("icon.png", None, u"Viewer: " + version)
        for p in plugin_display_list:
            if  persistent.plugin_display[p["id"]]:
                ui_imagebutton_with_text("icons/32x32/plugin.png", ["plugin", p["version_history"]], p["display_name"]+" %s",p["version"])
            else:
                ui_imagebutton_with_text("icons/32x32/plugin_disabled.png", ["plugin", p["version_history"]], p["display_name"]+" %s",p["version"])

        system, renderinfo, deflocale, cmdline = get_all_info()
        ui_header(u"System information:")
        ui_imagebutton_with_text("icons/32x32/screen_error.png", None, " / ".join(system[0:1]+system[2:4]))
        ui_imagebutton_with_text("icons/32x32/processor.png", None, " / ".join(system[4:]))
        ui_imagebutton_with_text("icons/32x32/agp.png", None, " / ".join(renderinfo))
        ui_imagebutton_with_text("icons/32x32/text_language.png", None, " / ".join(deflocale))
        ui_imagebutton_with_text("icons/32x32/application_xp_terminal.png", None, " / ".join(cmdline))
        ui_header(u"Folder layout information:")
        ui_folder_button(u"config.renpy_base: %s", renpy.config.renpy_base)
        ui_folder_button(u"config.basedir: %s", renpy.config.basedir)
        ui_folder_button(u"config.gamedir: %s", renpy.config.gamedir)
        ui.close()

    def about_action(button):
        import webbrowser
        site_map = {
                "renpy":            "http://renpy.org/",
                "pygame":           "http://pygame.org/",
                "python":           "http://python.org/",
            }

        if isinstance(button,list):
            ui_additional_window(version_history_iface,"icons/32x32/plugin.png",button)
        elif isinstance(button,tuple) and button[0] == "dir":
            sys_open_folder(button[1])
        elif button in site_map:
            webbrowser.open(site_map[button])
        pass

    def version_history_iface(options):
        ui.vbox()
        ui_header(u"Version history:")
        for (version, description) in options:
            if  isinstance(description,list):
                ui_text(version + u": %s",description[0])
                for d in description[1:]:
                    ui_text(u"       %s",d)
            else:
                ui_text(version + u": %s",description)
        ui.close()

    def about_reset():
        pass

    def about_get_state():
        return ''

    def about_set_state(state):
        pass

    current_plugin = {}
    current_plugin["id"] = "about"
    current_plugin["display_icon"] = "icons/32x32/info_rhombus.png"
    current_plugin["display_name"] = u"Information"
    current_plugin["interface"] = about_iface
    current_plugin["action"] = about_action
    current_plugin["reset"] = about_reset
    current_plugin["get_state"] = about_get_state
    current_plugin["set_state"] = about_set_state
    current_plugin["version"] = "1.2.0"
    current_plugin["version_history"] = [(u"1.0.0",u"Initial release"),(u"1.1.0",u"Added version history"),(u"1.2.0",[u"Locale information",u"Moved support and thanks sections to another plugin page"])]
    current_plugin["priority"] = 10
    current_plugin["is_optional"] = False
    plugin_list += [current_plugin]

    def support_iface():
        ui.vbox()
        ui_header(u"Support:")
        ui_imagebutton_with_text("icons/32x32/email_edit.png", ["plugin", "mail"], "Click here and mail me: lolbot_iichan@mail.ru")
        ui_imagebutton_with_text("icons/32x32/creative_commons.png", ["plugin", "creative_commons"], "Copyleft 2011-2013, Creative Commons: by-nc-sa")
        ui_header(u"Thanks to:")
        ui_imagebutton_with_text("icons/32x32/reseller_programm.png", ["plugin", "khmix"],  u"K.H.mix generator community")
        ui_imagebutton_with_text("icons/32x32/fatcow.png", ["plugin", "fatcow"],  u"FatCow 3500 Free Icons")
        ui_imagebutton_with_text("icons/32x32/user_batman.png", ["plugin", "huyase"],  u"Huyase Namae")
        ui_imagebutton_with_text("icons/32x32/user_geisha.png", ["plugin", "iichan"],  u"Mod-tan & IIchan.hk")
        ui_imagebutton_with_text("icons/32x32/pytom.png", ["plugin", "pytom"],  u"PyTom")

        ui_header(u"Charsets creators:")
        authors = {}
        for charset in os.listdir(chsetdirfull):
            name, link, icon = provide_credits_info(chsetdirfull, charset)
            if  name:
                authors[name] = (link,icon)
        names = authors.keys()
        names.sort(key=str.lower)
        for name in names:
            link,icon = authors[name]
            ui_imagebutton_with_text(icon, ["plugin", ("url",link)] if link else None, name)
        ui.close()

    def support_action(button):
        import webbrowser
        site_map = {
                "creative_commons": "http://creativecommons.org/licenses/by-nc-sa/3.0/",

                "khmix":            "http://khmix.sakura.ne.jp",
                "iichan":           "http://iichan.hk/",
                "fatcow":           "http://www.fatcow.com/free-icons",
                "huyase":           "http://www.pixiv.net/member.php?id=202193",
                "pytom":            "http://twitter.com/renpytom",
            }

        if  button == "mail":
            import pygame.version
            system, renderinfo, deflocale, cmdline = get_all_info()
            url  = "mailto:lolbot_iichan@mail.ru"
            url += "?subject=IIcharacter "+version
            url += "&body=%0D%0A%0D%0A%0D%0A----------------------------------------"
            url += "%0D%0ALang: " + persistent.current_lang
            url += "%0D%0ARenPy: " + renpy.version()
            url += "%0D%0APyGame: " + pygame.version.ver
            url += "%0D%0APython: " + sys.version
            url += "%0D%0AModules: "
            for p in plugin_display_list:
                url += "%0D%0A    * " + p["display_name"].encode("utf-8")+" "+p["version"]
            url += "%0D%0AOS: " + " / ".join(system[0:1]+system[2:4])
            url += "%0D%0ACPU: " + " / ".join(system[4:])
            url += "%0D%0ARender: " + " / ".join(renderinfo)
            url += "%0D%0ALocale: " + " / ".join(deflocale)
            url += "%0D%0ACommand line: " + " / ".join(cmdline)
            if  not renpy.windows:
                url = url.replace("%0D%0A","%0A")
            webbrowser.open(url)
        elif isinstance(button,tuple) and button[0] == "url":
            webbrowser.open(button[1])
        elif button in site_map:
            webbrowser.open(site_map[button])
        pass

    def support_reset():
        pass

    def support_get_state():
        return ''

    def support_set_state(state):
        pass

    current_plugin = {}
    current_plugin["id"] = "support"
    current_plugin["display_icon"] = "icons/32x32/reseller_programm.png"
    current_plugin["display_name"] = u"Support"
    current_plugin["interface"] = support_iface
    current_plugin["action"] = support_action
    current_plugin["reset"] = support_reset
    current_plugin["get_state"] = support_get_state
    current_plugin["set_state"] = support_set_state
    current_plugin["version"] = "1.1.0"
    current_plugin["version_history"] = [(u"1.0.0",u"Initial release"),(u"1.1.0",u"Credits information")]
    current_plugin["priority"] = 0
    current_plugin["is_optional"] = False
    plugin_list += [current_plugin]
