init python:
    import os
    wakaba_temp_dir = config.basedir + os.sep + "temp"

    wakaba_thread_fname = wakaba_temp_dir + os.sep + "thread.html"
    wakaba_board_fname = wakaba_temp_dir + os.sep + "board.html"
    wakaba_thread_fname = wakaba_temp_dir + os.sep + "thread.html"
    wakaba_result_fname = wakaba_temp_dir + os.sep + "result.html"
    wakaba_captch_refresh = True
    wakaba_thread_preview = None
    wakaba_thread_preview_n = 5

    captch = "captch"

    # oh, crap, renpy requires '/'s in filepaths, even on Win32
    wakaba_previewname = wakaba_temp_dir.replace(os.sep,"/") + "/" + "thread%d.png"
    wakaba_postpreviewname = wakaba_temp_dir.replace(os.sep,"/") + "/" + "post%d.png"
    wakaba_captch_fname = wakaba_temp_dir.replace(os.sep,"/") + "/" + "captch.gif"
    wakaba_tempname = wakaba_temp_dir.replace(os.sep,"/") + "/" + "send.png"

    wakaba_boards = {}
    wakaba_boards["iichan.hk"] = {}
    wakaba_boards["iichan.hk"]["display"] = "IIchan.hk"
    wakaba_boards["iichan.hk"]["main"] = "http://iichan.hk/%s/"
    wakaba_boards["iichan.hk"]["thread"] = "http://iichan.hk/%s/res/%d.html"
    wakaba_boards["iichan.hk"]["site"] = "iichan.hk"
    wakaba_boards["iichan.hk"]["post"] = "/cgi-bin/wakaba.pl/%s/"
    wakaba_boards["iichan.hk"]["boards"] = {}
    wakaba_boards["iichan.hk"]["boards"]["b"] = {"name":u"Бред","captch":"http://iichan.hk/cgi-bin/captcha1.pl/%s/?key=res%d"}
    wakaba_boards["iichan.hk"]["boards"]["vn"] = {"name":u"Визуальные новеллы","captch":"http://iichan.hk/cgi-bin/captcha.pl/%s/?key=res%d"}
    wakaba_boards["iichan.hk"]["fields"] = {}
    wakaba_boards["iichan.hk"]["fields"]["field1"] = "nya1"
    wakaba_boards["iichan.hk"]["fields"]["field2"] = "nya2"
    wakaba_boards["iichan.hk"]["fields"]["field3"] = "nya3"
    wakaba_boards["iichan.hk"]["fields"]["field4"] = "nya4"

    if  persistent.wakaba_current_site == None:
        persistent.wakaba_current_site = "iichan.hk"
    if  persistent.wakaba_current_board == None:
        persistent.wakaba_current_board = "b"
    if  persistent.wakaba_current_thread == None:
        pass
    if  persistent.wakaba_password == None:
        persistent.wakaba_password = "xxx"

    def wakaba_post_field_name(name):
        if  not name in wakaba_boards[persistent.wakaba_current_site]["fields"]:
            return name
        else:
            return wakaba_boards[persistent.wakaba_current_site]["fields"][name]

    def wakaba_getcaptch(board,id):
        import urllib
        site = urllib.urlopen(wakaba_boards[persistent.wakaba_current_site]["boards"][persistent.wakaba_current_board]["captch"]%(board,id))
        f = open(wakaba_captch_fname, 'wb')
        f.write(site.read())
        f.close()
        site.close()

    def wakaba_get_threads(board):
        import urllib
        site = urllib.urlopen(wakaba_boards[persistent.wakaba_current_site]["main"]%(board))
        f = open(wakaba_board_fname, 'wb')
        page = site.read()
        site.close()
        f.write(page)
        f.close()
        return [ wakaba_thread_to_label(th) for th in wakaba_threads_parse(page) ]
    
    def wakaba_get_thread(board,thread):
        import urllib
        site = urllib.urlopen(wakaba_boards[persistent.wakaba_current_site]["thread"]%(board,thread))
        f = open(wakaba_thread_fname, 'wb')
        page = site.read()
        site.close()
        f.write(page)
        f.close()
        return [ wakaba_thread_to_label(th) for th in wakaba_thread_parse(page) ]

    i = 0    
    def wakaba_renpy_styles(text):
        while wakaba_regexp_links.match(text):
            match = wakaba_regexp_links.match(text)
            url = "http://" + wakaba_boards[persistent.wakaba_current_site]["site"] +  match.group(2) if match.group(2)[0] == "/" else match.group(2)
            text = match.group(1) + "{a="+url+"}"+match.group(3)+"{/a}"+match.group(4)
        while wakaba_regexp_quote.match(text):
            match = wakaba_regexp_quote.match(text)
            text = match.group(1) + "{color=#789922}"+match.group(2)+"{/color}\n"+match.group(3)
        while wakaba_regexp_spoiler.match(text):
            match = wakaba_regexp_spoiler.match(text)
            text = match.group(1) + "{color=#998877}"+match.group(2)+"{/color}\n"+match.group(3)
        text = text.replace("<b>","{b}")
        text = text.replace("</b>","{/b}")
        text = text.replace("<strong>","{b}")
        text = text.replace("</strong>","{/b}")
        text = text.replace("<em>","{i}")
        text = text.replace("</em>","{/i}")
        text = text.replace("<i>","{i}")
        text = text.replace("</i>","{/i}")
        text = text.replace("<p>","")
        text = text.replace("</p>","\n\n")
        text = text.replace("<br />","\n")
        text = text.replace("<pre>","")
        text = text.replace("</pre>","")
        text = text.replace("<code>","{font=lucon.ttf}")
        text = text.replace("</code>","{/font}")
        text = text.replace("&#39;","'")
        text = text.replace("&#44;",",")
        text = text.replace("&gt;",">")
        text = text.replace("&lt;","<")
        text = text.replace("&quot;","\"")
        text = text.replace("	"," ")
        return text
    
    import re
    wakaba_regexp_short = re.compile('^.*?<img src="([^"]*)"[^>]*/>.*<a name="([0-9]*)"></a>.*<label>.*<span class="filetitle">([^<]*)</span>.*<span class="postername">(.*?)</span>\W*(.*?) *</label>.*?<blockquote> *(.*?) *</blockquote> ', re.MULTILINE|re.DOTALL)
    wakaba_regexp2_short = re.compile('^.*<a name="([0-9]*)"></a>.*<label>.*<span class="replytitle">([^<]*)</span>.*<span class="commentpostername">(.*?)</span>\W*(.*?) *</label>.*?<img src="([^"]*)"[^>]*/>.*?<blockquote> *(.*?) *</blockquote> ', re.MULTILINE|re.DOTALL)
    wakaba_regexp2noimg_short = re.compile('^.*<a name="([0-9]*)"></a>.*<label>.*<span class="replytitle">([^<]*)</span>.*<span class="commentpostername">(.*?)</span>\W*(.*?) *</label>.*?<blockquote> *(.*?) *</blockquote> ', re.MULTILINE|re.DOTALL)
    wakaba_regexp_links = re.compile('(.*)<a href="([^"]*)"[^>]*>([^<]*)</a>(.*)',re.S)
    wakaba_regexp_quote = re.compile('(.*)<blockquote class="unkfunc">((?:(?!</blockquote>).)*)</blockquote>(.*)',re.S)
    wakaba_regexp_spoiler = re.compile('(.*)<span class="spoiler">((?:(?!</span>).)*?)</span>(.*)',re.S)

    def wakaba_threads_parse(page):
        threads = page.split('<br clear="left" /><hr />')
        result = []
        for t in threads:
            if  wakaba_regexp_short.search(t):
                match = wakaba_regexp_short.match(t)
                result += [[
                        int(match.group(2)),
                        unicode(match.group(1),"utf-8"),
                        unicode(wakaba_renpy_styles(match.group(3)),"utf-8"),
                        unicode(wakaba_renpy_styles(match.group(4)),"utf-8"),
                        unicode(match.group(5),"utf-8"),
                        unicode(wakaba_renpy_styles(match.group(6)),"utf-8"),
                    ]]
                continue
        return result

    def wakaba_thread_parse(page):
        posts = page.split('<table><tbody>')
        result = []
        if  len(posts) < 2:
            return result
        if  wakaba_regexp_short.search(posts[1]):
            match = wakaba_regexp_short.match(posts[1])
            result += [[
                    int(match.group(2)),
                    unicode(match.group(1),"utf-8"),
                    unicode(wakaba_renpy_styles(match.group(3)),"utf-8"),
                    unicode(wakaba_renpy_styles(match.group(4)),"utf-8"),
                    unicode(match.group(5),"utf-8"),
                    unicode(wakaba_renpy_styles(match.group(6)),"utf-8"),
                ]]
        if  len(posts) < 3:
            return result
        for t in posts[2:]:
            if  wakaba_regexp2_short.search(t):
                match = wakaba_regexp2_short.match(t)
                result += [[
                        int(match.group(1)),
                        unicode(match.group(5),"utf-8"),
                        unicode(wakaba_renpy_styles(match.group(2)),"utf-8"),
                        unicode(wakaba_renpy_styles(match.group(3)),"utf-8"),
                        unicode(match.group(4),"utf-8"),
                        unicode(wakaba_renpy_styles(match.group(6)),"utf-8"),
                    ]]
                continue
            if  wakaba_regexp2noimg_short.search(t):
                match = wakaba_regexp2noimg_short.match(t)
                result += [[
                        int(match.group(1)),
                        None,
                        unicode(wakaba_renpy_styles(match.group(2)),"utf-8"),
                        unicode(wakaba_renpy_styles(match.group(3)),"utf-8"),
                        unicode(match.group(4),"utf-8"),
                        unicode(wakaba_renpy_styles(match.group(5)),"utf-8"),
                    ]]
                continue
        return result

    def wakaba_thread_to_label(th):
        return th[0],"{color=#cc1105}{b}%s{/b}{/color} {color=#117743}%s{/color} %s #%d"%(th[2],th[3],th[4],th[0]),th[1],th[5]
        

    def wakaba_captch_input():
        global captch
        result = ui_input_window(u"Input captcha: {image="+wakaba_captch_fname+"}",captch)
        if  result != None:
            captch = result
        
    def wakaba_fail_captch(board,id):
        fields= [
                    (wakaba_post_field_name("task")    ,"post"),
                    (wakaba_post_field_name("parent")  ,"%d"%(id)),
                    (wakaba_post_field_name("field1")  ,""),
                    (wakaba_post_field_name("field2")  ,""),
                    (wakaba_post_field_name("field3")  ,""),
                    (wakaba_post_field_name("field4")  ,"iwantanothercaptch"),
                    (wakaba_post_field_name("captcha") ,"iwantanothercaptch"),
                    (wakaba_post_field_name("password"),persistent.wakaba_password)
                ]
        files = []
        post_multipart(wakaba_boards[persistent.wakaba_current_site]["site"],wakaba_boards[persistent.wakaba_current_site]["post"]%board,fields,files)
        
    def wakaba_send_picture(board,id,captch,text):
        saveload_export_static(wakaba_temp_dir, wakaba_tempname)
        fields= [
                    (wakaba_post_field_name("task")    ,"post"),
                    (wakaba_post_field_name("parent")  ,"%d"%(id)),
                    (wakaba_post_field_name("field1")  ,""),
                    (wakaba_post_field_name("field2")  ,""),
                    (wakaba_post_field_name("field3")  ,mascot_name.encode("utf-8")),
                    (wakaba_post_field_name("field4")  ,text.encode("utf-8")),
                    (wakaba_post_field_name("captcha") ,captch.encode("utf-8")),
                    (wakaba_post_field_name("password"),persistent.wakaba_password)
                ]
        data = open(wakaba_tempname, mode='rb').read()
        files = [("file","iicharacter.png",data)]
        res = post_multipart(wakaba_boards[persistent.wakaba_current_site]["site"],wakaba_boards[persistent.wakaba_current_site]["post"]%board,fields,files)
        f = open(wakaba_result_fname, 'wb')
        f.write(res)
        f.close()

    def wakaba_previewthread(wakabasite,board,thread):
        import urllib
        i = 0
        global wakaba_thread_preview, wakaba_boards
        if  not wakaba_thread_preview:
            try:
                posts = wakaba_get_thread(board,thread)
                if  len(posts)>wakaba_thread_preview_n:
                    posts = posts[:1] + [(None,u"",None,u"... %d posts skipped ...\n"%(len(posts)-wakaba_thread_preview_n))] + posts[1-wakaba_thread_preview_n:]
            except:
                posts = []
        else:
            posts = wakaba_thread_preview

        if  len(posts) == 0:
            ui_text(u"Error connecting to http://"+wakaba_boards[persistent.wakaba_current_site]["thread"]%(persistent.wakaba_current_board,persistent.wakaba_current_thread))

        for id, labeltext, imgurl, text in posts:
            ui.frame(style="button")
            ui.vbox()
            if  id:
                ui_imagebutton_with_text("icons/32x32/source_code.png", ["plugin", ("reply",">>%d\n"%id)], labeltext)
            ui.hbox()
            ui.vbox()
            if  imgurl != None:
                if  not wakaba_thread_preview:
                    site = urllib.urlopen("http://"+wakaba_boards[wakabasite]["site"]+imgurl)
                    f = open(wakaba_postpreviewname%i, 'wb')
                    page = site.read()
                    site.close()
                    f.write(page)
                    f.close()
                ui.image(wakaba_postpreviewname%i)
                i += 1
            ui_line()
            ui.close()
            ui_text(text)
            ui.close()
            ui.close()
        wakaba_thread_preview = posts
        
    def wakaba_iface(options=None):
        ui.vbox()
        ui_imagebutton_with_text("icons/32x32/exclamation.png", None, u"This module is experimental and does NOT use threading for network interactions. This could cause serious time lags between operations.")
        ui_header(u"Wakaba imageboard selection:")
        ui_imagebutton_with_text("icons/32x32/world.png", ["plugin","select_site"], wakaba_boards[persistent.wakaba_current_site]["display"])
        ui_imagebutton_with_text("icons/32x32/wakaba.png", ["plugin","select_board"],wakaba_boards[persistent.wakaba_current_site]["boards"][persistent.wakaba_current_board]["name"])
        if  persistent.wakaba_current_thread == None:
            ui_imagebutton_with_text("icons/32x32/legend.png", ["plugin", "select_thread"], u"Select thread")
        else:
            ui_imagebutton_with_text("icons/32x32/legend.png", ["plugin", "select_thread"], u"#%d"%persistent.wakaba_current_thread)
            ui_imagebutton_with_text("icons/32x32/control_repeat_blue.png", ["plugin", "reset_thread"], u"Reload thread")
            ui_imagebutton_with_text("icons/32x32/www_page.png", ["plugin", "see_thread"], u"Open thread in browser")
            ui_line()

            ui_header(u"Wakaba thread preview:")
            wakaba_previewthread(persistent.wakaba_current_site, persistent.wakaba_current_board, persistent.wakaba_current_thread)

        if  persistent.wakaba_current_thread != None:
            ui_header(u"Wakaba posting:")
            if  wakaba_boards[persistent.wakaba_current_site]["boards"][persistent.wakaba_current_board]["captch"] != None:
                ui.hbox()
                ui_input_imagebutton_with_text("icons/32x32/textfield_key.png","captch",captch,options,u"Input captcha:")
                try:
                    wakaba_success = False
                    global wakaba_captch_refresh
                    if  wakaba_captch_refresh:
                        wakaba_getcaptch(persistent.wakaba_current_board,persistent.wakaba_current_thread)
                    wakaba_captch_refresh = True
                    wakaba_success = True
                    ui.image(wakaba_captch_fname)
                except:
                    ui_text(u"Error connecting to http://"+wakaba_boards[persistent.wakaba_current_site]["site"])
                ui.close()
                ui_imagebutton_with_text("icons/32x32/textfield_shuffle.png", ["plugin", "reset_captch"], u"Get another captcha")
            ui_imagebutton_with_text("icons/32x32/world_go.png", ["plugin", "send_picture"], u"Post to wakaba thread (using character description)")
            ui_imagebutton_with_text("icons/32x32/world_edit.png", ["plugin", ("reply","")], u"Post to wakaba thread (input text message)")
        ui.close()

    def wakaba_select_site_iface(options):
        ui.vbox()
        ui.label(u"Select site:")
        for site in wakaba_boards:
            ui_imagebutton_with_text("icons/32x32/world.png", ["return", site], wakaba_boards[site]["display"])
        ui.close()

    def wakaba_select_board_iface(options):
        ui.vbox()
        ui.label(u"Select board:")
        for board in wakaba_boards[persistent.wakaba_current_site]["boards"]:
            ui_imagebutton_with_text("icons/32x32/wakaba.png", ["return", board], wakaba_boards[persistent.wakaba_current_site]["boards"][board]["name"])
        ui.close()

    def wakaba_select_thread_iface(options):
        ui.vbox()
        ui.label(u"Select thread:")
        i = 0
        for id, labeltext, imgurl, text in wakaba_get_threads(persistent.wakaba_current_board):
            ui_imagebutton_with_text("icons/32x32/source_code.png", ["return", id], labeltext)
            ui.hbox()
            ui.vbox()
            try:
                import urllib
                site = urllib.urlopen("http://"+wakaba_boards[persistent.wakaba_current_site]["site"]+imgurl)
                f = open(wakaba_previewname%i, 'wb')
                page = site.read()
                site.close()
                f.write(page)
                f.close()
                ui.image(wakaba_previewname%i)
                i += 1
            except:
                pass
            ui_line()
            ui.close()
            ui_text(text)
            ui.close()
        ui.close()

    def wakaba_action(button):
        global wakaba_thread_preview
        global wakaba_captch_refresh
        global captch
        if  button == ("input","captch"):
            result = ui_input_window("captch",captch,wakaba_iface)
            if  result!= None: 
                captch = result
            wakaba_captch_refresh = False
        if  button == "reset_captch":
            wakaba_fail_captch(persistent.wakaba_current_board,persistent.wakaba_current_thread)
        if  button == "reset_thread":
            wakaba_thread_preview = None
        if  button == "send_picture":
            wakaba_send_picture(persistent.wakaba_current_board,persistent.wakaba_current_thread,captch,additional_info)
            wakaba_thread_preview = None
        if  isinstance(button,tuple) and button[0] == "reply":
            text = ui_input_window(u"Your reply to wakaba thread #%d"%persistent.wakaba_current_thread,button[1])
            if  text:
                wakaba_send_picture(persistent.wakaba_current_board,persistent.wakaba_current_thread,captch,text)
                wakaba_thread_preview = None
        if  button == "see_thread":
            import webbrowser
            webbrowser.open(wakaba_boards[persistent.wakaba_current_site]["thread"]%(persistent.wakaba_current_board,persistent.wakaba_current_thread))
        if  button == "select_site":
            current_site_old = persistent.wakaba_current_site
            result = ui_additional_window(wakaba_select_site_iface,"icons/32x32/www_page.png")
            if  result != None:
                persistent.wakaba_current_site = result
                result = ui_additional_window(wakaba_select_board_iface,"icons/32x32/www_page.png")
                if  result != None:
                    persistent.wakaba_current_board = result
                    persistent.wakaba_current_thread = None
                else:
                    persistent.wakaba_current_site = current_site_old
            wakaba_thread_preview = None
        if  button == "select_board":
            result = ui_additional_window(wakaba_select_board_iface,"icons/32x32/www_page.png")
            if  result != None:
                persistent.wakaba_current_board = result
                persistent.wakaba_current_thread = None
            wakaba_thread_preview = None
        if  button == "select_thread":
            result = ui_additional_window(wakaba_select_thread_iface,"icons/32x32/www_page.png")
            if  result != None:
                persistent.wakaba_current_thread = result
            wakaba_thread_preview = None

    def wakaba_reset():
        pass

    def wakaba_get_state():
        return ''

    def wakaba_set_state(state):
        pass

    current_plugin = {}
    current_plugin["id"] = "wakaba"
    current_plugin["display_icon"] = "icons/32x32/wakaba.png"
    current_plugin["display_name"] = u"Wakaba"
    current_plugin["interface"] = wakaba_iface
    current_plugin["action"] = wakaba_action
    current_plugin["reset"] = wakaba_reset
    current_plugin["get_state"] = wakaba_get_state
    current_plugin["set_state"] = wakaba_set_state
    current_plugin["version"] = "0.9.0"
    current_plugin["version_history"] = [(u"0.8.0",u"Initial release"),(u"0.8.1",u"IIchan.hk support"),(u"0.9.0",u"Simple thread preview")]
    current_plugin["priority"] = 20
    current_plugin["is_optional"] = True
    plugin_list += [current_plugin]
