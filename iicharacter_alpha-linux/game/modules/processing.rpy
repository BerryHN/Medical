init python:

    def transform_iface(options=None):
        ui.vbox()
        crop = mascot_export_crop if  mascot_export_crop else mascot_view_crop
        allow = "0123456789-"
        regexp = "^(-|)[0-9]+$"
        regexp_plus = "^[0-9]+$"

        ui_header(u"Crop options")
        if  mascot_export_crop != None:
            ui_imagebutton_with_text("icons/32x32/check_box.png", ["plugin", "need_crop"], u"Crop sprite")
            ui_input_imagebutton_with_text_and_sel("icons/32x32/canvas_size_l.png","crop_0",mascot_export_crop[0],options,u"Crop position, left:",allow,all_of_checks([re_check(regexp),less_check(mascot_export_crop[2])]))
            ui_input_imagebutton_with_text_and_sel("icons/32x32/canvas_size_r.png","crop_2",mascot_export_crop[2],options,u"Crop position, right:",allow,all_of_checks([re_check(regexp),greater_check(mascot_export_crop[0])]))
            ui_input_imagebutton_with_text_and_sel("icons/32x32/canvas_size_t.png","crop_1",mascot_export_crop[1],options,u"Crop position, top:",allow,all_of_checks([re_check(regexp),less_check(mascot_export_crop[3])]))
            ui_input_imagebutton_with_text_and_sel("icons/32x32/canvas_size_b.png","crop_3",mascot_export_crop[3],options,u"Crop position, bottom:",allow,all_of_checks([re_check(regexp),greater_check(mascot_export_crop[1])]))
        else:
            ui_imagebutton_with_text("icons/32x32/check_box_empty.png", ["plugin", "need_crop"], u"Crop sprite")

        ui_header(u"Scale options")
        ui_input_imagebutton_with_text_and_sel("icons/32x32/transform_scale.png","resize",int(round(100*mascot_export_zoom)),options,u"Scale, %:",allow,re_check(regexp_plus))
        ui_input_button_with_text("dimentions","%dx%d"%(int((crop[2]-crop[0])*mascot_export_zoom),int((crop[3]-crop[1])*mascot_export_zoom)),False,u"Sprite dimentions:")

        ui.close()

    def transform_action(button):
        global mascot_export_crop
        global mascot_export_zoom
        if  button in ["on_start","reset"]:
            transform_reset()
        elif  button == "need_crop":
            mascot_export_crop = mascot_view_crop if mascot_export_crop == None else None

        elif  button == ("input","resize"):
            global mascot_export_zoom
            result = ui_input_window("resize",int(100*mascot_export_zoom),transform_iface)
            if  result!= None: 
                mascot_export_zoom = float(int(result)/100.0)
        elif  button == ("prev","resize"):
            global mascot_export_zoom
            mascot_export_zoom = float(round(round(100*mascot_export_zoom)-5)/100.0)
        elif  button == ("next","resize"):
            global mascot_export_zoom
            mascot_export_zoom = float(round(round(100*mascot_export_zoom)+5)/100.0)
        elif  isinstance(button,tuple) and button[0] == "input":
            crop_id = int(button[1][5:])
            result = ui_input_window(button[1],mascot_export_crop[crop_id],transform_iface)
            if  result!= None: 
                mascot_export_crop = (
                        int(result) if crop_id == 0 else mascot_export_crop[0],
                        int(result) if crop_id == 1 else mascot_export_crop[1],
                        int(result) if crop_id == 2 else mascot_export_crop[2],
                        int(result) if crop_id == 3 else mascot_export_crop[3],
                    )
        elif  isinstance(button,tuple) and button[0] == "prev":
            crop_id = int(button[1][5:])
            mascot_export_crop = (
                    mascot_export_crop[0]-10 if crop_id == 0 else mascot_export_crop[0],
                    mascot_export_crop[1]-10 if crop_id == 1 else mascot_export_crop[1],
                    mascot_export_crop[2]-10 if crop_id == 2 else mascot_export_crop[2],
                    mascot_export_crop[3]-10 if crop_id == 3 else mascot_export_crop[3],
                )
        elif  isinstance(button,tuple) and button[0] == "next":
            crop_id = int(button[1][5:])
            mascot_export_crop = (
                    mascot_export_crop[0]+10 if crop_id == 0 else mascot_export_crop[0],
                    mascot_export_crop[1]+10 if crop_id == 1 else mascot_export_crop[1],
                    mascot_export_crop[2]+10 if crop_id == 2 else mascot_export_crop[2],
                    mascot_export_crop[3]+10 if crop_id == 3 else mascot_export_crop[3],
                )

    def transform_reset():
        global mascot_export_crop
        global mascot_export_zoom
        mascot_export_crop = None
        mascot_export_zoom = 1.0


    def transform_get_state():
        state = {}
        state["mascot_export_crop"] = mascot_export_crop
        state["mascot_export_zoom"] = mascot_export_zoom
        return state

    def transform_set_state(state):
        global mascot_export_crop
        global mascot_export_zoom
        mascot_export_crop = state["mascot_export_crop"]
        mascot_export_zoom = state["mascot_export_zoom"]

    current_plugin = {}
    current_plugin["id"] = u"transform"
    current_plugin["display_icon"] = "icons/32x32/transform_layer.png"
    current_plugin["display_name"] = u"Transform"
    current_plugin["interface"] = transform_iface
    current_plugin["action"] = transform_action
    current_plugin["reset"] = transform_reset
    current_plugin["get_state"] = transform_get_state
    current_plugin["set_state"] = transform_set_state
    current_plugin["version"] = "1.0.0"
    current_plugin["version_history"] = [
            (u"1.0.0",u"Initial release: crop, zoom"),
        ]
    current_plugin["priority"] = 70
    current_plugin["is_optional"] = False
    plugin_list += [current_plugin]
