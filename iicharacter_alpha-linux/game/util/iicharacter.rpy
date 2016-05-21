init python:
    def provide_credits_info(chsetdirfull, charset):
        import os
        credits_dir = (chsetdirfull+charset+os.sep+"credits"+os.sep).replace("\\","/")
        link = sys_read_file_line(credits_dir+"link")
        name = sys_read_file_line(credits_dir+"name")
        if  not name:
            return  None, link, "icons/32x32/user.png"
        if  os.path.exists(credits_dir+"icon.png"):
            icon = credits_dir+"icon.png"
        else:
            icons = [
                    "icons/32x32/user.png",
                    "icons/32x32/user_gray.png",
                    "icons/32x32/user_green.png", 
                    "icons/32x32/user_orange.png",
                    "icons/32x32/user_red.png", 
                ]
            icon = icons[ sum([len(name)]+[ord(c) for c in name]) % len(icons) ]
        return name, link, icon
        