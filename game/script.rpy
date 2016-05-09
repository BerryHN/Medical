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
            renpy.sound.play('K2.mp3')
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
                renpy.play('wrong.mp3', channel='sound')
                if self.music=='':
                    renpy.play(self.music, channel='music')
                renpy.jump(self.current)
            else:
                renpy.jump('death')
  
               
#Image Background
image city = "first bg.jpg"
image w = "ward.jpeg"
image garage ="garage.png"
image hospital='images/Uncle Mugen/hospital.jpg'
image ending = 'end.jpeg'
image happy dev ="happy dev.jpg"
image sad dev = 'sad dev.jpg'
image er_img = "ER_medium.jpg"
image football=im.Scale('soccer_field.jpg',800,600)

#Image color
image black= "#000000"

#Characters
image bont normal = "images/Bont normal.png"
image layzee = 'layzee0001.png'
image bont normalw = "oslor0001t.png"
image bolt ='bolt closed0001.png'
image bolt_f ='bolt open0001.png'
image Alice = 'Alice_normal0001.png'
image Alice angry = 'Alice_angry.png'

#Medical Images
image eye_n ='eye1.jpg'
image eye_enf ='eye2.jpg'
image eye_cured ='eye3.jpg'
image selected_LE ='Left selected.jpg'
image blood_back='Blood pressure back.png'
image pointer='needle.png'


#Characters
define u1 = Character('?????', color="#0000ff")
define u2 = Character('?????', color="#00ff00")
define u3 = Character('?????', color="#00ffa5")
define u4 = Character('?????', color="#12ffa5")
define l = Character("Lieutenant", color="#0000ff")
define s = Character("Sergeant", color="#00ff00")
define Layzee = Character("Dr Layzee", color="#de64da")
define InnerL= Character("Dr. Layzee Inner",color="#5f9ea0")
define Bont = Character("Dr. John Bont", color="#ffffff")
define Inner = Character("Dr. John Bont -thoughts-", color="#999666")
define Alice = Character("Ms. Alice", color="#00ffa5")
define Layzee = Character("Dr. Lazy", color="#aaff55")
define Bolt = Character("Mr. Bolt", color="#ffffff")
define Bad_m = Character("Mr. Bad", color="#ffffff")
define Bad_f = Character("Mrs. Bad", color="#ffffff")
define vlad = Character("Dr. Vladd", color="#ffffff")
define manolo = Character("Sr. Manolo", color="#ffffff")
define Hedley = Character("Dr. Hedley Quintana", color="#ffffff")
define Gloria = Character ('Mrs. Gloria', color="#ffff00")
define FatLady = Character('Mrs. Wahlee', color='#f0e68c')
define mom = Character("Mrs. Sweeny", color="#ff0000")
transform rotatelong:
    xpos 0.5
    ypos 0.3
    xalign 0.5
    yalign 0.5
    rotate (needle)

transform x:
    xpos 0.5
    ypos 0.3
    xalign 0.5
    yalign 0.5
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
    play music 'bad ending.mp3'
    scene ending with dissolve
    show text '[death_1]'  with Pause(4.5)
    if death_2 != "":
       show text '[death_2]'with Pause(4.5)
    show text '{color=#f00}The patient died{/color}' with Pause(2.5)
    jump splashscreen
    return




