init python:
    persistent.Fat_Lady=False
    persistent.Fat_Lady_1 =False
    persistent.Big_belly_boy =False
    persistent.Mad_Man =False
    persistent.Damsel_Distress =False
    persistent.Slow_Girl =False
    persistent.Sadman =False
    

    labs=False
    inv_page = 0 
    check=False
    deflate=10000
    pressure = 0
    needle = 0
    diastolic=120
    systolic=160
    
    death_2=''
    x=0
    persistent.promo = True
    persistent.lang = "en"
    
        
    def press():
        global pressure, needle, deflate, x
        r=120/deflate*0.5
        if pressure >0:
            renpy.hide_screen('gauge')
            pressure -= 0.75*r
            needle -= 1.2*r
            renpy.show_screen('gauge')
        else:
            renpy.hide_screen('gauge')
            pressure=needle=0
            renpy.show_screen('gauge')
        if pressure >= diastolic and pressure < systolic:
            renpy.sound.play('mp3/K2.mp3')
        renpy.restart_interaction()
        return
  
    def ticker():
        global freq
        ui.timer(0.9,press,repeat=True)
    
    overriding_on = None

    class Player:
        def __init__(self, current, music='', press=""):
            if persistent.promo:
                self.life=4
            else:
                self.life=7
            self.current=current
            if music!='':
                self.music=music
        def life_loss(self):
            if self.life >= 1:
                self.life -= 1
                renpy.play('mp3/wrong.mp3', channel='sound')
                if self.music=='':
                    renpy.play(self.music, channel='music')
                renpy.jump(self.current)
            else:
                renpy.jump('death')
    class Item:
        def __init__(self, name, image, description):
            self.name=name
            self.image=image
            self.description=description
    inventoryList=[]
  
               

label start:
    $ freq=renpy.random.randint(60,80)
    $renpy.pause(0)
    scene black
    with Pause(0.1)
    jump splashscreen
    
    return
label splashscreen:
    #python:
    play music 'mp3/George Street Shuffle.mp3'
    
    jump main_menu
    return
    
    
label fail:
    show bont normalw
    
    show text 'Easy! I have to be careful!' with Pause(1.0)
    show text 'Easy! I have to be careful!\nyou have [dr.life] point of life' with Pause(1.0)
    hide bont normalw
    return
    
label death:
    play music 'mp3/bad ending.mp3'
    scene ending with dissolve
    show text '[death_1]'  with Pause(4.5)
    if death_2 != "":
       show text '[death_2]'with Pause(4.5)
    show text '{color=#f00}The patient died{/color}' with Pause(2.5)
    jump splashscreen
    return