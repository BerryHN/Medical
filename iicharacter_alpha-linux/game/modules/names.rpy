init python:
    name_generator_temp = config.basedir + os.sep + "temp" + os.sep + "description.txt"

    mascot_name = ""
    additional_info = ""
    additional_info_pattern = ""

    if  persistent.name_generator_use_gatchina == None:
        persistent.name_generator_use_gatchina = False
    if  persistent.name_generator_use_name == None:
        persistent.name_generator_use_name = False

    def names_iface():
        ui.vbox()
        ui_header(u"Name and description settings:")
        ui_imagebutton_with_text("icons/32x32/user_edit.png", ["plugin", "edit_name"], u"Edit name")
        ui_imagebutton_with_text("icons/32x32/user_delete.png", ["plugin", "clear_name"], u"Clear name")
        ui_line()
        ui_imagebutton_with_text("icons/32x32/vcard_edit.png", ["plugin", "edit_description"], u"Edit description")
        ui_imagebutton_with_text("icons/32x32/vcard_delete.png", ["plugin", "clear_description"], u"Clear description")
        ui.close()

    def name_generator_iface():
        ui.vbox()
        ui_header(u"Name and description settings:")
        ui_imagebutton_with_text("icons/32x32/control_repeat_blue.png", ["plugin", "random"], u"Random name and description")
        ui_line()
        if  persistent.name_generator_use_name:
            ui_imagebutton_with_text("icons/32x32/check_box.png", ["plugin", "name_checkbox"], u"Autogenerate random name for new characters")
        else:
            ui_imagebutton_with_text("icons/32x32/check_box_empty.png", ["plugin", "name_checkbox"], u"Autogenerate random name for new characters")
        ui_imagebutton_with_text("icons/32x32/user_shuffle.png", ["plugin", "name"], u"Random name (RU)")
        ui_imagebutton_with_text("icons/32x32/user_edit.png", ["plugin", "edit_name"], u"Edit name")
        ui_imagebutton_with_text("icons/32x32/user_delete.png", ["plugin", "clear_name"], u"Clear name")
        ui_line()
        if  persistent.name_generator_use_gatchina:
            ui_imagebutton_with_text("icons/32x32/check_box.png", ["plugin", "gatchina_checkbox"], u"Autogenerate random descriptions for new characters")
        else:
            ui_imagebutton_with_text("icons/32x32/check_box_empty.png", ["plugin", "gatchina_checkbox"], u"Autogenerate random descriptions for new characters")
        ui_imagebutton_with_text("icons/32x32/vcard_shuffle.png", ["plugin", "description"], u"Random description (RU)")
        ui_imagebutton_with_text("icons/32x32/vcard_edit.png", ["plugin", "edit_description"], u"Edit description")
        ui_imagebutton_with_text("icons/32x32/vcard_delete.png", ["plugin", "clear_description"], u"Clear description")
        ui.close()

    def name_generator_get_name():
        import codecs
        f = codecs.open(config.gamedir + '/modules/names/plain_names.txt','r','utf8')
        mascot_name = renpy.random.choice(f.readlines())
        f.close()
        mascot_name = mascot_name[:-1]
        mascot_name = mascot_name[0].upper()+mascot_name[1:]
        mascot_name += u"-тян"
        return mascot_name

    def name_generator_get_gatchina_description():
            try:
                import urllib2
                import re
                regexp = re.compile("document.getElementById\('text'\).innerHTML='((.*\.)[^.]*\.)';document.forms\['rform'\].elements\['query'\].value='';")
                req = urllib2.Request('http://www.gatchina.biz/conversation?q=PATTERN')
                req.add_header('Referer', 'http://www.gatchina.biz/generator')
                r = urllib2.urlopen(req).read()
                r = regexp.match(r).group(1)
                r = r.replace('&nbsp;',' ')
                r = r.replace('&raquo;','"')
                r = r.replace('&laquo;','"')
                out = open(name_generator_temp,'w')
                out.write(r)
                out.close()
                additional_info = r
                
                import cp1251
                import codecs
                def search_1251(name):
                    return cp1251.getregentry()
                codecs.register(search_1251)
                return codecs.open(name_generator_temp,'r','cp1251').read()
            except:
                return u"Error connecting to http://www.gatchina.biz/generator"

    def name_generator_action(button):
        global mascot_name
        global additional_info
        global additional_info_pattern
        if  button in ["on_start"]:
            if  persistent.name_generator_use_gatchina:
                additional_info_pattern = name_generator_get_gatchina_description()
            else:
                additional_info_pattern = ""
            if  persistent.name_generator_use_name:
                mascot_name = name_generator_get_name()
            else:
                mascot_name = ""
        if  button in ["description","random"]:
            additional_info_pattern = name_generator_get_gatchina_description()
        if  button in ["name","random"]:
            mascot_name = name_generator_get_name()
        if  button in ["edit_name"]:
            result = ui_input_window(u"Input new name:",mascot_name)
            if  result != None:
                mascot_name = result
        if  button in ["clear_name"]:
            mascot_name = ""
        if  button in ["edit_description"]:
            result = ui_input_window(u"Input new description (PATTERN is a pattern for character name):",additional_info_pattern)
            if  result != None:
                additional_info_pattern = result
        if  button in ["clear_description"]:
            additional_info_pattern = ""
        if  button in ["gatchina_checkbox"]:
            persistent.name_generator_use_gatchina = not persistent.name_generator_use_gatchina
        if  button in ["name_checkbox"]:
            persistent.name_generator_use_name = not persistent.name_generator_use_name
        additional_info = additional_info_pattern.replace('PATTERN',mascot_name).replace('NRETTAP',mascot_name[::-1])

    def names_reset():
        pass

    def names_get_state():
        return ""

    def names_set_state(state):
        pass

    def name_generator_reset():
        global mascot_name
        global additional_info
        global additional_info_pattern
        additional_info = ""
        additional_info_pattern = ""
        mascot_name = ""

    def name_generator_get_state():
        state = {}
        state["mascot_name"] = mascot_name
        state["additional_info_pattern"] = additional_info_pattern
        return state

    def name_generator_set_state(state):
        global mascot_name
        global additional_info
        global additional_info_pattern
        mascot_name = state["mascot_name"]
        additional_info_pattern = state["additional_info_pattern"]
        additional_info = additional_info_pattern.replace('PATTERN',mascot_name).replace('NRETTAP',mascot_name[::-1])

    current_plugin = {}
    current_plugin["id"] = "name"
    current_plugin["display_icon"] = "icons/32x32/curriculum_vitae.png"
    current_plugin["display_name"] = u"Name Editor"
    current_plugin["interface"] = names_iface
    current_plugin["action"] = name_generator_action
    current_plugin["reset"] = names_reset
    current_plugin["get_state"] = names_get_state
    current_plugin["set_state"] = names_set_state
    current_plugin["version"] = "1.0.0"
    current_plugin["version_history"] = [(u"1.0.0",u"Initial release")]
    current_plugin["priority"] = 50
    current_plugin["is_optional"] = False
    plugin_list += [current_plugin]

    current_plugin = {}
    current_plugin["id"] = "name_generator_ru"
    current_plugin["display_icon"] = "icons/32x32/curriculum_vitae_shuffle.png"
    current_plugin["display_name"] = u"Name Generator (RU only)"
    current_plugin["interface"] = name_generator_iface
    current_plugin["action"] = name_generator_action
    current_plugin["reset"] = name_generator_reset
    current_plugin["get_state"] = name_generator_get_state
    current_plugin["set_state"] = name_generator_set_state
    current_plugin["version"] = "0.8.1"
    current_plugin["version_history"] = [(u"0.8.0",u"Initial release"),(u"0.8.1",u"Minor code refactoring")]
    current_plugin["priority"] = 50
    current_plugin["is_optional"] = True
    plugin_list += [current_plugin]
