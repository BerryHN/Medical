init python:

    def sys_open_folder(folder):
        folder = renpy.fsencode(folder)

        if renpy.macintosh:
            import subprocess
            subprocess.Popen([ "open", folder ])
        else:
            import webbrowser
            webbrowser.open(folder)

    def sys_start_renpy_project_cmd(folder):
        import sys
        cmd = [ sys.executable, "-EOO", sys.argv[0], folder ]
        return [ renpy.fsencode(i) for i in cmd ]

    def sys_start_renpy_project(folder):
        import subprocess
        p = subprocess.Popen(sys_start_renpy_project_cmd(folder))

    def sys_read_file_line(fname):
        import os
        if  not os.path.exists(fname):
            return None
        f = open(fname, "r")
        result = f.readlines()[0]
        f.close()
        if  len(result) == 0:
            return None
        if  result[-1] == "\n":
            return result[:-1]
        return result
