init -1024 python:
    version_history = [
        (u"1.0.0",u"Initial release"),
        (u"1.1.0",[
            u"Added version history",
            u"Moved save/load directory",
            u"Additional widget localization mechanism",
            u"Layers with position offset",
            u"Fixed transparency bug for non-software rendering"
        ]),
        (u"1.2.0",[
            u"Crop support",
            u"Tweaks for widget disabling",
            u"Managed text input",
            u"Toggle plugins visability",
        ]),
    ]
    version = version_history[-1][0]
    plugin_list = []

    detailed_view_mode = False

    additional_info = ""
    mascot_name = ""
    mascot_view = []
    mascot_view_zoom = 1.0
    mascot_view_crop = (0, 0, 1, 1)
    mascot_export_zoom = 1.0
    mascot_export_crop = None

    mascot_view_x = 716
    mascot_view_y = 92

    states_history_max = 42
    states_history_next = 0
    states_history = []

    if  persistent.plugin_display == None:
        persistent.plugin_display = {}
    if  persistent.current_lang == None:
        persistent.current_lang = "en"
    localization = {}
    localization_prefix = {}
    localization_suffix = {}

    save_dir = "../profiles"

    if  persistent.current_file == None:
        persistent.current_file = "default"

    tmp_vp_plugin_yadjustment = None
    tmp_is_in_input = False

    def local_text(text,args=None):
        global localization
        if  (persistent.current_lang in localization):
            prefix = ""
            suffix = ""
            if  persistent.current_lang in localization_prefix:
                prefix = localization_prefix[persistent.current_lang]
            if  persistent.current_lang in localization_suffix:
                suffix = localization_suffix[persistent.current_lang]
            if  isinstance(text,str):
                text = unicode(text)
            if  text in localization[persistent.current_lang]:
                text = localization[persistent.current_lang][text]
            if  isinstance(args,unicode) and args in localization[persistent.current_lang]:
                args = localization[persistent.current_lang][args]
            text = prefix + text + suffix
        if  args == None:
            return text
        return text % args



    def run_on_start():
        if len(plugin_list) == 0:
            renpy.error("At least 1 plugin should exist!")
        global active_plugin
        global plugin_display_list
        plugin_display_list = []
        plugin_display_list_tmp = [(x["priority"],x) for x in plugin_list]
        plugin_display_list_tmp.sort()
        for (p,x) in plugin_display_list_tmp:
            plugin_display_list = [ x ] + plugin_display_list
        for p in plugin_list:
            if  not p["id"] in persistent.plugin_display:
                persistent.plugin_display[p["id"]] = not p["is_optional"]
        active_plugin = [p for p in plugin_display_list if persistent.plugin_display[p["id"]]][0]
        try:
            fname = config.gamedir + '/' + save_dir + '/' + persistent.current_file
            load_state(fname)
        except:
            for p in plugin_display_list:
                p["action"]("on_start")

    def collect_state():
        result = {}
        for p in plugin_display_list:
            result[p["id"]] = p["get_state"]()
        return result

    def save_new_state():
        global states_history
        global states_history_next
        while  len( states_history ) > states_history_next:
            states_history.pop(states_history_next)
        states_history += [ collect_state() ]
        states_history_next += 1
        while  len( states_history ) > states_history_max:
            states_history.pop(0)
            states_history_next -= 1

    def button_new():
        for p in plugin_list:
            p["action"]("reset")
            p["action"]("on_start")
        save_new_state()

    def load_state(fname):
        import pickle
        f = open(fname, 'rb')
        state = pickle.load(f)
        for p in plugin_display_list:
            if  p["id"] in state:
                p["set_state"](state[p["id"]])
        save_new_state()

    def button_load():
        global states_history
        global states_history_next
        fname = ui_additional_window(load_iface,"icons/32x32/disk_multiple.png")
        if  fname == None:
            return
        persistent.current_file = fname

        fname = config.gamedir + '/' + save_dir + '/' + persistent.current_file
        load_state(fname)

    def button_saveas():
        import pickle
        global states_history
        global states_history_next
        result = ui_additional_window(save_iface,"icons/32x32/disk_multiple.png")
        if  result == None:
            return

        if  result == "edit":
            fname = ui_input_window(u"Input a new file name:",persistent.current_file)
            if  fname == None:
                return
            persistent.current_file = fname
        elif isinstance(result, list) and result[0] == "name":
            persistent.current_file = result[1]
        else:
            return

        fname = config.gamedir + '/' + save_dir + '/' + persistent.current_file
        f = open(fname, 'wb')
        pickle.dump(states_history[states_history_next-1], f) 

    def button_config():
        global active_plugin
        while True:
            result = ui_additional_window(conf_iface,"icons/32x32/cog.png")
            if  result == None or not result in persistent.plugin_display:
                return
            persistent.plugin_display[result] = not persistent.plugin_display[result]
            if  active_plugin["id"] == result:
                active_plugin = [p for p in plugin_display_list if persistent.plugin_display[p["id"]]][0]

    def button_undo():
        global states_history_next
        states_history_next -= 1
        result = states_history[states_history_next-1]
        for p in plugin_display_list:
            p["set_state"](result[p["id"]])

    def button_redo():
        global states_history_next
        states_history_next += 1
        result = states_history[states_history_next-1]
        for p in plugin_display_list:
            p["set_state"](result[p["id"]])

    def load_iface(options):
        ui.vbox()
        ui_header(u"Load configuration:")
        for i in os.listdir(unicode(config.gamedir + '/' + save_dir)):
            ui_imagebutton_with_text("icons/32x32/folder_go.png",["return",i],"{font=FOT-BudoStd-L.otf}"+i+"{/font}")
        ui.close()

    def save_iface(options):
        ui.vbox()
        ui_header(u"Save configuration:")
        ui_imagebutton_with_text("icons/32x32/save_as.png",["return","edit"],u"Input a name")
        ui_header(u"Rewrite configuration:")
        for i in os.listdir(unicode(config.gamedir + '/' + save_dir)):
            ui_imagebutton_with_text("icons/32x32/disk.png",["return",["name",i]],"{font=FOT-BudoStd-L.otf}"+i+"{/font}")
        ui.close()
    
    def conf_iface(options):
        ui.vbox()
        ui_header(u"Toggle plugins displaying:")
        n_allowed = len([p for p in plugin_display_list if persistent.plugin_display[p["id"]]])
        for p in plugin_display_list:
            if  persistent.plugin_display[p["id"]]:
                if  n_allowed > 1:
                    ui_imagebutton_with_text(p["display_icon"],["return",p["id"]],"%s %s",(p["display_name"],p["version"]))
                else:
                    ui_image_with_text(p["display_icon"],"%s %s",(p["display_name"],p["version"]))
            else:
                ui_imagebutton_with_text(im.Alpha(im.Grayscale(p["display_icon"]),0.5),["return",p["id"]],"%s %s (disabled)",(p["display_name"],p["version"]))
        ui.close()
    
    def plugin_viewer_iface(iface_func,do_draw_icons=True,alternative_tab=None,options=None):
        ui.vbox()
        ui.hbox(xfill=True)
        ui.side(['l', 'c', 'r'])
        ui.hbox()
        if  do_draw_icons:
            ui.imagebutton(
                        "icons/32x32/page.png",im.Sepia("icons/32x32/page.png"),clicked=ui.returns(["viewer","new"]),
                        left_padding=80,right_padding=0,top_padding=3,bottom_padding=-5
                    )
            ui.imagebutton(
                        "icons/32x32/folder.png",im.Sepia("icons/32x32/folder.png"),clicked=ui.returns(["viewer","load"]),
                        left_padding=24,right_padding=0,top_padding=3,bottom_padding=-5
                    )
            ui.imagebutton(
                        "icons/32x32/disk.png",im.Sepia("icons/32x32/disk.png"),clicked=ui.returns(["viewer","saveas"]),
                        left_padding=24,right_padding=0,top_padding=3,bottom_padding=-5
                    )
            if  states_history_next > 1:
                ui.imagebutton(
                        "icons/32x32/arrow_undo.png",im.Sepia("icons/32x32/arrow_undo.png"),clicked=ui.returns(["viewer","undo"]),
                        left_padding=24,right_padding=0,top_padding=3,bottom_padding=-5
                    )
            else:
                ui.imagebutton(
                        im.Grayscale("icons/32x32/arrow_undo.png"),im.Grayscale("icons/32x32/arrow_undo.png"),clicked=None,
                        left_padding=24,right_padding=0,top_padding=3,bottom_padding=-5
                    )
            if  states_history_next < len(states_history):
                ui.imagebutton(
                        "icons/32x32/arrow_redo.png",im.Sepia("icons/32x32/arrow_redo.png"),clicked=ui.returns(["viewer","redo"]),
                        left_padding=24,right_padding=0,top_padding=3,bottom_padding=-5
                    )
            else:
                ui.imagebutton(
                        im.Grayscale("icons/32x32/arrow_redo.png"),im.Grayscale("icons/32x32/arrow_redo.png"),clicked=None,
                        left_padding=24,right_padding=0,top_padding=3,bottom_padding=-5
                    )
            ui.imagebutton(
                        "icons/32x32/help.png",im.Sepia("icons/32x32/help.png"),clicked=ui.returns(["viewer","help"]),
                        left_padding=24,right_padding=0,top_padding=3,bottom_padding=-5
                    )
            ui.imagebutton(
                        "icons/32x32/cog.png",im.Sepia("icons/32x32/cog.png"),clicked=ui.returns(["viewer","config"]),
                        left_padding=24,right_padding=0,top_padding=3,bottom_padding=-5
                    )
            detailed_view_mode_image = "icons/32x32/layouts_header_2.png" if detailed_view_mode else "icons/32x32/layouts_header_3_mix.png"
            ui.imagebutton(
                        detailed_view_mode_image,im.Sepia(detailed_view_mode_image),clicked=ui.returns(["viewer","detailed_view_mode"]),
                        left_padding=290,right_padding=0,top_padding=3,bottom_padding=-5
                    )
        ui.close()
        ui.hbox(xfill=True)
        ui.close()
        ui.hbox()
        for l in ["en","jp","ru"]:
            if  l == persistent.current_lang:
                ui.imagebutton(
                        "icons/32x32/flag_"+l+".png","icons/32x32/flag_"+l+".png",clicked=None,
                        left_padding=0,right_padding=24,top_padding=3,bottom_padding=-5
                    )
            else:
                ui.imagebutton(
                        im.Sepia("icons/32x32/flag_"+l+".png"),"icons/32x32/flag_"+l+".png",clicked=ui.returns(["lang",l]),
                        left_padding=0,right_padding=24,top_padding=3,bottom_padding=-5
                    )
        ui.close()
        ui.close()
        ui.close()
        ui.hbox()
        ui.vbox()
        ui.label("",None,bottom_margin=20)
        allowed_plugins = [p for p in plugin_display_list if persistent.plugin_display[p["id"]]]
        margin = 40
        if len(allowed_plugins) >= 2:
            margin = min(40,(710-58*len(allowed_plugins))/(len(allowed_plugins)-1))
        if  alternative_tab:
            ui.frame(
                style=style.file_picker_frame,yfill=False,bottom_margin=margin,top_margin=0,right_margin=-8,
                left_padding=6,right_padding=6,bottom_padding=12,top_padding=12
            )
            ui.image(alternative_tab)
            ui.frame(
                style=style.file_picker_frame,yfill=False,bottom_margin=margin,top_margin=0,right_margin=-10,
                left_padding=6,right_padding=4,bottom_padding=12,top_padding=12
            )
            ui.imagebutton(im.Sepia("icons/32x32/cross.png"),"icons/32x32/cross.png",clicked=ui.returns(["return",None]))
        else:
            for p in allowed_plugins:
                if p != active_plugin:
                    ui.frame(
                        style=style.file_picker_frame,yfill=False,bottom_margin=margin,top_margin=0,right_margin=-10,
                        left_padding=6,right_padding=4,bottom_padding=12,top_padding=12
                    )
                    ui.imagebutton(im.Sepia(p["display_icon"]),p["display_icon"],clicked=ui.returns(["plugin_list",p]))
                else:
                    ui.frame(
                        style=style.file_picker_frame,yfill=False,bottom_margin=margin,top_margin=0,right_margin=-8,
                        left_padding=6,right_padding=6,bottom_padding=12,top_padding=12
                    )
                    ui.image(p["display_icon"])
        ui.close()
        ui.frame(style=style.file_picker_frame,xmaximum=650,ymaximum=736,xminimum=650,yminimum=736)
        ui.hbox()


        #TODO: check for fix of http://lemmasoft.renai.us/forums/viewtopic.php?f=32&t=12790
        global vp_plugin
        global tmp_vp_plugin_yadjustment
        vp_plugin = ui.viewport(mousewheel=True,child_size=(600, 65535))
        if  tmp_vp_plugin_yadjustment != None:
            vp_plugin.yadjustment = tmp_vp_plugin_yadjustment
        if  do_draw_icons:
            iface_func()
        else:
            iface_func(options)

        ui.hbox(xminimum=50)
        ui.bar(adjustment=vp_plugin.yadjustment, style='vscrollbar')
        ui.close()
        ui.close()

        ui.vbox()

        ui.frame(style=style.file_picker_frame,xmaximum=572,ymaximum=50,xminimum=572,yminimum=50) 
        ui.label(mascot_name,None)

        if  detailed_view_mode:
            ui.frame(style=style.file_picker_frame,xmaximum=572,ymaximum=514,xminimum=572,yminimum=514) 
        else:
            ui.frame(style=style.file_picker_frame,xmaximum=572,ymaximum=686,xminimum=572,yminimum=686) 
        ui.fixed()
        mascot_view_dx = int(556.0 - (mascot_view_crop[2]+mascot_view_crop[0])*mascot_view_zoom)/2
        mascot_view_dy = - int(mascot_view_crop[1]*mascot_view_zoom)
        renpy.config.screenshot_crop = [
                mascot_view_x + int(mascot_view_crop[0]*mascot_view_zoom) + mascot_view_dx,
                mascot_view_y + int(mascot_view_crop[1]*mascot_view_zoom) + mascot_view_dy,
                int((mascot_view_crop[2]-mascot_view_crop[0])*mascot_view_zoom),
                int((mascot_view_crop[3]-mascot_view_crop[1])*mascot_view_zoom)
            ]
        for p,im_obj,x,y in mascot_view:
            if  mascot_view_zoom != 1.0:
                ui.at(Position(xpos=mascot_view_dx+int(round(x*mascot_view_zoom)),ypos=mascot_view_dy+int(round(y*mascot_view_zoom)),xanchor="left",yanchor="top"))
#NOTE TO SELF: never use im.FactorScale()
#                ui.image(im.FactorScale(im_obj,mascot_view_zoom))
                ui.at(Transform(child=None,zoom=mascot_view_zoom))
            else:
                ui.at(Position(xpos=mascot_view_dx+x,ypos=mascot_view_dy+y,xanchor="left",yanchor="top"))
            ui.image(im_obj)
        if  mascot_export_crop != None:
            x,y,w,h = mascot_export_crop[0]-1, mascot_export_crop[1]-1, mascot_export_crop[2] - mascot_export_crop[0]+2, mascot_export_crop[3] - mascot_export_crop[1]+2
            ui.at(Position(xpos=mascot_view_dx+int(round(x*mascot_view_zoom)),ypos=mascot_view_dy+int(round(y*mascot_view_zoom)),xanchor="left",yanchor="top",xmaximum=int(round(w*mascot_view_zoom)),ymaximum=int(round(h*mascot_view_zoom)),xfill=False,yfill=False))
            ui.image(Frame("crop_frame.png",2,2))
        ui.close()
           

        if  detailed_view_mode:
            ui.frame(style=style.file_picker_frame,xmaximum=560,ymaximum=172,xminimum=560,yminimum=172) 
            ui.hbox()
            vp_info = ui.viewport(mousewheel=True)
            ui.label(additional_info,None)
            ui.hbox(xminimum=50)
            ui.bar(adjustment=vp_info.yadjustment, style='vscrollbar')
            ui.close()
            ui.close()

        ui.close()
        ui.close()
        ui.close()


label splashscreen:
    jump start

label start:
    scene futaba_bg
    $ run_on_start()
    $ states_history = [ collect_state() ]
    $ states_history_next = 1
    jump viewer

label viewer:
    scene futaba_bg
    python:
        plugin_viewer_iface(active_plugin["interface"])
        renpy.free_memory()
        [group,result] = ui.interact()
        global vp_plugin
        global tmp_vp_plugin_yadjustment
        global detailed_view_mode
        tmp_vp_plugin_yadjustment = vp_plugin.yadjustment
        if  group == "plugin_list":
            active_plugin = result
            tmp_vp_plugin_yadjustment = None
        elif group == "plugin":
            active_plugin["action"](result)
            save_new_state()
        elif group == "viewer":
            if  result == "new":
                button_new()
            elif result == "load":
                button_load()
            elif result == "saveas":
                button_saveas()
            elif result == "undo":
                button_undo()
            elif result == "redo":
                button_redo()
            elif result == "help":
                renpy.curried_call_in_new_context("lurkmore")()
            elif result == "config":
                button_config()
            elif result == "detailed_view_mode":
                detailed_view_mode = not detailed_view_mode
            else:
                renpy.error(result)
        elif group == "lang":
            persistent.current_lang = result
        else:
            renpy.error(group)
    jump viewer

label after_action:    
    $ save_new_state()
    jump viewer
