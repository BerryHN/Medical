init python:
    name_prefix_allow = "abcdefghijklmnopqrstuvwxyz01234567890_ "
    name_prefix_re = "^[a-z_][a-z_0-9]*( [a-z_][a-z_0-9]*)*$"

    if  not persistent.saveload_export_dir:
        persistent.saveload_export_dir = config.basedir + os.sep + "export"
    saveload_temp_dir = config.basedir + os.sep + "temp"

    saveload_filename_prefix = "sprite"

    def saveload_get_name(folder):
        pattern = folder + "/" + saveload_filename_prefix + "%04d.png"
        i = 1
        while True:
            fn = pattern % i
            if not os.path.exists(fn):
                break
            i += 1
        return fn

    def saveload_export_png(fname):
        import pygame

        crop = mascot_export_crop if  mascot_export_crop else mascot_view_crop
        args = [(crop[2]-crop[0], crop[3]-crop[1])]
        for p,im_obj,x,y in mascot_view:
            args += [ (x-crop[0], y-crop[1]), im_obj ]
        composite = im.Composite( *args )
        if  mascot_export_zoom != None and mascot_export_zoom != 1.0:
            composite = im.FactorScale(composite, mascot_export_zoom)
        rv = composite.load()
        pygame.image.save(rv,fname)

    def saveload_png_saver(folder,frames,fnames=None):
        import pygame
        result = []
        for i, f in enumerate(frames):
            fname = fnames[i] if  fnames and len(fnames)>i else saveload_get_name(folder)
            pygame.image.save(f,fname)
            result += [fname]
        return result

    def saveload_get_bin_name():
        wrong_sep = "\\" if os.sep == "/" else "/"
        return renpy.config.renpy_base.replace(wrong_sep,os.sep) + os.sep + sys.argv[0].split(os.sep)[-1]

    def saveload_export_func(folder, renpy_export = False):
        renpy_code = saveload_export_func_inner(folder)
        if  renpy_export:
            import platform, os, codecs, shutil
            bin_name = saveload_get_bin_name()
            for i in os.listdir(config_gamedir+"/game/export_base"):
                if  not os.path.exists(folder+os.sep+i):
                    shutil.copy(config_gamedir+"/game/export_base/"+i, folder+os.sep+i.replace(".template",""))
            if  renpy.windows:
                fname = folder + "/run.bat"
                if  not os.path.exists(fname):
                    f = open(fname,"w")
                    f.write('start ' + ' '.join(sys_start_renpy_project_cmd(folder)) + '\n')
                    f.close()            
            else:
                fname = folder + "/run.sh"
                if  not os.path.exists(fname):
                    f = open(fname,"w")
                    f.write(' '.join(sys_start_renpy_project_cmd(folder)) + ' &\n')
                    f.close()            
            fname = folder + "/credits.rpy"
            name, link, icon = provide_credits_info(chsetdirfull, charset)
            credit = '    "{b}%s{/b} character set'%(charset)
            if  name:
                credit += ' by {a=%s}%s{/a}'%(link,name) if link else ' by %s'%(name)
            credit += '"\n'
            f = open(fname,"r")
            lines = f.readlines()
            f.close()
            if  not credit in lines:
                f = open(fname,"a")
                f.write(credit)
                f.close()

            spritename = saveload_filename_prefix
            fname = folder + "/media.rpy"
            f = codecs.open(fname,"r","utf-8")
            spritenames = [l.replace("image ","").split(" = ")[0] for l in f.readlines() if l.startswith("image ")]
            while  spritename in spritenames:
                try:
                    n,i = " ".join(spritename.split(" ")[:-1]), int(spritename.split(" ")[-1])
                except:
                    n,i = spritename, 1
                spritename = n + " %d"%(i+1)
            f.close()
            f = codecs.open(fname,"a","utf-8")
            f.write("image " + spritename + " = " + renpy_code + "\n\n")
            f.close()

            fname = folder + "/script.rpy"
            f = codecs.open(fname,"a","utf-8")
            f.write('    scene bg\n')
            f.write('    show ' + spritename + '\n')
            f.write('    u"'+spritename+'" "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nam cursus. Morbi ut mi. Nullam enim leo, egestas id, condimentum at, laoreet mattis, massa. Sed eleifend nonummy diam. Praesent mauris ante, elementum et, bibendum at, posuere sit amet, nibh. "\n')
            f.write('    $ renpy.pause()\n\n')
            f.close()

    def saveload_export_func_inner(folder):
        try:
            fname = saveload_get_name(folder)
            saveload_export_png(fname)
            return 'u"' + fname.split("/")[-1] + '"' 
        except: pass

        try:
            anim_list = saveload_export_animated_TransitionAnimation(folder,saveload_png_saver)
            if  anim_list != None:
                return 'Animation(\n    ' + '\n    '.join(['u"' + i[0] + '", %f,'%i[1] for i in anim_list]) + '\n  )'
        except: pass

        try:
            initial, states, edges = saveload_export_animated_SMAnimation(folder,saveload_png_saver)
            return 'anim.SMAnimation(\n    ' + 'u"' + initial + '",\n    ' + '\n    '.join(['anim.State(u"%s",u"%s"),'%i for i in states]) + '\n    ' + '\n    '.join(['anim.Edge(u"%s",%f,u"%s",prob=%d),'%i for i in edges]) + '\n    showold=True\n  )'
        except: pass

        fnames = saveload_export_static_inner(folder,saveload_png_saver)
        fname = fnames[0].split("/")[-1]
        return 'u"' + fname + '" #unabled to export complex behaviour, only 1 animated layer is supported'

    def saveload_export_animated_TransitionAnimation(folder,saver):
        crop = mascot_export_crop if  mascot_export_crop else mascot_view_crop
        for p,im_obj,x,y in mascot_view:
            if  isinstance(im_obj,renpy.display.anim.TransitionAnimation):
                frames = []
                for im_frame in im_obj.images:
                    args = [(crop[2]-crop[0], crop[3]-crop[1])]
                    for p1,im_obj1,x1,y1 in mascot_view:
                        args += [ (x1-crop[0], y1-crop[1]), im_obj1 if p1 != p else im_frame ]
                    composite = im.Composite( *args )
                    if  mascot_export_zoom != None and mascot_export_zoom != 1.0:
                        composite = im.FactorScale(composite, mascot_export_zoom)
                    frames += [ composite.load() ]
                fnames = saver(folder,frames)
                return [(fn.split("/")[-1], im_obj.delays[i]) for i,fn in enumerate(fnames)]
        return None

    def saveload_export_animated_SMAnimation(folder,saver):
        crop = mascot_export_crop if  mascot_export_crop else mascot_view_crop
        for p,im_obj,x,y in mascot_view:
            if  isinstance(im_obj,renpy.display.anim.SMAnimation):
                frames = []
                for state_image in im_obj.states.itervalues():
                    args = [(crop[2]-crop[0], crop[3]-crop[1])]
                    for p1,im_obj1,x1,y1 in mascot_view:
                        args += [ (x1-crop[0], y1-crop[1]), im_obj1 ]
                        if  p1 == p:
                            args[-1] = state_image.get_image()
                    composite = im.Composite( *args )
                    if  mascot_export_zoom != None and mascot_export_zoom != 1.0:
                        composite = im.FactorScale(composite, mascot_export_zoom)
                    frames += [ composite.load() ]
                fnames = saver(folder,frames)
                return im_obj.initial, [(st.name, fnames[i].split("/")[-1]) for i,st in enumerate(im_obj.states.itervalues())], list(set([(i.old, i.delay, i.new, i.prob) for j in im_obj.edges.itervalues() for i in j ]))
        return None

    def saveload_export_static_inner(folder,saver,fname=None):
        crop = mascot_export_crop if  mascot_export_crop else mascot_view_crop
        args = [(crop[2]-crop[0], crop[3]-crop[1])]
        for p,im_obj,x,y in mascot_view:
            if  isinstance(im_obj,renpy.display.anim.TransitionAnimation):
                args += [ (x-crop[0], y-crop[1]), im_obj.images[0] ]
            elif isinstance(im_obj,renpy.display.anim.SMAnimation):
                args += [ (x-crop[0], y-crop[1]), im_obj.states[im_obj.initial].get_image() ]
            else:
                args += [ (x-crop[0], y-crop[1]), im_obj ]
        composite = im.Composite( *args )
        if  mascot_export_zoom != None and mascot_export_zoom != 1.0:
            composite = im.FactorScale(composite, mascot_export_zoom)
        if  fname:
            return saver(folder, [composite.load()], [fname])
        else:
            return saver(folder, [composite.load()])

    def saveload_export_static(folder,fname=None):
        return saveload_export_static_inner(folder, saveload_png_saver, fname)

    def saveload_iface(options=None):
        ui.vbox()

        ui_header(u"Export options")
        ui_input_imagebutton_with_text("icons/32x32/folder_wrench.png","persistent.saveload_export_dir",persistent.saveload_export_dir,options,u"Export directory:",None,os.path.isdir)
        ui_input_imagebutton_with_text("icons/32x32/textfield.png","filename",saveload_filename_prefix,options,u"File name prefix:",name_prefix_allow,re_check(name_prefix_re))

        ui_header(u"Export method")
        ui_imagebutton_with_text("icons/32x32/picture_save.png",["plugin", "export_all"],u"Save as PNG")
        ui_imagebutton_with_text("icons/32x32/clipboard_sign.png",["plugin", "export_clipboard"],u"Save as PNG and copy to clipboard")
        ui_imagebutton_with_text("icons/32x32/renpy_export.png",["plugin", "export_renpy"],u"Save as PNG and append to RenPy template file")

        ui_header(u"Export results")
        ui_imagebutton_with_text("icons/32x32/folder_picture.png",["plugin", "show_dir"],u"See exported pictures in OS browser")
        ui_imagebutton_with_text("icons/32x32/renpy_run.png",["plugin","renpy_run"] if os.path.exists(persistent.saveload_export_dir+"/script.rpy") else None,u"Run generated RenPy code")
        ui.close()

    def saveload_action(button):
        import os
        global saveload_filename_prefix
        if  button == ("input","filename"):
            result = ui_input_window("filename",saveload_filename_prefix,saveload_iface)
            if  result!= None: 
                saveload_filename_prefix = result
        if  button == ("input","persistent.saveload_export_dir"):
            result = ui_input_window("persistent.saveload_export_dir",persistent.saveload_export_dir,saveload_iface)
            if  result!= None: 
                persistent.saveload_export_dir = result
        if  button == "export_all":
            saveload_export_func(persistent.saveload_export_dir)
        if  button == "export_renpy":
            saveload_export_func(persistent.saveload_export_dir,True)
        if  button == "export_clipboard":
            expected_name = saveload_temp_dir + os.sep + "clipboard.png"
            saveload_export_static(saveload_temp_dir, expected_name)

            import pygame
            import pygame.scrap
            pygame.scrap.init()
            try:
                pygame.scrap.put("FileName",expected_name)
            except:
                pygame.scrap.put(pygame.SCRAP_TEXT,expected_name)

        if  button == "show_dir":
            sys_open_folder(persistent.saveload_export_dir)
        if  button == "renpy_run":
            sys_start_renpy_project(persistent.saveload_export_dir)

    def saveload_reset():
        pass

    def saveload_get_state():
        state = {}
        state["saveload_filename_prefix"] = saveload_filename_prefix
        return state

    def saveload_set_state(state):
        global saveload_filename_prefix
        saveload_filename_prefix = state["saveload_filename_prefix"]

    current_plugin = {}
    current_plugin["id"] = u"export"
    current_plugin["display_icon"] = "icons/32x32/picture_save.png"
    current_plugin["display_name"] = u"Export"
    current_plugin["interface"] = saveload_iface
    current_plugin["action"] = saveload_action
    current_plugin["reset"] = saveload_reset
    current_plugin["get_state"] = saveload_get_state
    current_plugin["set_state"] = saveload_set_state
    current_plugin["version"] = "1.2.0"
    current_plugin["version_history"] = [
            (u"1.0.0",u"Initial release"),
            (u"1.1.0",[u"Support for anim.SMAnimation layers",u"Moved export directory",u"Export to clipboard"]),
            (u"1.2.0",[u"Crop support",u"Filename prefix input",u"Export to RenPy test game",u"Starting RenPy test game",u"Added credits to RenPy test game"]),
        ]
    current_plugin["priority"] = 40
    current_plugin["is_optional"] = False
    plugin_list += [current_plugin]
