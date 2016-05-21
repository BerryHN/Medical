init -1025 python:

    def ui_input_imagebutton_with_text_and_sel(imgbutton,name,value,options,text,allow=None,result_checker=None):
        ui.hbox()
        if  tmp_is_in_input:
            ui.imagebutton(im.Sepia(imgbutton),im.Sepia(imgbutton),clicked=None,top_padding=1,left_padding=48,right_padding=6)
            ui_text(text,yalign=0.5,left_padding=0,right_padding=4)
            ui.imagebutton(im.Grayscale("icons/32x32/resultset_previous.png"),im.Grayscale("icons/32x32/resultset_previous.png"),clicked=None)
            ui_input_button(name,value,options,allow,result_checker)
            ui.imagebutton(im.Grayscale("icons/32x32/resultset_next.png"),im.Grayscale("icons/32x32/resultset_next.png"),clicked=None)
        else:
            ui.imagebutton(imgbutton,im.Sepia(imgbutton),clicked=ui.returns(["plugin",("input",name)]),top_padding=1,left_padding=48,right_padding=6)
            ui_text(text,yalign=0.5,left_padding=0,right_padding=4)
            if  result_checker and result_checker("%d"%(int(value)-10)):
                ui.imagebutton("icons/32x32/resultset_previous.png",im.Sepia("icons/32x32/resultset_previous.png"),clicked=ui.returns(["plugin",("prev",name)]))
            else:
                ui.imagebutton(im.Sepia("icons/32x32/resultset_previous.png"),im.Sepia("icons/32x32/resultset_previous.png"),clicked=None)
            ui_input_button(name,value,options,allow,result_checker)
            if  result_checker and result_checker("%d"%(int(value)+10)):
                ui.imagebutton("icons/32x32/resultset_next.png",im.Sepia("icons/32x32/resultset_next.png"),clicked=ui.returns(["plugin",("next",name)]))
            else:
                ui.imagebutton(im.Sepia("icons/32x32/resultset_next.png"),im.Sepia("icons/32x32/resultset_next.png"),clicked=None)

        ui.close()

    def ui_imagebutton_with_text(imgbutton,returns,text,args=None):
        ui.hbox()
        if  tmp_is_in_input or returns == None:
            ui.imagebutton(im.Sepia(imgbutton),im.Sepia(imgbutton),clicked=None,top_padding=1,left_padding=48,right_padding=6)
        else:
            if returns != None:
                ui.imagebutton(imgbutton,im.Sepia(imgbutton),clicked=ui.returns(returns),top_padding=1,left_padding=48,right_padding=6)
            else:
                ui.imagebutton(imgbutton,imgbutton,clicked=None,top_padding=1,left_padding=48,right_padding=6)
        layout.label(local_text(text,args), None, top_padding=7)
        ui.close()

    def ui_image_with_text(imgbutton,text,args=None):
        ui.hbox()
        ui.imagebutton(imgbutton,imgbutton,None,top_padding=1,left_padding=48,right_padding=6)
        layout.label(local_text(text,args), None, top_padding=7)
        ui.close()

    def ui_imagebutton(imgbutton,returns):
        if returns != None:
            ui.imagebutton(imgbutton,im.Sepia(imgbutton),clicked=ui.returns(returns),top_padding=1,left_padding=48,right_padding=6)
        else:
            ui.imagebutton(imgbutton,imgbutton,clicked=None,top_padding=1,left_padding=48,right_padding=6)

    def ui_imagebutton_nopadding(imgbutton,returns):
        if returns != None:
            ui.imagebutton(imgbutton,im.Sepia(imgbutton),clicked=ui.returns(returns))
        else:
            ui.imagebutton(imgbutton,imgbutton,clicked=None)

    def ui_header(text,args=None):
        layout.label("", None)
        layout.label(local_text(text,args), "header", left_padding=16)

    def ui_text(text,args=None,**kwargs):
        if  not "left_padding" in kwargs:
            kwargs["left_padding"] = 16
        layout.label(local_text(text,args), None, **kwargs)

    def ui_line():
        layout.label("", None)

    def ui_additional_window_ignore(group,result):
        return None

    def ui_input_imagebutton_with_text(imgbutton,name,value,options,text,allow=None,result_checker=None):
        ui.hbox()
        if  tmp_is_in_input:
            ui.imagebutton(im.Sepia(imgbutton),im.Sepia(imgbutton),clicked=None,top_padding=1,left_padding=48,right_padding=6)
        else:
            ui.imagebutton(imgbutton,im.Sepia(imgbutton),clicked=ui.returns(["plugin",("input",name)]),top_padding=1,left_padding=48,right_padding=6)
        ui_text(text,yalign=0.5,left_padding=0,right_padding=4)
        ui_input_button(name,value,options,allow,result_checker)
        ui.close()

    def ui_input_button_with_text(name,value,options,text,allow=None,result_checker=None):
        ui.hbox()
        ui_text(text,yalign=0.5,left_padding=48,right_padding=4)
        ui_input_button(name,value,options,allow,result_checker)
        ui.close()

    def ui_input_button(name,value,options,allow=None,result_checker=None):
        if  isinstance(value, int): value = "%d"%value
        if  isinstance(value, float): value = "%f"%value
        if  options == None:
            ui.button(clicked = ui.returns(["plugin",("input",name)]))
            ui.text(value)
        elif  isinstance(options, tuple) and len(options)==2 and options[0] == name:
            ui.frame(style="button")
            ui.input(value,allow=allow,result_checker=result_checker)
        else: 
            ui.frame(style="button")
            ui.text(value)

    def ui_input_iface(options):
        question_text,original_value = options
        ui.vbox()
        ui_header(question_text)        
        ui.frame(style="button")
        ui.input(original_value)        
        ui.close()
        
    def ui_input_window(question_text,original_value,iface=ui_input_iface):
        global tmp_is_in_input
        tmp_is_in_input = True
        while True:
            plugin_viewer_iface(iface,False,"icons/32x32/textfield.png",(question_text,original_value))
            result = ui.interact()
            if  isinstance(result,list):
                [group,result] = result
                if  group == "lang":
                    persistent.current_lang = result
                    continue
                elif  group == "return":
                    tmp_is_in_input = False
                    return result
            tmp_is_in_input = False
            return result
        
    def ui_additional_window(func_iface,icon="icons/32x32/toolbox.png",options=None,func_callback=ui_additional_window_ignore):
        global tmp_vp_plugin_yadjustment
        tmp_vp_plugin_yadjustment = None
        while True:
            plugin_viewer_iface(func_iface,False,icon,options)
            [group,result] = ui.interact()
            func_callback(group,result)
            if  group == "lang":
                persistent.current_lang = result
            elif  group == "return":
                tmp_vp_plugin_yadjustment = None
                return result
