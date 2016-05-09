label fat2:
    if check==False and persistent.checkpoint_8 != None:
        "Where do you want to start?"
        menu:
            "From the beginning of the chapter":
                $ dr=Player('fat2')
                $ check=True
                jump fat2
            "From automatic checkpoint_":
                $ renpy.jump(persistent.checkpoint_8)
    else:
        $ dr=Player('fat2')
    $persistent.Slow_Girl=True
    return
