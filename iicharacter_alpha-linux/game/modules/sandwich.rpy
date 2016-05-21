init -10 python:
    color_limits = {}
    sandwich_list = {}
    current_mascot = {}
    current_sides = {}
    current_recolor = {}
    current_used_colors = {}
    current_limits = {"L":{},"R":{},"C":{}}
    current_limits["L"][-1] = {"_side":"L"}
    current_limits["R"][-1] = {"_side":"R"}
    sorted_keylist = {}
    layergrouplist = {}
    chsetdir = 'charsets/'
    config_gamedir = config.basedir.replace('\\','/')
    chsetdirfull = config_gamedir + '/' + chsetdir

    chset_localization = {}

init python:
    import os
    def chset_localize(str):
        lang = persistent.current_lang
        if  lang in chset_localization:
            if  charset in chset_localization[lang]:
                if  str in chset_localization[lang][charset]:
                    prefix = "" if not lang in localization_prefix else localization_prefix[lang]
                    suffix = "" if not lang in localization_suffix else localization_suffix[lang]
                    return prefix + chset_localization[persistent.current_lang][charset][str] + suffix
        return str

    def add_key_to_sandwich_list( s_list, key, name, path ):
        s_list[key] = {}
        s_list[key]["name"] = name
        s_list[key]["path"] = path
        s_list[key]["items"] = []
        global config_gamedir
        for itemname in os.listdir(config_gamedir + '/' + s_list[key]["path"]):
            s_list[key]["items"] += [itemname]                

    def get_layergroup_for_key(key):
        if  len( sandwich_list[charset][key]["name"].split("@") ) < 2:
            return ""
        return sandwich_list[charset][key]["name"].split("@")[1]

    for charset in os.listdir(chsetdirfull):
        color_limits[charset] = {}
        sandwich_list[charset] = {}
        sorted_keylist_unreduced = [ [(int(i.split(".")[0]),"C")] if not "LR" in i.split(".")[2:] else [(int(i.split(".")[0]),"R"),(int(i.split(".")[0]),"L")] for i in os.listdir(chsetdirfull+charset+'/layers/') ]
        sorted_keylist[charset] = reduce(lambda x,y: x+y, sorted_keylist_unreduced)
        sorted_keylist[charset].sort()
        layergrouplist[charset] = {}
        for layname in os.listdir(chsetdirfull+charset+'/layers/'):
            layname_sp = layname.split(".")
            [priority,name] = layname_sp[:2]
            group = name.split("@")[1] if len(name.split("@"))>1 else ""
            if  group != "" and not group in layergrouplist[charset]:
                layergrouplist[charset][group] = True
            path = chsetdir+charset+'/layers/' + layname
            if "LR" in layname_sp[2:]:
                add_key_to_sandwich_list(sandwich_list[charset], (int(priority),"L"), name, path)
                add_key_to_sandwich_list(sandwich_list[charset], (int(priority),"R"), name, path)
            else:
                add_key_to_sandwich_list(sandwich_list[charset], (int(priority),"C"), name, path)
        for fname in os.listdir(chsetdirfull+charset+'/colors/'):
            colorname, ext = fname.split(".")[0], fname.split(".")[1]
            if  ext == "limits":
                color_limits[charset][colorname] = []
                f = open(chsetdirfull+charset+'/colors/' + fname)
                for line in f.readlines():
                    color_limits[charset][colorname] += [line]
                f.close()

init python:
    charset = "charset"

    def set_item_color(name,color,delta=0.0):
        return lambda x: set_item_color_action(name,color,x-delta)
    
    def set_item_color_action(name,color,x):
        if x < 0.0: x += 1.0
        if x > 1.0: x -= 1.0
        current_recolor[name][color] = x
        fill_mascot_view()
        ui.jumps("after_action")()

    def set_item_custom(name):
        return ["plugin",("call",lambda: set_item_custom_action(name))]

    def set_item_custom_action(name):
        current_recolor[name]["custom"] = not current_recolor[name]["custom"]

    def set_item_palette(name,coloring):
        return ["plugin",("call",lambda: set_item_palette_action(name,coloring))]
    
    def set_item_palette_action(name,coloring):
        current_recolor[name]["h"] = coloring[0]
        current_recolor[name]["s"] = coloring[1]
        current_recolor[name]["br"] = coloring[2]
        fill_mascot_view()

    def set_item_rand_tone(name,color):
        return ["plugin",("call",lambda: set_item_rand_tone_action(name,color))]
    
    def set_item_rand_tone_action(name,color):
        current_recolor[name][color] = generate_tone(name,color)
        fill_mascot_view()

    def set_item_rand_hue_sat(name):
        return ["plugin",("call",lambda: set_item_rand_hue_sat_action(name))]
    
    def set_item_rand_hue_sat_action(name):
        h,s,br = generate_hue_sat_br(name,current_recolor[name]["palette"],current_recolor[name]["custom"])
        current_recolor[name]["h"] = h
        current_recolor[name]["s"] = s
        current_recolor[name]["br"] = br
        fill_mascot_view()

    def set_item_default_hue_sat(name):
        return ["plugin",("call",lambda: set_item_default_hue_sat_action(name))]
    
    def set_item_default_hue_sat_action(name):
        current_recolor[name]["h"]  = current_recolor[name]["palette"][0][0][0]
        current_recolor[name]["s"]  = current_recolor[name]["palette"][0][0][1]
        current_recolor[name]["br"] = current_recolor[name]["palette"][0][0][2]
        fill_mascot_view()

    def fill_mascot_view():
        global current_limits
        global current_mascot
        global mascot_view
        global config_gamedir
        global mascot_view_crop
        mascot_view_crop = None
        mascot_view = []
        current_limits = {"L":{},"R":{},"C":{}}
        current_limits["L"][-1] = {"_side":"L"}
        current_limits["R"][-1] = {"_side":"R"}
        for key in sorted_keylist[charset]:
            current_mascot[key]["imagepath"] = config_gamedir + '/' + sandwich_list[charset][key]["path"] + '/'
            current_mascot[key]["imagepath"] +=current_mascot[key]["name"]
            animated_sprites = {}
            state_machines = {}
            state_machines_init = {}
            for imagename in os.listdir(current_mascot[key]["imagepath"]):
                im_priority, im_side = key
                splitname = imagename.split(".")
                state_names = []
                state_edges = []
                if  splitname[-1] in ["png", "ref"]:
                    if  splitname[-1] == "png":
                        im_obj = current_mascot[key]["imagepath"]+'/'+imagename
                    else:                        
                        im_obj = chsetdirfull+charset+'/sheets/'+splitname[0]+'.png'
                    im_obj = im.Image(im_obj)
                    frame_id = None
                    frame_pause = 50
                    state_id = None
                    state_pause = 50
                    state_chance = None
                    state_init = None
                    dx = 0
                    dy = 0
                    for i in range(1,len(splitname)-1,2):
                        if  splitname[i] == "C":
                            im_matrix = [0.5,0,0,0,0,  0,0.5,0,0,0, 0,0,1,0,0, 0,0,0,1,0, 0,0,0,0,1]
                            im_obj = im.MatrixColor(im_obj,im_matrix)
                            im_h = current_recolor[splitname[i+1]]["h"]
                            im_matrix = im.matrix.hue(360.0*im_h)
                            im_obj = im.MatrixColor(im_obj,im_matrix)
                            im_s = current_recolor[splitname[i+1]]["s"]
                            im_matrix = im.matrix.saturation(im_s)
                            im_obj = im.MatrixColor(im_obj,im_matrix)
                            im_b = 2.0 * current_recolor[splitname[i+1]]["br"] - 1.0
                            im_matrix = im.matrix.brightness(im_b)
                            im_obj = im.MatrixColor(im_obj,im_matrix)
                        if  splitname[i] == "H":
                            im_h = int(splitname[i+1])
                            im_matrix = im.matrix.hue(1.0*im_h)
                            im_obj = im.MatrixColor(im_obj,im_matrix)
                        if  splitname[i] == "A":
                            im_a = current_recolor[splitname[i+1]]["a"]
                            im_matrix = [1,0,0,0,0,  0,1,0,0,0, 0,0,1,0,0, 0,0,0,im_a,0, 0,0,0,0,1]
                            im_obj = im.MatrixColor(im_obj,im_matrix)
                        if  splitname[i] == "T":
                            im_h = current_recolor[splitname[i+1]]["h"]
                            im_matrix = im.matrix.hue(360.0*im_h)
                            im_obj = im.MatrixColor(im_obj,im_matrix)
                            im_s = current_recolor[splitname[i+1]]["s"]
                            im_matrix = im.matrix.saturation(im_s)
                            im_obj = im.MatrixColor(im_obj,im_matrix)
                            im_b = 2.0 * current_recolor[splitname[i+1]]["br"] - 1.0
                            im_matrix = im.matrix.brightness(im_b)
                            im_obj = im.MatrixColor(im_obj,im_matrix)

                        if  splitname[i] == "O":
                            im_priority += int(splitname[i+1])
                        if  splitname[i] == "L":
                            im_priority = int(splitname[i+1])

                        if  splitname[i] == "F":
                            frame_id = int(splitname[i+1])
                        if  splitname[i] == "FP":
                            frame_pause = int(splitname[i+1])

                        if  splitname[i] == "S":
                            state_id = splitname[i+1]
                            state_names += [ state_id ]
                        if  splitname[i] == "SI":
                            state_id = splitname[i+1]
                            state_names += [ state_id ]
                            state_init = state_id
                        if  splitname[i] == "SP":
                            state_pause = int(splitname[i+1])
                        if  splitname[i] == "SC":
                            state_chance = int(splitname[i+1])
                        if  splitname[i] == "SD":
                            state_edges += [ (state_id, splitname[i+1], state_pause, state_chance) ]
                            state_pause = 50
                            state_chance = None

                        if  splitname[i] == "CR":
                            splitargs = splitname[i+1].split(",")
                            im_obj = im.Crop(im_obj,int(splitargs[0]),int(splitargs[1]),int(splitargs[2]),int(splitargs[3]))
                        if  splitname[i] == "DX":
                            dx += int(splitname[i+1])
                        if  splitname[i] == "DY":
                            dy += int(splitname[i+1])
                        if  splitname[i] == "LR":
                            delta = int(splitname[i+1])
                            im_w, im_h = im.cache.get(im_obj).get_size()
                            if  im_side == "L":
                                im_obj = im.Crop(im_obj,0,0,delta,im_h)
                            if  im_side == "R":
                                dx += delta
                                im_obj = im.Crop(im_obj,delta,0,im_w-delta,im_h)
                    if  frame_id == None and state_id == None:
                        mascot_view += [(im_priority,im_obj,dx,dy)]
                    elif state_id == None:
                        if  not im_priority in animated_sprites:
                            animated_sprites[im_priority] = {}
                        animated_sprites[im_priority][frame_id] = (im_obj,frame_pause/1000.0)
                    else:
                        if  state_init != None:
                            state_machines_init[im_priority] = state_init
                        if  not im_priority in state_machines:
                            state_machines[im_priority] = []
                        for i in state_names:
                            state_machines[im_priority] += [ anim.State(i,im_obj) ]
                        for (i,j,p,c) in state_edges:
                            if  c == None:
                                state_machines[im_priority] += [ anim.Edge(i,p/1000.0,j) ]
                            else:
                                state_machines[im_priority] += [ anim.Edge(i,p/1000.0,j,prob=c) ]
                elif  splitname[-1] == "size":
                    global mascot_view_crop
                    if  mascot_view_crop != None:
                        mascot_view_crop = (
                            min( mascot_view_crop[0], int(splitname[0]) ),
                            min( mascot_view_crop[1], int(splitname[1]) ),
                            max( mascot_view_crop[2], int(splitname[2]) ),
                            max( mascot_view_crop[3], int(splitname[3]) )
                        )
                    else:
                        mascot_view_crop = ( int(splitname[0]), int(splitname[1]), int(splitname[2]), int(splitname[3]) )
                elif  splitname[-1] == "set":
                    for i in range(0,len(splitname)-1,2):
                        if  not im_priority in current_limits[im_side]:
                            current_limits[im_side][im_priority] = {}
                        current_limits[im_side][im_priority][splitname[i]] = splitname[i+1]
                else:
                    continue
            for im_priority, animation in animated_sprites.iteritems():
                arglist = []
                for frame,(im_obj,pause) in animation.iteritems():
                    arglist += [im_obj,pause]
                mascot_view += [(im_priority,Animation(*arglist),0,0)]
            for im_priority, state_machine in state_machines.iteritems():
                mascot_view += [(im_priority,anim.SMAnimation(state_machines_init[im_priority],*state_machines[im_priority],showold=True),0,0)]
        mascot_view.sort()

    def check_avaliable_internal(priority, sides, limit_key, limit_val, initial, operation):
        result = initial
        found_in = None
        for s in sides:
            for p,l in current_limits[s].iteritems():
                if  p >= priority:
                    continue
                if  found_in and p <= found_in:
                    continue
                if  limit_key in l:
                    result = operation(limit_val,l[limit_key])
                    found_in = p
        return result

    def check_available(key,item):
        priority, side = key
        global current_limits
        splitname = item.split(".")
        i = 1
        while i < len(splitname):
            if splitname[i] == "IF" and len(splitname)-i > 2:
                sides = ["C"] if side == "C" else ["C",side]
                result = check_avaliable_internal(priority,sides,splitname[i+1],splitname[i+2],False,lambda x,y:x==y)
                if  not result:
                    return False
                i += 3
            elif splitname[i] == "IFLR" and len(splitname)-i > 2:
                result = check_avaliable_internal(priority,["L"],splitname[i+1],splitname[i+2],False,lambda x,y:x==y)
                if  not result:
                    return False
                result = check_avaliable_internal(priority,["R"],splitname[i+1],splitname[i+2],False,lambda x,y:x==y)
                if  not result:
                    return False
                i += 3
            elif splitname[i] == "IFNOT" and len(splitname)-i > 2:
                sides = ["C"] if side == "C" else ["C",side]
                result = check_avaliable_internal(priority,sides,splitname[i+1],splitname[i+2],True,lambda x,y:x!=y)
                if  not result:
                    return False
                i += 3
            elif splitname[i] == "X" and len(splitname)-i > 1:
                i += 2
            else:
                renpy.error((priority,splitname))
        return True

    def get_available_items_name(x):
        return x.split(".")[0]

    def get_available_items(key):
        available = [i for i in sandwich_list[charset][key]["items"] if check_available(key,i)]
        available = sorted(available, key = get_available_items_name)
        return available
         
    def get_random_layer(key,available,nomul=False):
        priority, side = key
        if  len(available) == 0:
            renpy.error( (key,"available == []") )
        if  nomul:
            return renpy.random.choice(available)

        available_multi = []
        for name in available:
            mult = 1
            splitname = name.split(".")
            i = 1
            while i < len(splitname):
                if splitname[i] == "IF" and len(splitname)-i > 2:
                    i += 3
                elif splitname[i] == "IFLR" and len(splitname)-i > 2:
                    i += 3
                elif splitname[i] == "IFNOT" and len(splitname)-i > 2:
                    i += 3
                elif splitname[i] == "X" and len(splitname)-i > 1:
                    mult *= int(splitname[i+1])
                    i += 2
                else:
                    renpy.error((key,splitname))
            available_multi += [name]*mult

        if  len(available_multi) == 0:
            global current_limits
            renpy.error( (key,"available_multi == []",available,current_limits[side]) )

        return renpy.random.choice(available_multi)

    def generate_hue_sat_br(name,palette,is_custom):
        if  is_custom:
            for i in range(10000):
                clr = {}
                clr["r"] = renpy.random.choice([0.01*x for x in range(101)])
                clr["g"] = renpy.random.choice([0.01*x for x in range(101)])
                clr["b"] = renpy.random.choice([0.01*x for x in range(101)])
                clr["h"],clr["s"],clr["v"] = count_hsv(clr["r"],clr["g"],clr["b"])
                clr["br"] = renpy.random.choice([0.01*x for x in range(25,76)])
    
                ok = True
                if  name in color_limits[charset]:
                    for limit in color_limits[charset][name]:
                        try:
                            ok = ok and eval(limit,clr)
                        except:
                            pass
                if ok:
                    return clr["h"],clr["s"],clr["br"]
            renpy.error("cannot generate color for layer " + name)
        else:
            return renpy.random.choice([i for i in reduce(lambda x,y:x+y,palette) if isinstance(i,tuple)])

    def generate_tone(name,letter):
        for i in range(10000):
            clr = {}
            clr[letter] = renpy.random.choice([0.5+0.01*x for x in range(51)])
            ok = True
            if  name in color_limits[charset]:
                for limit in color_limits[charset][name]:
                    ok = ok and eval(limit,clr)
            if ok:
                return clr[letter]
        renpy.error("cannot generate tone for layer " + name)

    def fill_color_list():
        global current_recolor
        global current_used_colors
        current_used_colors = {}
        for key in sorted_keylist[charset]:
            if  not "imagepath" in current_mascot[key]:
                renpy.error((key,current_mascot,current_limits))
            for imagename in os.listdir(current_mascot[key]["imagepath"]):
                splitname = imagename.split(".")
                if  not splitname[-1] in ["png","ref"]:
                    continue
                for i in range(1,len(splitname)-1):
                    if  splitname[i] == "C":
                        current_used_colors[splitname[i+1]] = "T"
                    if  splitname[i] == "A":
                        current_used_colors[splitname[i+1]] = "A"
                    if  splitname[i] == "T":
                        current_used_colors[splitname[i+1]] = "T"
        for name in current_used_colors:
            if  not name in current_recolor:
                item = {}
                item["type"] = current_used_colors[name]
                if  item["type"] == "A":
                    item["a"] = generate_tone(name,"a")
                if  item["type"] == "T":
                    fname = name+".palette"
                    if fname in os.listdir(chsetdirfull+charset+'/colors/'):
                        item["palette"] = []
                        f = open(chsetdirfull+charset+'/colors/' + fname)
                        for line in f.readlines():
                            item["palette"] += [eval(line,None,None)]
                        f.close()
                    else:
                        item["palette"] = [
                                [(i/12.0,1.0,0.5) for i in range(12)]+[[0.0,0.0,1.0],(0.0,0.0,0.5),None],
                                [(i/12.0,0.7,0.4) for i in range(12)]+[[0.0,0.0,0.0],(0.0,0.0,0.4),(0.0,0.0,0.6)]
                            ]
                    fname = name+".delta"
                    if fname in os.listdir(chsetdirfull+charset+'/colors/'):
                        f = open(chsetdirfull+charset+'/colors/' + fname)
                        item["delta"] = eval(f.readline(),None,None)
                        f.close()
                    else:
                        item["delta"] = 0
                    item["custom"] = False
                    item["h"],item["s"],item["br"] = generate_hue_sat_br(name,item["palette"],item["custom"])
                current_recolor[name] = item

    def sandwich_color_iface():
        ui.vbox()
        ui_header(u"Set colors:")
        ui_imagebutton_with_text("icons/32x32/control_repeat_blue.png", ["plugin", "reset"], u"Random colors")
        ui_imagebutton_with_text("icons/32x32/control_rewind_blue.png", ["plugin", "rewind"], u"Default colors")
        ui_line()
        sorted_recolor = [i for i in current_used_colors]
        sorted_recolor.sort()
        for name in sorted_recolor:
            item = current_recolor[name]
            if  item["type"] == "A":
                ui_text(u"Transparency of %s:",name)
                ui.hbox()
                ui_imagebutton("icons/32x32/control_repeat_blue.png",set_item_rand_tone(name,"a"))
                ui.bar(1.0, item["a"], changed=set_item_color(name,"a"), yminimum=20, style="black_slider")
                ui.close()
            if  item["type"] == "T":
                ui_text(u"Hue, saturation and brightness of %s:",name)
                ui.hbox()
                ui.vbox()
                ui_imagebutton("icons/32x32/control_repeat_blue.png",set_item_rand_hue_sat(name))
                ui_imagebutton("icons/32x32/control_rewind_blue.png",set_item_default_hue_sat(name))
                ui.close()
                if  item["custom"]:
                    ui.vbox(xmaximum=(len(item["palette"][0])-1)*32)
                    val = item["h"]+item["delta"]
                    if val < 1.0: val += 1.0
                    if val > 1.0: val -= 1.0
                    ui.bar(1.0, val, changed=set_item_color(name,"h",item["delta"]), yminimum=20, style="rainbow_slider")
                    ui.bar(1.0, item["s"], changed=set_item_color(name,"s"), yminimum=20, style="saturation_slider")
                    ui.bar(1.0, item["br"], changed=set_item_color(name,"br"), yminimum=20, style="brightness_slider")
                    ui.close()
                    ui.imagebutton("icons/32x32/color_wheel.png",im.Sepia("icons/32x32/color_wheel.png"),clicked=ui.returns(set_item_custom(name)),top_margin=1)
                else:
                    ui.vbox()
                    for pal in item["palette"]:
                        ui.hbox()
                        for p in pal:
                            if p == None:
                                ui.imagebutton("icons/32x32/color_wheel.png",im.Sepia("icons/32x32/color_wheel.png"),clicked=ui.returns(set_item_custom(name)),top_margin=1)
                            else:
                                if p[2] == 0.0:
                                    icon = "icons/32x32/radiobutton_black.png"
                                elif p[2] == 1.0:
                                    icon = "icons/32x32/radiobutton_white.png"
                                else:
                                    icon = "icons/32x32/radiobutton_empty.png"
                                    matrix = im.matrix.hue(360.0*(p[0]-item["delta"])+30.0)
                                    icon = im.MatrixColor(icon,matrix)
                                    matrix = im.matrix.saturation(1.5*p[1])
                                    icon = im.MatrixColor(icon,matrix)
                                    matrix = im.matrix.brightness(2.0*p[2]-1.0)
                                    icon = im.MatrixColor(icon,matrix)
                                if (item["h"],item["s"],item["br"]) == (p[0],p[1],p[2]):
                                    icon = im.Composite(None,(0,0),icon,(0,0),"icons/32x32/radiobutton_used.png")
                                ui.imagebutton(icon,im.Sepia(icon),clicked=ui.returns(set_item_palette(name,p)),top_margin=1)
                        ui.close()
                    ui.close()
                ui.close()
            ui_line()
        ui.close()

    def sandwich_color_action(button):
        if  button == "on_start":
            return
        if  button == "reset":
            global current_recolor
            global current_used_colors
            current_used_colors = {}
            current_recolor = {}
            fill_color_list()
            fill_mascot_view()
            return
        if  button == "rewind":
            global current_recolor
            for c, item in current_recolor.iteritems():
                if item["type"] == "T":
                   item["h"]  = item["palette"][0][0][0]
                   item["s"]  = item["palette"][0][0][1]
                   item["br"] = item["palette"][0][0][2]
            fill_color_list()
            fill_mascot_view()
            return
        (what,arg) = button
        if  what == "call":
            arg()
        fill_color_list()
        fill_mascot_view()
        
    def sandwich_color_reset():
        global current_mascot
        current_mascot = {}

    def sandwich_color_get_state():
        state = {}
        return state

    def sandwich_color_set_state(state):
        pass

    current_plugin = {}
    current_plugin["id"] = "colors"
    current_plugin["display_icon"] = "icons/32x32/palette.png"
    current_plugin["display_name"] = u"Colors"
    current_plugin["interface"] = sandwich_color_iface
    current_plugin["action"] = sandwich_color_action
    current_plugin["reset"] = sandwich_color_reset
    current_plugin["get_state"] = sandwich_color_get_state
    current_plugin["set_state"] = sandwich_color_set_state
    current_plugin["version"] = "1.2.0"
    current_plugin["version_history"] = [(u"1.0.0",u"Initial release"),(u"1.1.0",u"Option to revert colors to default values"),(u"1.2.0",[u"Built-in palette of colors and interface for using them",u"Moved color limits to '*.limits' files",u"Support for user-defined palettes in '*.palette' files",u"Support for hue delta between actual layers and interface, now skin hue selector does not look completely shifted anymore"])]
    current_plugin["priority"] = 80
    current_plugin["is_optional"] = False
    plugin_list += [current_plugin]


    def set_layer(key,diff,idx,length):
        if  idx+diff < 0  or idx+diff >= length:
            return None
        if  diff == 0 and length == 1:
            return None

        next = idx+diff
        if  diff == 0:
            next = -1
        return ui.returns(["plugin",("call",lambda: set_layer_action(key,next,idx))])
    
    def set_layer_action(key,idxnew,idxold):
        global current_mascot
        if idxnew != -1:
            current_mascot[key]["name"] = get_available_items(key)[idxnew]
        else:
            available = get_available_items(key)
            oldname = available[idxold]
            for i in range(10):
                current_mascot[key]["name"] = get_random_layer(key,available,True)
                if  current_mascot[key]["name"] != oldname:
                    break
        set_layer_action_after(key)

    def otherkey(key):
        priority, side = key
        otherside = "R" if side == "L" else "L"
        return (priority, otherside)

    def set_layer_action_after(key):
        priority, side = key
        global current_mascot
        global current_sides
        global current_limits
        global config_gamedir

        priority, side = key
        if  side != "C" and not current_sides[priority]:
            current_mascot[otherkey(key)]["name"] = current_mascot[key]["name"]

        for k in sorted_keylist[charset]:
            p,s = k
            if p >=  priority:
                available = get_available_items(k)
                if  not current_mascot[k]["name"] in available:
                    shrtname = current_mascot[k]["name"].split(".")[0]
                    good_available = [ a for a in available if a.split(".")[0] == shrtname and a.find(".X.0.") == -1 ]
                    if len(good_available)>0:
                        current_mascot[k]["name"] = get_random_layer(k,good_available,True)
                    else:
                        current_mascot[k]["name"] = get_random_layer(k,available)
            if p >= priority:
                current_mascot[k]["imagepath"] = config_gamedir + '/' + sandwich_list[charset][k]["path"] + '/'
                current_mascot[k]["imagepath"] +=current_mascot[k]["name"]
                current_limits[s][p] = {}
                for imagename in os.listdir(current_mascot[k]["imagepath"]):
                    splitname = imagename.split(".")
                    if  splitname[-1] == "set":
                        for i in range(0,len(splitname)-1,2):
                            current_limits[s][p][splitname[i]] = splitname[i+1]
        fill_color_list()
        fill_mascot_view()

    def sandwich_layer_iface():
        ui.vbox()
        ui_header(u"Select layers:")
        ui_imagebutton_with_text("icons/32x32/control_repeat_blue.png", ["plugin", "reset"], u"Random layers")
        ui_imagebutton_with_text("icons/32x32/cross.png", ["plugin", ("opt_clear", None)], u"Clear optional layers")
        ui_line()
        sandwich_layer_iface_section("",True)
        for section, opened in layergrouplist[charset].iteritems():
            sandwich_layer_iface_section(section,opened)
        ui.close()

    def sandwich_layer_iface_section(section,opened):
        cnt_nullable = 0
        cnt_available = 0
        for key in sorted_keylist[charset]:
            if  section != get_layergroup_for_key(key): continue
            available = get_available_items(key)
            if  len(available) <= 1: continue
            cnt_available += 1
            if  available.index(current_mascot[key]["name"])!=0 and available[0].split(".")[0] == "-":
                cnt_nullable += 1
        if  not cnt_available:
            return

        if  section != "":
            ui.hbox()
            if  cnt_nullable:
                ui.imagebutton(im.Grayscale("icons/32x32/cross16.png"),"icons/32x32/cross16.png",clicked=ui.returns(["plugin", ("opt_clear",section)]),left_padding=16)
            else:
                ui.imagebutton("icons/32x32/empty.png","icons/32x32/empty.png",clicked=None,left_padding=16)
            ui_imagebutton_nopadding("icons/32x32/control_repeat_blue.png", ["plugin", ("reset",section)])
            layers_icon = "icons/32x32/layers_map_join.png" if opened else "icons/32x32/layers_map.png"
            ui_imagebutton_nopadding(layers_icon,["plugin", ("toggle",section)])
            layout.button(local_text(section), None, clicked=None,xfill=True)
            ui.close()
        if not opened:
            return

        for key in sorted_keylist[charset]:
            if  section != get_layergroup_for_key(key):
                continue
            if  key[1] == "R" and not current_sides[key[0]] and len(get_available_items(otherkey(key))) > 1:
                continue

            available = get_available_items(key)
            if  len(available) <= 1:
                continue
            if  not key in current_mascot or not current_mascot[key]["name"] in available:
                renpy.error((key,current_mascot[key]["name"],available,current_limits,sorted_keylist[charset]))
            idx = available.index(current_mascot[key]["name"])
            pseudolength = sum([0.0 if i.split(".")[0] == "-" else 1.0 if len(i.split(".")[0])>2 else 0.4 for i in available])
            if  len(available) == 2 and available[0].split(".")[0] == "-":
                pseudolength = 0.0

            if  pseudolength <= 2.0:
                ui.hbox()
            else:
                ui.hbox(xmaximum=500)

            if  idx == 0 or available[0].split(".")[0] != "-":
                ui.imagebutton("icons/32x32/empty.png","icons/32x32/empty.png",clicked=None,left_padding=16)
            else:
                ui.imagebutton(im.Grayscale("icons/32x32/cross16.png"),"icons/32x32/cross16.png",clicked=set_layer(key,-idx,idx,len(available)),left_padding=16)

            if  pseudolength <= 2.0:
                ui.imagebutton("icons/32x32/empty.png","icons/32x32/empty.png",clicked=None)
            else:
                ui.imagebutton("icons/32x32/control_repeat_blue.png",im.Sepia("icons/32x32/control_repeat_blue.png"),clicked=set_layer(key,0,idx,len(available)))

            layer_text = "%s: "
            if  key[1] != "C":
                if  current_sides[key[0]]:
                    layer_text = "%s R: " if key[1] == "R" else "%s L: "
                    ui_imagebutton_nopadding("icons/32x32/butterfly_16.png",["plugin",("sides",key)])
                else:
                    ui_imagebutton_nopadding("icons/32x32/butterfly_diff_16.png",["plugin",("sides",key)])
                ui_text(layer_text,sandwich_list[charset][key]["name"].split("@")[0],xminimum=120-32,left_padding=0,yalign=0.5)
            else:
                ui_text(layer_text,sandwich_list[charset][key]["name"].split("@")[0],xminimum=120,left_padding=0,yalign=0.5)

            if  pseudolength <= 2.0:
                for i,item in enumerate(available):
                    if  item.split(".")[0] == "-":
                        continue
                    if  idx == i:
                        ui.imagebutton("icons/32x32/check_box.png",im.Sepia("icons/32x32/check_box.png"),clicked=set_layer(key,-idx,idx,len(available)))
                    else:
                        ui.imagebutton("icons/32x32/check_box_empty.png",im.Sepia("icons/32x32/check_box_empty.png"),clicked=set_layer(key,i-idx,idx,len(available)))
                    if  pseudolength > 0:
                        layout.button(chset_localize(item.split(".")[0]), None, clicked=None,xmaximum=1000)
            else:
                click = set_layer(key,-1,idx,len(available))
                if  click != None:
                    ui.imagebutton("icons/32x32/resultset_previous.png",im.Sepia("icons/32x32/resultset_previous.png"),clicked=click)
                else:
                    ui.imagebutton(im.Grayscale("icons/32x32/resultset_previous.png"),im.Grayscale("icons/32x32/resultset_previous.png"),clicked=None)
                layout.button(chset_localize(current_mascot[key]["name"].split(".")[0]), None,clicked=ui.returns(["plugin", ("layer",key)]),xfill=True)
                click = set_layer(key,+1,idx,len(available))
                if  click != None:
                    ui.imagebutton("icons/32x32/resultset_next.png",im.Sepia("icons/32x32/resultset_next.png"),clicked=click)
                else:
                    ui.imagebutton(im.Grayscale("icons/32x32/resultset_next.png"),im.Grayscale("icons/32x32/resultset_next.png"),clicked=None)
                layout.label(" %d/%d"%(idx+1,len(available)), None,xminimum=100)

            ui.close()
        ui_line()

    def sandwich_layer_selector_iface(options):
        key = options
        global sandwich_list
        global charset
        name = sandwich_list[charset][key]["name"]
        ui.vbox()
        ui_header(u"Select layer for %s:"%name)
        available = get_available_items(key)
        for variant in available:
            if  variant.split(".")[0] != "-":
                ui_imagebutton_with_text("icons/32x32/layer_raster.png",["return",variant],chset_localize(variant.split(".")[0]))
            else:
                ui_imagebutton_with_text("icons/32x32/cross16.png",["return",variant],variant.split(".")[0])
        ui.close()

    def sandwich_layer_action_opt_clear(section):
        global current_limits
        current_limits = {"L":{},"R":{},"C":{}}
        current_limits["L"][-1] = {"_side":"L"}
        current_limits["R"][-1] = {"_side":"R"}
        for key in sorted_keylist[charset]:
            priority, side = key
            available = get_available_items(key)
            current_limits[side][priority] = {}
            if  len(available)>0 and available[0].split(".")[0] == "-" and (section in [None, get_layergroup_for_key(key)]):
                current_mascot[key] = {}
                current_mascot[key]["name"] = available[0]
                current_mascot[key]["imagepath"] = config_gamedir + '/' + sandwich_list[charset][key]["path"] + '/'
                current_mascot[key]["imagepath"] +=current_mascot[key]["name"]
            elif  len(available)>0 and not current_mascot[key]["name"] in available:
                current_mascot[key] = {}
                current_mascot[key]["name"] = get_random_layer(key,available)
                current_mascot[key]["imagepath"] = config_gamedir + '/' + sandwich_list[charset][key]["path"] + '/'
                current_mascot[key]["imagepath"] +=current_mascot[key]["name"]
            for imagename in os.listdir(current_mascot[key]["imagepath"]):
                splitname = imagename.split(".")
                if  splitname[-1] == "set":
                    for i in range(0,len(splitname)-1,2):
                        current_limits[side][priority][splitname[i]] = splitname[i+1]
        fill_color_list()
        fill_mascot_view()

    def sandwich_layer_action_reset(section):
        global current_limits
        current_limits = {"L":{},"R":{},"C":{}}
        current_limits["L"][-1] = {"_side":"L"}
        current_limits["R"][-1] = {"_side":"R"}
        for key in sorted_keylist[charset]:
            priority, side = key
            current_limits[side][priority] = {}
            available = get_available_items(key)
            good_available = []
            if  side == "R" and not current_sides[priority]:
                shrtname = current_mascot[otherkey(key)]["name"].split(".")[0]
                good_available = [ a for a in available if a.split(".")[0] == shrtname ]
            elif not section in [None, get_layergroup_for_key(key)] and not current_mascot[key]["name"] in available:
                shrtname = current_mascot[key]["name"].split(".")[0]
                good_available = [ a for a in available if a.split(".")[0] == shrtname ]
            if len(good_available)>0:            
                available = good_available
            if  len(available)>0 and (section in [None, get_layergroup_for_key(key)] or not current_mascot[key]["name"] in available):
                current_mascot[key] = {}
                current_mascot[key]["name"] = get_random_layer(key,available)
                current_mascot[key]["imagepath"] = config_gamedir + '/' + sandwich_list[charset][key]["path"] + '/'
                current_mascot[key]["imagepath"] +=current_mascot[key]["name"]
            for imagename in os.listdir(current_mascot[key]["imagepath"]):
                splitname = imagename.split(".")
                if  splitname[-1] == "set":
                    for i in range(0,len(splitname)-1,2):
                        current_limits[side][priority][splitname[i]] = splitname[i+1]
        fill_color_list()
        fill_mascot_view()

    def sandwich_layer_action(button):
        global current_mascot
        global current_sides
        global current_limits
        global charset
        global config_gamedir
        if  button == "on_start":
            for key in sorted_keylist[charset]:
                priority, side = key
                if  side != "C":
                    current_sides[key[0]] = False
        if button in ["on_start", "reset"]:
            sandwich_layer_action_reset(None)
            fill_color_list()
            fill_mascot_view()
            return
        try:
            (what,arg) = button
            if  what == "call":
                arg()
            elif  what == "layer":
                key = arg
                result = ui_additional_window(sandwich_layer_selector_iface,"icons/32x32/layer_edit.png",key)
                if  result != None:
                    current_mascot[key]["name"] = result
                    set_layer_action_after(key)
            elif  what == "sides":
                key = arg
                priority, side = arg
                current_sides[priority] = not current_sides[priority]
                set_layer_action_after(key)
            elif  what == "reset":
                sandwich_layer_action_reset(arg)
                return
            elif  what == "opt_clear":
                sandwich_layer_action_opt_clear(arg)
                return
            elif  what == "toggle":
                layergrouplist[charset][arg] = not layergrouplist[charset][arg]
                return
        except:
            pass

    def sandwich_layer_reset():
        pass

    def sandwich_layer_get_state():
        state = {}
        return state

    def sandwich_layer_set_state(state):
        pass

    current_plugin = {}
    current_plugin["id"] = "layers"
    current_plugin["display_icon"] = "icons/32x32/layers_map.png"
    current_plugin["display_name"] = u"Layers"
    current_plugin["interface"] = sandwich_layer_iface
    current_plugin["action"] = sandwich_layer_action
    current_plugin["reset"] = sandwich_layer_reset
    current_plugin["get_state"] = sandwich_layer_get_state
    current_plugin["set_state"] = sandwich_layer_set_state
    current_plugin["version"] = "1.2.0"
    current_plugin["version_history"] = [
        (u"1.0.0",u"Initial release"),
        (u"1.1.0",[
            u"Support for anim.SMAnimation layers",
            u"Fixed bug that prevented project from packaging",
            u"Fixed bug that caused some layers not to disappear",
            u"References, clipping and position offset",
            u"New interface for layers with a few choices"
        ]),
        (u"1.2.0",[
            u"Support for left/right sublayers with separate variables set",
            u"A file modifier to split into left/right sublayers",
            u"Support for layer grouping using '@' sign"
        ])]
    current_plugin["priority"] = 100
    current_plugin["is_optional"] = False
    plugin_list += [current_plugin]


    def sandwich_charset_iface():
        ui.vbox()
        ui_header(u"Select character set:")
        ui_imagebutton_with_text("icons/32x32/control_repeat_blue.png", ["plugin", "reset"], u"Random charset")
        charsets_list = os.listdir(chsetdirfull)
        charsets_list.sort()
        for x in charsets_list:
            cnt = sum([len(p["items"]) for p in sandwich_list[x].itervalues()])
            name, params = x.split(".")[0], x.split(".")[1:]
            if  "M" in params and not "F" in params:
                icon = "icons/32x32/folder_male.png"
            elif "F" in params and not "M" in params:
                icon = "icons/32x32/folder_female.png"
            else:
                icon = "icons/32x32/folder_female_male.png"
            ui.side(['l','c','r'])
            ui.hbox()
            ui_imagebutton_with_text(icon, ["plugin", ("charset",x)], "%s "%name)
            for p in params:
                words = p.split("-")
                if  words[0] == "CC":
                    if  "NA" in words:
                        ui_imagebutton_nopadding("icons/16x16/no_requirements.png",["plugin",("license",(p,x))])
                    if  "BY" in words:
                        ui_imagebutton_nopadding("icons/16x16/attribution.png",["plugin",("license",(p,x))])
                    if  "NC" in words:
                        ui_imagebutton_nopadding("icons/16x16/no_commercial.png",["plugin",("license",(p,x))])
                    if  "ND" in words:
                        ui_imagebutton_nopadding("icons/16x16/non_derivative.png",["plugin",("license",(p,x))])
                    if  "SA" in words:
                        ui_imagebutton_nopadding("icons/16x16/copyleft.png",["plugin",("license",(p,x))])
            ui.close()
            ui.hbox(xfill=True)
            ui.close()
            ui.hbox()
            name, link, icon = provide_credits_info(chsetdirfull, x)
            if  name:
                ui.label(" by %s (%d details)"%(name,cnt), top_padding=7)
            else:
                ui.label(" (%d details)"%(cnt), top_padding=7)
            ui.close()
            ui.close()
        ui_line()
        ui.close()

    def sandwich_license_iface((license,charset)):
        ui.vbox()
        ui_header(u"Character set:")
        ui_imagebutton_with_text("icons/32x32/folder.png", None, charset.split(".")[0])

        name, link, icon = provide_credits_info(chsetdirfull, charset)
        if  name:
            ui_header(u"Author:")
            ui_imagebutton_with_text(icon, ["return", link], name)

        ui_header(u"You are free:")
        ui_imagebutton_with_text("icons/32x32/copying_and_distribution.png",None, u"{b}to Share{/b} — to copy, distribute and transmit the work")
        if not "ND" in license:
            ui_imagebutton_with_text("icons/32x32/derivatives.png",None, u"{b}to Remix{/b} — to adapt the work")
        if not "NC" in license:
            ui_imagebutton_with_text("icons/32x32/commercial.png",None, u"to make commercial use of the work")

        ui_header(u"Under the following conditions:")
        if "NA" in license:
            ui_imagebutton_with_text("icons/32x32/no_requirements.png",None, u"No requirements")
        if "BY" in license:
            ui_imagebutton_with_text("icons/32x32/attribution.png",None, u"{b}Attribution{/b} — you must attribute the work in the manner specified by the author or licensor")
        if "NC" in license:
            ui_imagebutton_with_text("icons/32x32/no_commercial.png",None, u"{b}Noncommercial{/b} — you may not use this work for commercial purposes")
        if "SA" in license:
            ui_imagebutton_with_text("icons/32x32/copyleft.png",None, u"{b}Share Alike{/b} — if you alter, transform, or build upon this work, you may distribute the resulting work only under the same or similar license to this one")
        if "ND" in license:
            #holy crap, what is it doing here?
            ui_imagebutton_with_text("icons/32x32/non_derivative.png",None, u"{b}No Derivative Works{/b} — you may not alter, transform, or build upon this work")

        cc_links = {
                "CC-BY-NC-SA-30":"http://creativecommons.org/licenses/by-nc-sa/3.0/",
                "CC-BY-NC-30":"http://creativecommons.org/licenses/by-nc/3.0/",
                "CC-BY-SA-30":"http://creativecommons.org/licenses/by-sa/3.0/",
                "CC-BY-30":"http://creativecommons.org/licenses/by/3.0/",
            }
        if  license in cc_links:
            ui_header(u"License details:")
            ui_imagebutton_with_text("icons/32x32/user_judge.png", ["return", cc_links[license]], u"Creative Commons 3.0")
            

        ui.close()


    def sandwich_charset_action(button):
        import webbrowser
        new_charset = None
        if  button in ["on_start","reset"]:
            new_charset = renpy.random.choice(os.listdir(chsetdirfull))
        else:
            try:
                (what,arg) = button
            except:
                return
            if what == "url":
                webbrowser.open(arg)
            if  what == "charset":
                new_charset = arg
            if  what == "license":
                while True:
                    result = ui_additional_window(sandwich_license_iface,"icons/32x32/creative_commons.png",arg)
                    if  not result:
                        break
                    webbrowser.open(result)
            if  what == "call":
                arg()
                return

        if  new_charset != None:
            global charset
            if  charset != new_charset:
                global mascot_export_zoom
                global mascot_export_crop
                mascot_export_zoom = 1.0
                mascot_export_crop = None
            charset = new_charset
            global current_recolor
            current_recolor = {}
            global mascot_view_zoom
            mascot_view_zoom = float(open(chsetdirfull+charset+"/zoom").read())
            sandwich_layer_reset()
            sandwich_color_reset()
            sandwich_layer_action("on_start")
            sandwich_color_action("on_start")

    def sandwich_charset_reset():
        pass

    def sandwich_charset_get_state():
        import copy
        state = {}
        global charset
        global current_mascot
        global current_sides
        global current_limits
        global current_recolor
        global current_used_colors
        state["charset"] = charset
        state["current_mascot"] = copy.deepcopy(current_mascot)
        state["current_sides"] = copy.deepcopy(current_sides)
        state["current_limits"] = copy.deepcopy(current_limits)
        state["current_recolor"] = copy.deepcopy(current_recolor)
        state["current_used_colors"] = copy.deepcopy(current_used_colors)
        return state

    def sandwich_charset_set_state(state):
        import copy
        global charset
        charset = state["charset"]

        global mascot_view_zoom
        mascot_view_zoom = float(open(chsetdirfull+charset+"/zoom").read())

        global current_mascot
        global current_sides
        global current_limits
        global current_recolor
        global current_used_colors
        current_mascot = copy.deepcopy(state["current_mascot"])
        current_sides = copy.deepcopy(state["current_sides"])
        current_limits = copy.deepcopy(state["current_limits"])
        current_recolor = copy.deepcopy(state["current_recolor"])
        current_used_colors = copy.deepcopy(state["current_used_colors"])
        fill_mascot_view()

    current_plugin = {}
    current_plugin["id"] = "charsets"
    current_plugin["display_icon"] = "icons/32x32/group.png"
    current_plugin["display_name"] = u"Charsets"
    current_plugin["interface"] = sandwich_charset_iface
    current_plugin["action"] = sandwich_charset_action
    current_plugin["reset"] = sandwich_charset_reset
    current_plugin["get_state"] = sandwich_charset_get_state
    current_plugin["set_state"] = sandwich_charset_set_state
    current_plugin["version"] = "1.2.0"
    current_plugin["version_history"] = [(u"1.0.0",u"Initial release"),(u"1.0.1",u"Added counters for number of layers"),(u"1.1.0",u"Charsets icons for males and females"),(u"1.2.0",[u"Creative Commons licenses screen", u"Added credits info"])]
    current_plugin["priority"] = 120
    current_plugin["is_optional"] = False
    plugin_list += [current_plugin]

