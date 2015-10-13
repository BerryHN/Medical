init python:
   #s import random from random
  #  import renpy.store as store
 #   import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
   # from operator import attrgetter # we need this for sorting items
    labs=False
    inv_page = 0 
    #showitems = True
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
        
   # def overriding_overlay():
        #if not overriding_on:
        #    return
       # ui.keymap(mousedown_1=ui.returns(None))
      #  ui.keymap(mouseup_1=ui.returns(None))
     #   ui.keymap(I=ui.returns('False'))
        

    #config.overlay_functions.append(overriding_overlay) 

    class Player:
        def __init__(self, current, music=''):
            self.life=7
            self.current=current
            if music!='':
                self.music=music
        def life_loss(self):
            if self.life >= 1:
                self.life -= 1
                renpy.play('wrong.mp3', channel='sound')
                renpy.jump(self.current)
                if self.sound!='':
                    renpy.play(self.music, channel='music')
            else:
                renpy.jump('death')
    
   # class Item(store.object):
    #    def __init__(self, name, description, image, submitted, symptom=True,  imageneology=False):
     #       self.name         = name
      #      self.description  = description
#            self.image        = image
 #           self.symptom      = symptom
  #          self.submitted    = submitted
   #         self.imageneology = imageneology
    #    def imageneology(self):
     #       if self.imageneology:
      #          renpy.show_screen(self.imageneology)
            
               
#Images
image city = "first bg.jpg"
image w = "ward.jpeg"
image garage ="garage.png"
image black= "#000000"
image bont normal = "images/Bont normal.png"
image layzee = 'layzee0001.png'
image bont normalw = "oslor0001t.png"
image bolt ='bolt closed0001.png'
image bolt_f ='bolt open0001.png'
image Alice = 'Alice_normal0001.png'
image Alice angry = 'Alice_angry.png'
image er_img = "ER_medium.jpg"
image ending = 'end.jpeg'
image eye_n ='eye1.jpg'
image eye_enf ='eye2.jpg'
image eye_cured ='eye3.jpg'
image selected_LE ='Left selected.jpg'
image blood_back='Blood pressure back.png'
image pointer='needle.png'
image happy dev ="happy dev.jpg"
image sad dev = 'sad dev.jpg'
image hospital='images/Uncle Mugen/hospital.jpg'
image football=im.Scale('soccer_field.jpg',800,600)
#Characters
define u1 = Character('?????', color="#0000ff")
define u2 = Character('?????', color="#00ff00")
define u3 = Character('?????', color="#00ffa5")
define u4 = Character('?????', color="#12ffa5")
define l = Character("Liutenant", color="#0000ff")
define s = Character("Sargent", color="#00ff00")
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
    play music 'mp3/Penumbra.mp3'
    scene ending with dissolve
    show text '[death_1]'  with Pause(4.5)
    if death_2 != "":
       show text '[death_2]'with Pause(4.5)
    show text '{color=#f00}The patient died{/color}' with Pause(2.5)
    jump splashscreen
    return

label hangman:
    $ chart= []
    #show screen chart_button
    stop music
    $ death_1='{color=#fff}So Mr. Bolt refused your help.{/color}'
    $ death_2= '{color=#fff}6 hours later, you learned that Mr. Bolt jumped thru the window on the 9th floor of the ward.{/color}'
    scene black with dissolve
    if check==False and persistent.checkpoint_1 != None:
        "Where do you want to start?"
        menu:
            "From the beginning of the chapter":
                $ dr=Player('hangman')
                $ check=True
                jump hangman
            "From the an earlier saved game":
                $ dr=Player(persistent.checkpoint_1)
                $ renpy.jump(persistent.checkpoint_1)
    else:
        $ dr=Player('hangman')
                
    
    #call screen aff_screen
    #play music "W.ogg"
    show text 'WARNING! THIS CHAPTER CONTAINS STRONG IMAGES'with Pause(2.5)
    show text 'This was a real case!'with Pause(2.5)
    stop music
    
    show text 'Case 1\nThe Sadman' with Pause(2.5)
    show text "Location: ?????\nDate: ????" with Pause(3.5)
    scene black with dissolve
    scene city 
   
    
    play music 'Grillo.mp3'
    u1 "Sir, do you think I’m got get a raise?"
    u2 "I am not sure, you need more experience"
    u1 "what do you mean?"
    u2 "You are not attentive, take a look at Mr. Bolt garage, there is something suspicious and you have not noticed it sergeant!"
    u2  "Sorry, let’s hurry Lieutenant" 
    scene city
    play sound 'gun.mp3'
    l "That sound suspicious, let's take a look, Sargent... be quiet!"
    l "Shhh… let’s take a look!"
    
    stop music
    play music 'su.mp3'
    scene black
    s "Freez…. Lieutenant look!"
    stop music
    play music 'action.mp3'
    l "Hurry!"
    l "Hurry!"
    scene garage
    l "Cut the belt and seize him!"
    s "Done! sir!"
    s "Will we arrest him?"
    l "Don’t be silly, that’s the reason that you’ve never get a raise!"
    l "You must go together with him in the back!"
    scene black
    l "I’ve already called ER!"
    l "They have a new patient"
    stop music
    play music "amb.mp3"
    show text "General hospital, Psychiatry Ward" with Pause(2.5)
    scene w
    show bont normal
    u3 "Miss Alice, a week here and I have nothing to do"
    hide bont normal
    show Alice
    Alice "Tell me your orders Dr. Bont"
    hide Alice
    show bont normal
    Bont "Orders?"
    hide bont normal
    show Alice
    Alice "We have a new patient!"
    hide Alice
    show bont normal
    Bont "A new patient?"
    hide bont normal
    show Alice
    Alice "Yes this is the chart"
    hide Alice
    show bont normal
    Bont "What?"
    hide Alice
    show bont normal
    Bont "Let me read that..."
    hide w
    scene black 
    with dissolve
    
    show text 'ER chart' with Pause(2.5)
    show text 'ER chart "Anamnesis"'with Pause (2.5)
    show text 'ER chart "Anamnesis"\nInform by Dr. Layzee'with Pause (2.5)
    scene er_img
    play music "conga.mp3"
    l "We saw Mr. Agnus Bolt a 54 years old"
    l "Trying to kill him hanging with his belt"
    l "My subordinate and I took action"
    l "We seize him, called ER and we proces… I mean submit you for medical  treatment"
    scene black
    show text 'ER chart "Physical examination"' with Pause(2.5)
    show text 'ER chart "Physical examination"\n"Inform by Dr. Layzee"' with Pause(2.5)
    ""
    Inner "Grr! Dr Layzee… I hate that woman!"
    scene er_img
    show layzee at  right
    Layzee "Male 54 years old"
    Layzee "Deeply depressed"
    Inner "Interesting"
    Layzee "Systolic blood pressure 120"
    Inner "That’s normal"
    Layzee "Diastolic blood pressure 80"
    Inner "That’s normal"
    Layzee "Temperature 37.0 C"
    Inner "That’s normal"
    Layzee "Cardiac frequency 85 beats per minute"
    Inner "Both of them are also normal"
    Layzee "Cardiac frequency 20 breaths per minutes"
    Inner "Both of them are also normal"
    Layzee "No remarkable signs at physical examination"
    Layzee "Workup diagnosis: Failed Suicide attempt"
    hide layzee
    stop music
    play music 'amb.mp3'
    
    label hang_q1:
        show screen health_bar
        scene w
        show bont normal
        'What happened?'
        $ dr.current='hang_q1'
        $ dr.music='amb.mp3'
        menu:
            "Mr Bolt had a heart attack":
                $ dr.life_loss()
            "Mr Bolt stole his own garage":
                $ dr.life_loss()
            "Mr Bolt tried to kill himself by hanging":
                jump hang_q2
    label hang_q2:
        scene w
        show bont normal
        $ dr.current = 'hang_q2'
        Inner "Well this a psychiatric ward, after all"
        Inner "A patient with a failed suicide diagnosis get hospitalized here!"
        Inner "The succesfull ones"
        play music 'bad ending.mp3'
        Inner "..."
        stop music
        play music dr.music
        Inner "Let's continue..."
        'When it happened?'
        menu:
            "At 4:00":
                jump hang_q3
            "At noon":
                $ dr.life_loss()
            "At 16:00":
                $ dr.life_loss()
    label hang_q3:
        scene w
        show bont normal
        $ dr.current = 'hang_q3'
        Inner "Disease never sleeps!"
        Inner "The war never ends..."
        Inner "But we are human beings... and sleep"
        Inner "sleep! sleep!"
        Inner "My precious!"
        "What was the most important finding in ER physical examination?"
        menu:
            "He looked sad":
                jump hang_q4
            "He looked pale":
                $ dr.life_loss()
            "He had fever":
                $ dr.life_loss()
            "He had problems breath":
                $ dr.life_loss()
    label hang_q4:
        scene w
        show bont normal
        $ dr.current = 'hang_q4'
        "Given the current data why is Mr. Bolt depressed?"
        menu:
            "Financial problems":
                $ dr.life_loss()
            "He has a secret mistress":
                $ dr.life_loss()
            "There is no enough data to raise conclusions":
                jump hang_q5
            "He had an incurable disease":
                $ dr.life_loss()
            "He caught her wife cheating":
                $ dr.life_loss()
    label hang_q5:
        scene w
        show bont normal
        $ dr.current = 'hang_q5'
        "How can I learn further about Mr. Bolt problems?"
        menu:
            "Taking a chest X-ray":
                $ dr.life_loss()
            "Taking a blood sample":
                $ dr.life_loss()
            "Taking a urine sample":
                $ dr.life_loss()
            "Asking Mr. Bolt himself":
                jump hang_q6
    label hang_q6:
        scene w
        show bont normal
        $ dr.current = 'hang_q6'
        Bont "It seems that as usual, we need a long talk with Mr. Bolt, don't you think so Alice?" 
        hide bont normal
        show Alice
        Alice "The patient is ready, what are your orders?" 
        hide Alice
        show bont normal
        Bont "No Alice, I need to speak with patient first... no injection needed (c)" 
        Bolt "..."
    label hang_q7:
        scene w
        show bont normal
        $ dr.current = 'hang_q7'
        "How can we follow?"
        hide bont normal
        show bolt
        menu:
            "Good morning Mr. Bolt, how can I help you?":
                jump hang_q8
            "GOOD MORNING!!!!":
                $ dr.life_loss()
            "What's going on with you? Maybe I can help... give me shot":
                jump hang_q8a
    label hang_q8a:
        scene w
        hide bont normal
        hide bolt
        show Alice
        Alice "Have you requested a shot"
        show bont normal
        hide Alice
        Bont "No! get back to your business, Alice"
        jump hang_q8
    label hang_q8:
        $ dr.current = 'hang_q8'
        scene w
        show bolt
        Bolt "I can see your kind intentions, but I have a problem you cannot solve" 
        hide bolt
        show bont normal
        Bont "What's your problem?" 
        show bolt
        hide bont normal
        Bolt "My garage is having normal clients as usual"
        Bolt "You know, the city is quite small" 
        Bolt "My employees are young and require guidance" 
        Bolt "But I don't like they take care of me" 
        Bolt "I am too old..." 
        hide bolt
        show bont normal
        $ question_1 = "Which of the following statements seems to contradict each other? and they may point out Mr. Bolt’s problem?"
        $ correct_a=False
        $ correct_b=False
        label menu_1:
            scene w
            show bont normal
            "[question_1]"
            menu:
                "My garage is having normal clients as usual":
                    if correct_a or correct_b:
                        $ dr.life_loss()
                    else:
                        jump test_1
                "You know, the city is quite small":
                    if correct_a or correct_b:
                        $ dr.life_loss()
                    else:
                        jump test_1
                "My employees are young and require guidance":
                    $ correct_a=True
                    jump test_1
                "But I don't like they take care of me":
                    $ correct_b=True
                    jump test_1
    label test_1:
        if correct_a and correct_b:
            $ dr.current='hang_q9'
            jump hang_q9
        else:
            $ question_1 ="You need to select another statement"
            jump menu_1
    label hang_q9:
        $ dr.current='hang_q9'
        scene w
        show bont normal
        Bont "So it means that you are old and experience person"
        Bont "It doesn’t make sense to me that your employees require guidance" 
        Bont 'And they have to "take care" of you'
        hide bont normal
        show bolt
        Bolt "Because I am too old..."
        Bolt "I am not able to identify the tools and the car parts"
        hide bolt
        show bont normal
        Bont "That’s sounds horrible… but…"
        hide bont normal
        show bolt
        Bolt "What?"
        hide bolt
        show bont normal
        Bont 'Why are you not able to do such do such "trivial" tasks'
        hide bont normal
        show bolt
        Bolt "Because, I cannot see"
        hide bont normal
        show bolt
        "Given the current information what part of the body is urgent to examine?"
        hide bolt
        menu:
            "His left arm":
                $ dr.life_loss()
            "A detailed psychiatric inventory":
                $ dr.life_loss()
            "His eyes":
                jump hang_q10
            "His tongue":
                $ dr.life_loss()

    
    
    label hang_q10:
        $ dr.current='hang_q10'
        $ result = ''
        if persistent.checkpoint_1==None:
            "Do you want to save your current progress?"
            menu:
                "Yes":
                    $ persistent.checkpoint_1 = 'hang_q10'
                "No":
                    pass
        scene w
        show bont normal
        Inner "Indeed I have to look as his eyes"
        Inner "It seems a very complicated situation"
        Inner "Let's take a look of his left eye"
        hide bont normal
        "Click in the area causing the visual loss"
        $ result_LE = renpy.imagemap('pterigion-3.jpg', 'pterigion-3.jpg', 
            [(291,235,343,290, 'correct'),
            (0,0,291,235,'a'),
            (0,235,291,290,'b'),
            (0,800,291,290,'c'),
            (291,0,343,235,'d'),
            (291,290,343,800,'e'),
            (343,0,800,290,'f'),
            (343,235,800,290,'g'),
            (343,235,800,600,'h')])
      
        if result_LE == 'correct':
            jump hang_q11
        else:
            $dr.life_loss()
        $ dr.current='hang_q11'
    label hang_q11:
        scene selected_LE
        show bont normal at right
        Inner "So it means that Mr Bolt is cannot see in his left eye"
        Inner "So it means that Mr Bolt is cannot see in his left eye"
        Inner "But, what's going on in the other eye?"
        "Click in the area causing the visual loss"
        hide bont normal
        $ result_RE = renpy.imagemap('R_eye.png', 'R_eye.png', 
            [(441,220,511,303, 'correct'),
            (0,0,441,220,'a'),
            (0,220,441,302,'b'),
            (0,800,441,302,'c'),
            (441,0,511,220,'d'),
            (441,302,511,800,'e'),
            (511,0,800,302,'f'),
            (511,220,800,302,'g'),
            (511,220,800,600,'h')])
        if result_RE == 'correct':
            jump hang_q12
        else:
            $dr.life_loss()
    label hang_q12:
        $ dr.current='hang_q12'
        $ dr.music = 'conga.mp3'
        scene w
        show bont normal
        Inner "So this poor fella is indeed blind!"
        Bont "Alice! Quick!"
        show Alice
        hide bont normal
        Alice "Gimme your orders, Dr. Bont!"
        hide Alice
        show bont normal
        Bont "Could you give the form BA-27F"
        show Alice
        hide bont normal
        Alice "What kind of order is that?"
        Alice "The patient has just been admitted due to suicide attempt!"
        Alice "Do you know what does the form does?"
        hide Alice
        show bont normal
        Bont "I am ordering it! I know what it does!"
        'What do you think the form BA-27F does?'
        hide bont normal
        menu:
            "Discharge the patient":
                jump hang_q13
            "Request X-Rays":
                $dr.life_loss()
            "Request urgent consult to eye specialist":
#                python:
                if "eyes_consult" in vars():
                    Inner "Doing an eye specialist consult makes no sense!"
                    $dr.life_loss()
                else:
                    Inner "Indeed, he need an eye specialist"
                    Inner "However, he there is NO hurry to fix his problem"
                    Inner "However, he will not get worse in short lapse of time"
                    Inner "There is no need for an \"urgent\" consultation!"
                    $ eyes_consult = True
                    $renpy.jump(dr.current)
                    
    label hang_q13:
        $ dr.current='hang_q13'
        scene w
        hide Alice
        show bont normal
        Bont "This ward has nothing to offer to this patient"
        show Alice
        hide bont normal
        Alice "I cannot obey such order"
        Alice "We are responsible for his safety"
        Alice "I can be sued if he tries to kill himself"
        hide Alice
        show bont normal
        Bont "He cannot kill himself if he listen to me first"
        Bont "If he listen what to what I say!"
        "Mr Bolt was deeply depressed because..."
        hide bont normal
        menu:
            "...he cheated her wife":
                $dr.life_loss()
            "...he need help to do daily activities in the garage":
                jump hang_q14
            "...he is unable to walk":
                $dr.life_loss()
    label hang_q14:
        $ dr.current='hang_q14'
        scene w
        #hide Alice
        show bont normal
        Bont "The reason he could not do such activities is because ..."
        hide bont normal
        menu:
            "...he was unable to hold the car parts":
                $dr.life_loss()
            "...he could not identify the car parts":
                jump hang_q15
            "...he has forgot how to do his job":
                $dr.life_loss()
            "...he has conflict with his subordinates":
                $dr.life_loss()
    label hang_q15:
        $ dr.current='hang_q15'
        scene w
        show bont normal
        Bont "So the real reason behind his problem is..."
        hide bont normal
        menu:
            "...that he was not able to see":
                jump hang_q16
            "...that his subordinates do antics in the garage":
                $dr.life_loss()
            "...his was forgetful where he put the car parts":
                $dr.life_loss()
            "...he is becoming old":
                $dr.life_loss()
    label hang_q16:
        $ dr.current='hang_q16'
        scene w
        show bont normal
        Bont "He lost his sight"
        Bont "so, he wanted to kill himself"
        Bont "I can guess he tried glasses without success"
        Bont "So decided to kill himself by hanging because..."
        hide bont normal
        menu:
            "...he thought he was too old":
                $dr.life_loss()
            "...he has economic probles":
                $dr.life_loss()
            "...he thought the problem cannot be solved":
                jump hang_q17
            "...he did not want to bother his subordinates":
                $dr.life_loss()
    label hang_q17:
        $ dr.current='hang_q17'
        scene w
        show Alice
        hide bont normal
        Alice "Really!"
        hide Alice
        show bolt
        Bolt "Is as the doctor says"
        Bolt "I am too old and my blindness is incurable"
        show bont normal
        hide bolt
        Bont "He he he"
        show Alice
        hide bont normal
        Alice "Why are you laughing to that poor soul?"
        
        Alice "You are so mean"
        show bont normal
        hide Alice
        
        Bont "And you are so naïve, Miss Alice!"
        stop music 
        play music "conga.mp3"
        Bont "Mr. Bolt is indeed wrong!"
        Bont "He is not able to see menu because..."
        hide bont normal
        menu:
            "... he has a retina disease":
                $dr.life_loss()
            "... he has diabetes":
                $dr.life_loss()
            "... he has an opaque film covering his pupils":
                jump hang_q18
            "... he has cataracts":
                $dr.life_loss()
    label hang_q18:
        show bont normal
        scene eye_enf
        Bont "He as an opaque film covering his pupils"
        Bont "It is located in his corneas"
        Bont "You can see it yourself Alice"
        Bont "The membranes are called pterigyon"
        Bont "Usually NO treatment are required"
        Bont "unless it renders to symptoms"
        Bont "like the blindness in this patient" 
        Bont "and with a magic scalpel of my colleague Dr. Light"
        scene eye_cured
        Bont "So he is able to see..."
        hide bont normal
        show bolt
        scene w
        Bolt "So it means that..."
        show bont normal
        hide bolt
        Bont "you were going to kill yourself for a problem"
        Bont "That can be easily cured with a simple surgery"
        hide bont normal
        show Alice
        Alice "So..."
        hide Alice
        show bont normal
        Bont "So Alice, can I have the forms?"
        hide bont normal
        show Alice
        Alice "You are a very good doctor!"
        hide Alice
        scene garage
        show bolt_f at right
        "So a couple of week later the patient was operated"
        "He was able to see again… and"
        "and he continued repairing cars"
        "and helping his younger mechanics"
        "and helping his younger mechanics\nand not the otherway around!"
        hide bolt_f 
        scene w
        "Final diagnosis:\n1-Suicide attempt\n2-Secondary to blindness\n3-Secondary to bilateral pterigion"
        if persistent.promo:
            jump dev
        else:    
            $ persistent.Sadman=True
            return
label sadman:
    if 'persistent.check' in vars() and persistent.checkpoint_2 != None:
        "Where do you want to start?"
        menu:
            "From the beginning of the chapter":
                $ dr=Player('sadman')
                $ check=True
                jump hangman
            "From the an earlier saved game":
                $ dr=Player('')
                $ renpy.jump(dr.current)
    else:
        $ dr=Player('sadman')
    $ systolic=120
    $ diastolic=80
    stop music
    $ death_1='{color=#f00}Mr. Bad\'s sister didn\'t allow Dr. Bont to proceed.\n3 days after the consult the patient died.{/color}'
    $ dr=Player('sadman')
    label intro:
        play music 'mp3/Exhilarate.mp3'
        scene football
        "???"
        "And the ball moves!"
        Bont "Hey I am alone!"
        Bont "Give me the ball... It's just me and the goalie!"
        Bont "... I cannot breathe..."
        Alice "Dr. Bont!"
        Bont "Alice?"
        Alice "Dr. Bont!"
        Bont "Wait... I can breathe..."
        Alice "There is a new patient"
        Bont "Patient?"
        Inner "Am I in the hospital"
        scene er_img
        stop music
        play music "mp3/George Street Shuffle.mp3"
        Bont "Alice?"
        Alice "..."
        Alice "I am waiting for your orders, Dr. Bont"
        Bont "What time is it?"
        Alice "1:15 am"
        Bont "I see..."
        Alice "Sorry, Dr. Bont. I am a bit busy I couldn't take the patient's vitals."
        Bont "Don't worry, I'll take for you"
        Bont "In ER, I am supposed to do so..."
        Alice "Can I execute your orders?"
        Bont "No.. I mean, I need to see the patient, don't you think so?"
        Alice "Sorry doctor, there are too many patients..."
        Bont "... Don't say anymore!"
    label sadman_q1:
        $dr.current="sadman_q1"
        scene er_img
        Bont "Can I see the patient?"
        Alice "Mr. Bad and his sister will come soon."
        Alice "Here it is"
        Bont "Hello"
        Bad_m "..."
        Bont "Hello?"
        Bad_m "I want to die..."
        Inner "Not again!"
        Inner "NOT AGAIN!!"
        Inner "I hope he has a pterigyon"
        Inner "I doesn't be useful to ask him questions"
        Inner 'Probably "someone" else might now more abour what is going on...'
        "Who do you think can answers questions about Mr. Bad"
        menu:
            "Mr. Bad himself":
                $ dr.life_loss()
            "Ms. Alice":
                $ dr.life_loss()
            "Mr. Bad's sister":
                jump sadman_q2
            "Mr. Bad's wife":
                $ dr.life_loss()
    label sadman_q2:
        $ dr.current='sadman_q2'
        Bont "Good evening Mrs. Bad"
        Bad_f "I am desperate!"
        Bad_f "Please help me!!!"
        Bont "I'll do my best..."
        Bont "Tell me what happened"
        Bad_f "Since a month ago my brother became ill"
        Bad_f "He said that he want to kill himself"
        Inner "NOT AGAIN!"
        Bad_f "He was not able to eat, and the was not able to stand"
        Bad_f "He lost the spark of life"
        Bad_f "We are very wealthy and we did not have any economic stress"
        Bad_f "He has not complained of any love affair as far as I know"
        Bad_f "He also had afternoon fever in the last 2 weeks"
        Inner "Why Mr. Bad is too sad?"
        menu:
            "Because he lost a lot of money":
                $ dr.life_loss()
            "Not stated yet":
                jump sadman_q3
            "He was not able to eat":
                $ dr.life_loss()
            'He had fever in the last 2 weeks':
                $ dr.life_loss()
            'He has a hidden affair':
                $ dr.life_loss()
    label sadman_q3:
        $ dr.current = "sadman_q3"
        Inner "Indeed her story doesn't explain why Mr. Bad is sad"
        Inner 'However, there is something "odd" in her telling'
        Inner 'Which statement of  Ms. Bad is "odds"?'
        menu:
            "Because he lost a lot of money":
                $ dr.life_loss()
            "He was not able to eat":
                $ dr.life_loss()
            'He had fever in the last 2 weeks':
                jump sadman_q4
            'He has a hidden affair':
                $ dr.life_loss()
    label sadman_q4:
        $ dr.current = "sadman_q4"
        Inner 'I don\'t understand what does such "afternoon fever" mean?'
        Inner "That could be a really good hint for something else"
        Bad_f "I have nothing more to say"
        Bont "Let's examine the patient"
        show text "Physical examination"
    label sadman_q5:
        $ dr.current = "sadman_q5"
        Bont "Hello Mr. Bad, what can I do for you?"
        Bad_m "..."
        Bad_m "I want to die!"
        Inner "Cheez! he is even worse than Mr. Bolt..."
        Inner "I just wonder if all patients I attend are so depressed?"
        Bad_m "Let me die... doctor"
        Bad_f "You see... He has been treated by a psychiatrist and he is now worse"
        Inner "I have no idea what the heck is going on here"
        Bont "I will do by best"
        Bad_f "...He hasn't been able to stand up..."
        Inner "Really? that's sound interesting..."
        Bont "Mr. Bad, can you raise your left arm?"
        Bad_m "..."
        Bad_m "I can't!"
        Bont "Mr. Bad, can you raise your right arm?"
        Bad_m "..."
        Bad_m "I can't!"
        #Inner "Inner"
        Bont "Alice... come here now!"
        Alice "Yes, dr. Bont"
        Bont "Could you give the temperature"
        Alice "Of course, 37.1 degrees"
        Bont "Thanks..."
        label sadman_q6:
            $ dr.current="sadman_q6"
            Bont "If a patient is unable to raise at least one arm, what it is your more likely suspicion?"
            menu:
                "Myocardial infarction":
                    Bont "Are you c-rious?"
                    $dr.life_loss()
                "Monisanto Syndrome":
                    Bont "I never heard about that"
                    Bont "Where can I read more about that zebra"
                    $dr.life_loss()
                "Stroke":
                    $dr.current="sadman_q7"
                    jump sadman_q7a
                "Stomach ulcer":
                    Bont "Are you c-rious?"
                    $dr.life_loss()
        label sadman_q7a:
            Bont "Well the sudden lack of movement belong to the FAST mnemonics"
            Inner "F: Face"
            Inner "A: Arms"
            Inner "S: Speech"
            Inner "T: Time to call..."
            Inner "The latter is not needed, because he is already in the hospital"
            Inner "Hmm... I think we need to go deeper here..."
            menu:
                'How can we go "deeper"?'
                "Order a craneal tomography (CT) with contrast":
                    if 'ct_scan' in vars():
                        Inner "You should not insist in CT with contrast"
                        $dr.life_loss()
                    else:
                        $ct_scan=True
                        Inner "It looks like a good idea..."
                        Inner "but the problem of using CT with contrast is that such study doesn't allow us to identify bleeding"
                        jump sadman_q7
                "Order a craneal tomography (CT) without contrast":
                    $dr.current='sadman_q7'
                    $renpy.jump(dr.current)
                'Order a complete blood count (CBC)':
                    Bont "Are you c-rious?"
                    Inner "I don't get your strategy!"
                    $dr.life_loss()
                'Order potassium levels':
                    Bont "Are you c-rious?"
                    Inner "I really don't get it!"
                    $dr.life_loss()
        label sadman_q7:
            Inner "We need to distinguish if Mr. Bad is bleeding or not!"
            Inner "We need to know if surgery is needed or not"
            Inner "At this age, bleeding is not so common, but we need to discard it"
            Bont "Alice, please can you prepare Mr. Bad for a CT scan without contrast"
            Bad_m ".... I want to die!"
            Alice "I'll be quick!"
            show text "THIRTY MINUTES LATER"
            Alice "The CT scan is ready"
            Inner "Poor Mr. Bad, he is not able to move!"
            #Screen CT scan
            Alice "What have happened"
            Bont "Alice, Mr. Bad has bled!"
            Bont "It's a subtle bleeding..."
            Alice "Do I need to prepare him for surgery?"
            Bont "I think it's a good idea"
            Bont "Please take some blood test: CBC, electrolytes and a urine test"
            Alice "Understood, Dr. Bont"
            Alice "Should I call Dr. Zomb?"
            Bont "No, I don't want to..."
            Alice "But didn't you said that you want him prepare for surgery..."
            Bont "I need to labs before calling Dr. Zomb.."
            Alice "Understood!"
            show text "AN HOUR LATER"
            Alice "The labs are ready..."
            Bont "Hmm"
            #Screen labs...
            
            if 'persistent.checkpoint_2' not in vars():
                "Do you want to save your current progress?"
                menu:
                    "Yes":
                        $ persistent.checkpoint_2 = True
                        $ dr.current = 'sandman_q7x'
                    "No":
                        pass
        label sadman_q7x:
            Bont "It means that he has bled due to low platelets..."
            Alice "What do you think we can do?"
            Bont "Nothing... we need to call the hematologist..."
            Alice "So we transfuse..."
            Bont "Don't say that, Mr. Bad need further studies"
            Alice "So, should I call Dr. Vladd?"
            Bont "Please, do that"
            Alice "As your wish"
            "..."
            
            Alice "Take the phone..."
            Bont "Hello, Dr Vladd"
            vlad "I am very sleepy..."
            vlad "If you need some units of blood, you just take it from the bank"
            vlad "I'll sign the forms tomorrow and let me back to slee.."
            Bont "#HoldIt!\nI have no transactions to be done in the bank... but I have a deposit!"
            vlad "A deposit?"
            Inner "This is the only bank that prefer withdraws, but not deposits... especially during night time"
            Bont "I need to admit a patient!"
            vlad "What?"
            Bont "Yes, I this the case... I have a case"
            menu:
                vlad "Ok that is the chief complaint?\nWhy he requested for medical attention?"
                "He was deeply depressed":
                    $dr.current="sadman_q8"
                    $renpy.jump(dr.current)
                "He has a bleeding in the head":
                    vlad "Was he really bleeding?"
                    Bont "ooops, I don't think so"
                    $dr.life_loss()
                "He has low platelets":
                    vlad "I don't think it was the chief complaint"
                    Bont "no... not really"
                    $dr.life_loss()
        label sandman_q8:
            vlad "Ha ha ha, but I am not a psychiatrist!"
            Bont "I know, but Mr. Bad came with his sister and she said"
            Bont "he had being attended by a psychiatrist for a month without success."
            vlad "And?"
            Bont "In addition, she said something weird"
            Bont "something {b}unexpected{/b} for a person with depression"
            #menu:
            vlad "What did she said?"
            menu:
                "she said:"
                '"His brother has no financial issues"':
                    vlad "nah! that's is expected in a major depression"
                    Bont "You are right!"
                    $dr.life_loss()
                '"His brother has fever"':
                    $dr.current="sandman_q9"
                    $renpy.jump(dr.current)
                '"His brother was unable to stand up"':
                    vlad "nah! that's is expected in a major depression"
                    Bont "You are right!"
                    if 'depression_vlad' in vars():
                        $dr.life_loss()
                    else:
                        Inner "Not really, but i need a stronger argument!!"
                        $ depression_vlad=True
                        jump sandman_q8
        label sandman_q9:
            vlad "Fever... What it has to do..."
            Bont "I was pondering the same..."
            Bont "So I decided to do deeper analysis"
            menu:
                "How did Bont handle the problem"
                "He did a brain scan":
                    vlad "Why did you requested that?"
                    Bont "I don't remember"
                    $dr.life_loss()
                "He was asked to raise his both hands":
                    $dr.current="sadman_q10"
                    $renpy.jump(dr.current)
                "He took a CBC":
                    vlad "Why did you requested that?"
                    Bont "I don't remember"
                    $dr.life_loss()
        label sadman_q10:
            vlad "and?"
            Bont "He could do that!"
            menu:
                "Why did Mr. Bad could not raise his arms?"
                "Mr. Bad had a myocardial infarction":
                    vlad "Are you c-rious?"
                    $dr.life_loss()
                "Mr. Bad had Miquineto Syndrome":
                    vlad "I never heard about that"
                    vlad "Where can I read more about that zebra"
                    $dr.life_loss()
                "Mr. Bad had a stroke":
                    $dr.current="sadman_q11"
                    jump sadman_q11
                "Mr. Bad had a stomach ulcer":
                    Bont "Are you c-rious?"
                    $dr.life_loss()
        label sadman_q11:
            vlad "A stroke"
            Bont "Yes, Mr. Bad had a stroke"
            vlad "So, what does the CT scan revelead?"
            menu:
                #Screen 
                "What do you see in the CAT"
                "Blood":
                    $dr.current="sadman_q12"
                    jump sadman_q12
                "Cerebal mass":
                    vlad "Are you c-rious?"
                    $dr.life_loss()
                "Non-hemorragic stroke":
                    vlad "Are you c-rious?"
                    $dr.life_loss()
        label sadman_q12:
            vlad "Interesting"
            vlad "Why didn't you call a neurosurgeon instead?"
            menu:
                Bont "I didn't do that because..."
                "Dr. Zomb needs to sleep":
                    vlad "Me too!"
                    $dr.life_loss()
                "The patient has platelets too low":
                    $dr.current="sadman_q13"
                    jump sadman_q13
                "The hemoglobin levels were too low":
                    vlad "Brain surgery usually doesn't bleed so much"
                    Bont "Oops!"
                    $dr.life_loss()
        label sadman_q13:
            vlad "Interesting"
            menu:
                vlad "Why was platelet levels too low?"
                "Because he has leukemia":
                    $dr.current="sadman_q14"
                    jump sadman_q14
                "Because he has dengue fever":
                    vlad "Really?"
                    Bont "Not really!"
                    $dr.life_loss()
                "Because he has solid tumor":
                    vlad "Really?"
                    Bont "Not really!"
                    $dr.life_loss()
        label sadman_q14:
            vlad "I'll take the case"
            Bont "I have no idea which kind of leukemia he has..."
            vlad "I see, I have to do a bone marrow biopsy and take a look of the blood smear"
            Bont "Nice, see your there"
            "..."
            Bont "Mrs. Bad, the hematologist, Dr. Vlad will take the case of your brother"
            Bad_f "What now?"
            Bont "He told me that he will admit the patient under in the hematology ward"
            Bont "He will take the case."
            Bad_f "Will he be OK?"
            Bont "I don't know... He has to speak with you and he will treat him if he can..."
            Bad_f "Thanks"
            Bad_m "Thanks! I feel better..."
            '3 hours later'
            vlad "He has a acute myeloid leukemia (AML)"
            Inner "So the blood line responsible corresponds to a myeloid type..."
            Inner "The myeloid precursor kinda get rise to almost all blood cells, except lymphocytes, those that produce antibodies"
            
            Bont "Really? which type"
            vlad "It looks like an M2 type"
            vlad "I think we can deal with it!"
            vlad "You've done a good job"
            Inner "Damned! that's not good!"
            Inner "An M3 type had the worse prognosis before, but now it has a very good prognosis..."
            Inner "Any other type of AML have a bad prognosis"
            Inner "I feel sad... but that's life!"
            Bont "The life of the doctor is hard, decisions to be made..."
            Bont "We are not gods..."
            
        $persistent.Slow_Girl=True
        return
label slowGirl:
    
    stop music
    scene hospital
    if check==False and persistent.checkpoint_3 != None:
        "Where do you want to start?"
        menu:
            "From the beginning of the chapter":
                $ dr=Player('slowGirl')
                $ check=True
                jump hangman
            "From the an earlier saved game":
                $ dr=Player(persistent.checkpoint_3)
                $ renpy.jump(persistent.checkpoint_3)
    else:
        $ dr=Player('slowGirl')
    label slow1:
        stop music
        play music "mp3/Hackbeat.mp3"
        u4 "Hola! is there someone there?"
        Bont "Excuse me..."
        u4 "Yes..."
        Bont "Who are you?"
        manolo "Sorry, I am Manuel Alfredo De Los Angeles Pérez Rodríguez"
        Bont "So... who are you?"
        manolo "I am the one who steal the hearts of the women!"
        manolo "I am the new medicine student assigned to Emergency Department..."
        Bont "Ahh ok! I like your attitude..."
        Bont "A real freshman... nice to hear..."
        manolo "Yes... I am a tabula rasa... eager to know and learn!"
        Bont "Well, there are no patients! I wonder where Ms Alice is..."
        manolo "a linda ..."
        Bont "...Don't even think about that!"
        manolo "So it means that I can go home"
        Bont "Not really! I love a man who \"steals the hearts of the women\""
        manolo "What do you mean?"
        Bont "Let's talk about the heart..."
        manolo "No way! my heart is only for the ladies"
        Bont "Nop! I mean the ECG, the {color=#ff0000}\"heart\"{/color} of the Emergency Department"
        manolo "WHAT!"
        Bont "You look a bit pale"
        manolo "But I haven't studied that..."
        Bont "What are you doing in an Emergency Department if you don't know what about ECG!"
        manolo "But today it's my first day!"
        Bont "A cheap excuse!"
        Bont "Let's begin!"
        manolo "OK"
        label heart1:
            $dr.current="heart1"
            
            Bont "The heart is a special organ"
            Bont "The heart has {color=#ffff00}automatism{/color}"
            manolo "What is that?"
            Bont "{color=#ffff00}Automatism{/color} is a instrisic property of the cardiac muscle that allow depolarization without external stimulus"
            manolo "OK"
            Bont "The heart also has {color=#ffff00}rhythmicity{/color}"
            manolo "What is that?"
            Bont "Manolo, {color=#ffff00}rhythmicity{/color} is also an instrisic property of the heart muscle that related to automatism."
            manolo "ah?"
            Bont "It's a cycle of despolarization of heart cells in a regular fashion"
            manolo "So, it means that the heart cells depolarize like a the tic tac of a clock"
            Bont "Indeed, Sr. Manolo..."
            menu:
                Bont "Sr. Manolo, which parts of the heart are related to {color=#ffff00}automatism{/color} and  {color=#ffff00}rhythmicity{/color}?"
                "SA node":
                    $dr.life_loss()
                "AV node":
                    $dr.life_loss()
                "Purkinje system":
                    $dr.life_loss()
                "The whole heart":
                    $dr.current="heart2"
                    $renpy.jump(dr.current)
        label heart2:
            Bont "Indeed, the automatism and the rhythmicity occur in the whole heart"
            manolo "Indeed, it means that in normal conditions, the heart will discharge in a regular fashion"
            Bont "Yes! the heart normally does so"
            manolo 'However, there a problem with that statement! '
            Bont " A bloody damned genius! "
            menu:
                manolo "If all heary cell are able to discharge in a regular fashion, but..."
                "...why does it beat irregularly way in normal people?":
                    Bont "It doesn't happen!"
                    $dr.life_loss()
                "...it doesn't mean that they have to do in a orderly fashion":
                    $dr.current='heart3'                         
        label heart3:
            Bont "Oh! you are correct!"
            manolo "Really? derp... I mean... Of course"
            manolo "I mean... You are a great {color=#ffff00}maestro{/color}"
            manolo "I always knew it"
            stop music
            Alice "heeeeelp!"
            play music "mp3/Firebrand.mp3"
            Bont "Alice?"
            Alice "help me!"
            Inner "Alice? a patient"
            manolo "What is going on?... She looks like a nurse"
            Alice "Doctor, I am weak"
            Bont "Indeed Mr. Manuel... She plays two roles, yesterday a nurse, but today a patient"
            Alice "Stop kidding and help me... By the way who is this young guy"
            Bont "Ah... since we are in a hurry, I did not introduce you..."
            Bont "He is my personalized Padawan"
            manolo "Pada.."
            Alice "Padaw...?"
            Alice "Stop the monkey business, I cannot stand... I feel so weak..."
            Bont "Padawan... forget about that"
            manolo "I am a new med student"
            Bont "So you can take her the pulse and the temperature"
            Alice "I have taken the temperature myself"
            Alice "I have {color=#ff0000}fever{/color}"
            $International=True
            $temp_init= 38.5
            if International :
                $temp=str(temp_init)+"ºC"
            else:
                $temp_int=32+temp_init*5/9
                $temp_init=round(temp_init, 1)
                $temp=str(temp_init)+"ºF"
            Alice "It was [temp]"
            Inner "What? she have fever!"
            Bont "Don't worry Alice... we'll do my best"
            manolo "Do you mean we...derp... I mean..."
            manolo "Everything for a bella jovencita"
            Bont "I carry these masks... Quick Mr. Manuel..."
            Alice "ah... ah.."
            Alice "achorooo!"
            Inner "She is sneezing, and her nose looks red!"
            Inner "Alice also has runny nose..."
            Inner "This is so weird!"
            Alice "Cannot speak Dr. Bont"
            Bont "Be brave Alice"
            Bont "Hold my hand Alice"
            Inner "What the heck is this?"
            Bont "Go Manolo!"
            manolo "Ah?"
            Bont "Be a hero and save the damsel"
            manolo "Take her the pulse"
            $dr.current="first"
            $renpy.jump(dr.current)
            $ input_value = "x"
    label first:
        scene black
        $ overriding_on=True
        $ counter = 5
        $ times = 4
        $ duration = float(6.0/times)
        
        label pulse1:
            Inner "Count the number of pulsewaves (vibrations) in 6 seconds"
            python:
                while counter < times:
                    renpy.vibrate(0.2)
                    renpy.pause(duration, hard=True)
                    counter += 1
                renpy.jump('eval')
        
    label eval:
        $dr.current="eval"
        menu:
            "How many times did you felt the pulsewave?"
            "1":
                $dr.life_loss()
            "2":
                $dr.life_loss()
            "3":
                $dr.life_loss()
            "4":
                $dr.current="slow2"
                jump slow2
            "5":
                $dr.life_loss()
    label slow2:
        manolo "She has 4 pulsewaves 6 seconds"
        
        Bont "which means that:"
        menu:
            "She has a myocardial infarction":
                $dr.life_loss()
            "She has 40 pulsewaves per minute":
                $dr.current='slow3'
                $renpy.jump(dr.current)
            "She has a severe anemia":
                $dr.life_loss()
            "She is just faking a problem":
                $dr.life_loss()
    label slow3:
        Alice "Are you going to take my blood pressure"
        Bont "Sorry, but we can wait for that"
        Bont "I need to put a cardiac monitor"
        Alice "But I am a litte tired, that's nothing serious..."
        manolo "You have pulse frequency of 40 per minute..."
        Alice "What? that's too slow!"
        Alice "Do you believe this rookie"
        Bont "Unfortunately he is right!"
    label slow4:
        $dr.current
        Alice "What does it mean?"
        Bont "Given the current data what will you answer to her?"
        menu:
            
            "You have a myocardial infarction":
                $dr.life_loss()
            "I don't know":
                $dr.current='slow5'
            "You have a severe anemia":
                $dr.life_loss()
            "You caught a cold":
                Bont "Indeed we have evidence that Alice caught a cold"
                Bont "But it doesn't explain why she has so low pulse!"
                $dr.life_loss()
    label slow5:
        menu:
            Bont "How can we know what is going on?"
            "Using a cardiac monitor":
                $dr.current ="slow6"
            "Taking a throat culture for bacteria":
                Bont "It maybe a good idea, but we have more important business"
                manolo "You are right maestro"
                $dr.life_loss()
            "Taking sodium blood levels":
                Bont "This is pointless"
                $dr.life_loss()
    label slow6:
        Bont "I already have the monitor..."
        Bont "Ok, dear colleague need a monitor, I think we need to continue our talk we go interrupted!"
        manolo "Damned a monitor... but I am a vulgar med student!"
        Bont "Once you finish... You'll become a real doctor to my eyes"
        manolo "Really?..."
        manolo "...I mean, of course {color=#ffff00}maestro{/color}"
        Bont "Let's see the strip"
        manolo "Let's do this"
        menu:
            Bont "What is the diagnosis"
            "I see two sets of hearts":
                $dr.current="slow7"
            "Myocardial infarction":
                Bont "Not at all!"
                $dr.life_loss()
            "Ectopic beats":
                Bont "Close.. but not at all!"
                $dr.life_loss()
        label slow7:
            Alice "What kind of silly answer is that?"
            Alice "Hey! I feel better!"
            manolo "Indeed... It's silly..."
            Bont "But... you have revealed the beautiful and silly {color=#ffff00}gem of the truth{/color}"
            Bont "Could you elaborate... what do you mean?"
            Bont "When you said there were {color=#ffff00}2 hearts{/color}"
            manolo "It looks to me like {color=#ffff00}2 sets of waves{/color}"
            Bont "There are {color=#ffff00}2 sets of waves{/color}..."
            Bont "Before someone interrupt us"
            Alice "Hey! I am here!"
            Bont "Sorry! I continue..."
            Bont "You ponder how if each cell in the heart has {color=#ffff00}automatism{/color} and {color=#ffff00}rhythmicity{/color}"
            Bont "How the heart doesn't enter in chaos"
            manolo "It's true... it's like a orchestra with each musician playing whatever they want..."
            Bont "It doesn't matter how good is each musician..."
            ""
            manolo "I think there is some kind of \"director\" who organize ..."
            Bont "...everything"
            Bont "Each heart cell has its own speed of discharge..."
            Bont "However with a {color=#ffff00}natural pacemaker{/color}" 
            Bont "Therefore the natural pacemaker..."
            manolo "...coordinates and the fastest cells direct the whole heart"
            Bont "Exactly"
            Alice "I feel way better, but what are these cables?"
            Bont "It's a temporary pacemaker..."
            Alice "A what?"
            Bont "Don't pull it out... of you'll feel bad again"
            
        label maestro1:
            $dr.current='maestro'
            Bont "Let's continue..."
            Bont "Therefore, she has a complete AV block!"
            manolo "A new \"director\" has taken the control of the heart"
            Bont "Indeed a {color=#ffff00}slower{/color} pacemaker, but the old one still beating..."
            Bont "...but the old {color=#ffff00}director{/color} still there, but it cannot get the message because..."
            menu:
                "...it is blocked":
                    $dr.current='maestro2'
                "...it is our of control":
                    $dr.life_loss()
                "...there is no enough data to say anything":
                    $dr.life_loss()
        label maestro2:
            $dr.current='maestro2'
            manolo "Should you want me to present the case to a surgeon?"
            Alice "A surgeon?"
            Alice "There is no way I allow a surgery!"
            Bont "I am not talking about surgery at all"
            manolo "but she has a problem..."
            Bont "..that we know nothing about..."
            Bont "I think we need to know more about what's happened"
            Alice "Ok ask whatever you want!"
            Bont "Tell us what happened"
            Alice "Since yesterday, I had cough, sneezing, runny nose..."
            Alice "I also was not able to swallow"
            manolo "Interesting!"
            Bont "Fascinating... What happened the day before?"
            Alice "I was working as usual, I felt fine..." 
            manolo "When did the fever started?"
            Bont "Since yesterday?"
            Alice "All of the symptoms started yesterday"
            manolo "but it could be rheumatic fever..."
            Alice "Rheumatic what?"
            Bont "Oh... someone is studying!"
            manolo "A pharingeal infection that relates to heart problem"
            manolo "Can I take a pharingeal swap?"
            Alice "No way!"
            Bont "Why not? I think it's a good idea!"
            manolo "Let's try that!"
            Alice "Ok..."
            Alice "Let's try that!"
            manolo "a pharingeal swap..."
            Alice "Gah! Gah"
            Bont "So, what did you found?"
            manolo "It was negative"
            manolo "I think it was..."
            Bont "... something very bad"
            Alice "What do you mean?"
            manolo "It means that if you were positive"
            manolo "it means that we have a clear idea how to treat you"
            Alice "So, it means..."
            Bont "...that we need to hear more about your telling"
            Alice "I don't think I have nothing else to say..."
            Bont "hmmm"
            Bont "It means that Dr. Manolo is right"
            Alice "What do you mean?"
            manolo "Can I call the surgeon"
            Alice "..."
            Alice "Wait... I... I... I have something else to say..."
            Bont "I think... my ears suddenly opened!"
            manolo "My ears are also opened"
            Alice "I bought some acetaminophen pills"
            Bont "Can I see one of these pills"
            Bont "What is your opinion colleage Manuel?"
            #Screen on pills
            manolo "100 mg?"
            Bont "Indeed... 100mg sounds very weird!"
            manolo "Can we see the labels where the pills come from?"
            manolo "That's weird the ECG looks fine..."
            label palish:
                $dr.current='palish'
                manolo "Alice looks pale..."
                Bont "I don't think it's ECG, it looks like juicy secrets... "
                Alice "Nooo!"
                Alice "I confess..." 
                Alice "I took some acetamiphonen pills from the medications banks..."
                Bont "Sorry, but we beg to differ!"
                menu:
                    Bont "My colleague and I think that..."
                    "...you have not done taken any pill from the bank":
                        $dr.life_loss()
                    "...you have not taken acetaminophen pills from the bank":
                        $dr.current='final1'
                    "...it's irrelevant if you have taken any pills from the bank":
                        $dr.life_loss()
            label final1:
                manolo "You took something else from the bank"
                Alice "What is this rookie taking about?"
                Bont "He is taking about something some pills causing a heart block!"
                Bont "Mrs Gloria!"
                Alice "Wait stop that!" 
                manolo "Don't worry..."
                manolo "It's a secret among us..."
                Gloria "Sorry Dr. Bont but I am a bit busy..."
                Bont "Don't worry! I just want to see the bank of pills"
                Gloria "Why do you want to do so?"
                Bont "It's something we have some business to do"
                Gloria "You are not authorized to..."
                Bont "... take any medications"
                Bont "We just want to see take a peek! it's a life or death issue"
                Gloria "A what?"
                Bont "just business as usual..."
                Gloria "OK, but not take anything"
                Bont "promise Lady Gloria"
                Gloria "Hummf, do that!"
               #Screen pill bank!
                Bont "Miss Gloria, we want to read what this label says"
                Gloria "It says \"atenolol\""
                Bont "{color=#ffff00}Atenolol{/color}... so, Dr. De Los Angeles"
                manolo "are you talking to... sorry, yes sir!"
                label final2:
                    Bont "What do you think is relevant about {color=#ffff00}atelolol{/color}"
                    menu:
                        "It has a starting dose of 100mg":
                           $dr.life_loss()
                        "The pills are white":
                           $dr.life_loss()
                        "Mrs. Gloria has a poor handwriting":
                           $dr.life_loss()
                        "It may cause complete AV blocks":
                           $dr.current='final3'
                label final3:
                    Bont "Thank you Mrs. Gloria..."
                    Gloria "What a waste of time"
                    Bont "Your cooperation has been more valuable"
                    Gloria "Go back to see my patients"
                    Alice "So I took..."
                    manolo "{color=#ffff00}atenolol{/color} in a very high dose"
                    Bont "And you naturally developed a complete heart block"
                    manolo "So you will not need any permanent pacemaker!"
                    Bont "Because once the body get rid of the drug, you'll be fine"
                    Bont "So thank you mr... sorry Dr. Manuel De Los Angeles"
                    Alice "Thanks, Dr. De Los Angeles"
                    manolo "No! don't call me like that! There is a lot to learn..."
                    manolo "I need to study more and become a real doctor, like Dr. Bont"
                    Bont "So be it..."
                    Bont "I hope we see more patients together!"
                    manolo "I'll study hard and do my best!"
                    show text "To be continued!"
    return
label fat1:
    if check==False and persistent.checkpoint_7 != None:
        "Where do you want to start?"
        menu:
            "From the beginning of the chapter":
                $ dr=Player('fat1')
                $ check=True
                jump hangman
            "From the an earlier saved game":
                $ dr=Player(persistent.checkpoint_7)
                $ renpy.jump(persistent.checkpoint_7)
    else:
        $ dr=Player('fat1')
    Alice "Hello Grace"
    Layzee "Hello Alice, where the patient?"
    Alice "Here is the chart, Grace"
    Layzee "Thanks..."
    InnerL "Hmmm, these Obgyns are crazy!"
    InnerL "A wedge resection of the ovary to fix a polycyst ovarian syndrome {color=#ffff00}(PCOS){/color}"
    Layzee "Alice, can I see the patient?"
    Alice "Do you have any order, Grace?"
    Layzee "Of course not!"
    Alice "You are right, Grace..."
    Alice "You need to see the patient... here it is..."
    Layzee "Thank you! Alice"
    Alice "Be my guest, Grace"
    Alice "Good morning, Mrs. Wahlee"
    Alice "She is Dr. Grace Layzee"
    Alice "She is the anesthesiologist"
    Layzee "Nice to meet you, Mrs. Wahlee"
    FatLady "So, you are..."
    Layzee "I am the doctor responsible for anesthesia while you are operated..."
    Layzee "Could you leave us alone, Alice"
    Alice "I leave you alone Mrs. Wahlee and Grace..."
    Layzee "Bye, Alice"
    FatLady "Hmm... Why does the nurse speaks so \"casually\" to you"
    Layzee "ha ha ha, we were are very closely related, but I prefer to go back to our business..."
    FatLady "Sorry, I didn't want to be rude..."
    Layzee "Don't worry... Tell me a bit about you..."
    FatLady "Well, Dr. Gyn told me ..."
    Layzee "Sorry, but I would like to know why do you consulted Dr. Gyn"
    FatLady "Well, my husband and I have tried to get a child, but we have tried for two years..."
    FatLady "...but we were not being successfull"
    InnerL "I think in a follow-up question... what it could be more appropriate?"
    menu:
        "How did you met Dr. Gyn?":
            $ dr.life_loss()
        "How did you met your husband?":
            $ dr.life_loss()
        "Is there any fertily problem with your husband?":
            $dr.current='fat2'
    label fat2:
        FatLady "Dr. Gyn requested help from an urologist"
        FatLady "The urologist found no problems with him"
        InnerL "Interesting"
        InnerL "So it means..."
        InnerL "That the infertility problem is due a problem ..."
        menu:
            '...Mr. Wahlee':
                $dr.life_loss()
            '...Mrs. Wahlee':
                $dr.current="fat3"
            '...Mr. and Mrs. Wahlee':
                $dr.life_loss()
            '...there is no enough information!':
                $dr.life_loss()
    label fat3:
        Layzee "So, it means that you must have a problem"
        FatLady "Indeed, Dr. Gyn found a {color=#ffff00}PCOS{/color} while he did an {color=#ffff00}ultrasound test{/color}"
        Layzee "I see!"
        Layzee "Could you tell if you have any other disease?"
        FatLady "No, as far as I know"
        Layzee "Have you noticed some new symptoms, besides your infertility problem?"
        FatLady "Well, I have noticed that I have become a bit hungrier in the last week"
        FatLady "Also I have peed a lot amount of water and I drink a lot of water"
        InnerL "Interesting..."
        Layzee "Alice! come quick!"
        Alice "Here I am, Grace!"
        Layzee "Are the lab test of Mrs. Wahlee ready?"
        Alice "Not yet, Grace"
        FatLady "I have an ECG and x-rays requested by Dr. Gyn"
        Layzee "Could I see them? is there any other lab that can I see?"
        FatLady "No I just have these"
        #x-ray and #ECG
        InnerL "Well, I cannot find anything else"
        Layzee "Alice!"
        Alice "Tell me Grace..."
        Layzee "Are the lab test ready?"
        Alice "Unfortunately not..."
        Alice "However, the urine test seems to be ready"
        Layzee "Can I see?"
        Alice "Here it is..."
        InnerL "Is there anything wrong with the urine test?"
        menu:
            "Specific gravity: 1.008 Normal(1.003-1.030)":
                $ dr.loss_life()
            "Red Blood cells casts: - Normal(-)":
                $ dr.loss_life()
            "Leukocytes casts: - Normal(-)":
                $ dr.loss_life()
            "Glucose: + Normal(-)":
                $ dr.current = 'fat4'
            "Nitrite test: - Normal(-)":
                $ dr.loss_life()
        label fat4a:
            Layzee "Damned, what is this?"
            FatLady "Is there anything wrong, Dr. Layzee?"
            Alice "Is there anything wrong, Grace?"
            Layzee "Alice, call Dr. Bont immediately!"
            Layzee "I also need the lab tests..."
            Alice "Why?"
            Layzee "No time to ask! please fetch the labs quickly!"
            Alice "Ok!"
            Layzee "I have to speak with Dr. Bont"
            FatLady "Who is Dr. Bont"
            Layzee "He is our diagnostician..."
            Layzee "It seems that the surgery can wait!"
            FatLady "There are more urgent matters, and I need Dr. Bont to help us"
            '...'
            Alice "He is coming soon..."
        label fat4:
            Bont "Hello, Dr. Layzee..."
            InnerL "So, it comes that pretentious prick!"
            Layzee "Hello, my dear..."
            Bont "Hello, Dr. Layzee... why are so pale and..."
            Layzee "No, I'm fine... but we need to talk about Mrs. Wahlee"
            Bont "Who?"
            Layzee "Sorry, Mrs. Wahlee... he is Dr. Jamie Bont"
            Layzee "He is our diagnostician..."
            Bont "Ok, how can I help you"
            FatLady "I don't understand either..."
            Bont "Could you tell us what's going on?"
            Layzee "Well, Mrs Wahlee..."
            "Which service is in charge of Mrs. Wahlee?"
            menu:
                "She is treated by an ObGyn":
                   $dr.current='fat5'
                "She is treated by an urologist":
                    $dr.life_loss()
                "She is treated by a hematologist":
                    $dr.life_loss()
                "She is treated by a psychiatrist":
                    $dr.life_loss()
        label fat5:
            Bont "So why was she treated by ObGyn"
            "Which was Mrs. Wahlee's chief complain?"
            menu:
                "PCOS":
                    $dr.life_loss()
                'Infertility':
                    $dr.current='fat6'
                "Weight issues":
                    $dr.life_loss()
                "Complicated pregnancy":
                    $dr.life_loss()
        label fat6:
            Bont "So, she had a problem of infertility"
            Bont "Can you tell me which problem is causing her infertility?"
            Layzee "Let me recall it!"
            menu:
                "PCOS":
                    $dr.life_loss()
                'Infertility':
                    $dr.current='fat7'
                "Weight issues":
                    $dr.life_loss()
                "Complicated pregnancy":
                    $dr.life_loss()
        label fat7:
            Layzee "She has {color=#ffff00}P{/color}oly{color=#ffff00}C{/color}ystic {color=#ffff00}O{/color}varian {color=#ffff00}S{/color}yndrome known as {color=#ffff00}PCOS{/color}"
            Bont "I am a bit confused... why is she hospitalized?"
            "She was hospitalized because"
            menu:
                "She is under antibiotic treatment":
                    $dr.life_loss()
                "She is under chemotherapy":
                    $dr.life_loss()
                "She was going to be operated":
                    $dr.current='fat8'
        label fat8:
            Bont "Operated?"
            Layzee "Indeed, don't you remember that I am an anesthesiologist?"
            Layzee "She was going to undergo a wedge resection of the ovary"
            Bont "Hmmm..."
            InnerL "I know, it is weird!"
            Layzee "The physical examination was normal, as well as ECG and x-ray"
            Bont "What about the labs?"
            menu:
                "None of them are available now":
                    $dr.life_loss()
                "The urine test shows a cross out glucose":
                    $dr.current = 'fat9'
                "The blood test show abnormal levels of sodium":
                    Bont "Are you sure?"
                    Layzee "Not really"
                    $dr.life_loss()
                "The specific gravity of the urine test is normal":
                    Bont "I doesn't seems to be relevant"
                    Layzee "Indeed you are right!"
                    $dr.life_loss()
        label fat9:
            FatLady "It doesn't seem like a big deal?"
            Bont "Do you have the blood levels?"
            Layzee "Hey! here comes Alice!"
            Alice "Here are the blood test you requested..."
            Layzee "I don't think I need it anymore..."
            Alice "But Grace..."
            Layze "It seems that Dr. Bont seems to be more interested in them..."
            Bont "Alice, are these labs taken while fasting?"
            Alice "Indeed, Dr. Bont... you look pale!"
            FatLady "so it means"
            Layzee "I am sorry, but you cannot be operated today..."
            Alice "she has {color=#ffff00}210 mg/dl{/color} (Normal value: 70-126 mg/dl)"
            Layzee "Now, you have a newly diagnosed {color=#ffff00}diabetes mellitus{/color}"
            Layzee "It could be dangerous to perform a surgery in such conditions..."
            Layzee "Don't you think so, Dr. Bont"
            Bont "Indeed, I will give her some medications and she'll be discharge tomorrow"
            "So, the surgery didn't take place..."
            "But, it will not the last time we will hear from Mrs. Wahlee!"
            "...to be continued!"
    $persistent.Fat_Lady_2=True
    return
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
label damsel:
    if check==False and persistent.checkpoint_4 != None:
        "Where do you want to start?"
        menu:
            "From the beginning of the chapter":
                $ dr=Player('damsel')
                $ check=True
                jump damsel
            "From the an earlier saved game":
                $ dr=Player(persistent.checkpoint_4)
                $ renpy.jump(persistent.checkpoint_4)
    else:
        $ dr=Player('damsel')
    Bont "Good Morning, Alice!"
    Alice "Good Morning, Dr. Bont"
    Bont "Can we see our first patient?"
    Alice "Well, the next patient is a bit difficult..."
    Alice "She is my {color=#ffff00}cousin{/color}"
    Bont "Oh! your cousin"
    Inner "There is a saying in the medicine school"
    Inner 'A "relative" of health professional is a challenge'
    Alice "I had a very hard time to convince her..."
    Alice "Grace, you can come in..."
    Layzee "Good morning, Dr. Bont!"
    Inner "Are Alice and Dr. Layzee {color=#ffff00}cousins{/color}"
    Layzee "Alice told me that you are a very proficient..."
    Layzee "However, I think we can stop taking, I rather prefer dying without needles in my arm..."
    Alice "Stop that Grace..."
    Inner "Damned, she is a very proficient{color=#ffff00}colleague{/color}..."
    Inner "If she says these kind of things... "
    Inner "It doesn't look good!"
    Bont "Sorry, Dr. Layzee, but here I am the doctor and now you are just another patient..."
    Layzee "Ok! ok! Let's turn this down..."
    Layzee "Let's play your game..."
    Layzee "Probably a bit of {color=#ffff00}ananmnesis {/color}can turn you down"
    Alice "What does she mean, Dr. Bont?"
    Bont "She says that we have to listen her! I agree..."
    $w=25
    if international:
        $w=25*2.2
        $peso=str(w)+" kilograms"
    else:
        $peso=str(w)+" pounds"    
    Layzee "I have lost [peso] in 1 month"
    Bont "Hold it!"
    Inner "Which follow-up question seems more appropriate?"
    menu:
        "Have you joined a cult":
            $dr.life_loss()
        "Have you following any kind of diet?":
            $dr.current='damsel2'
        "Do you have fever":
            $dr.life_loss()
    label damsel2:
        Layzee "Don't insult me!"
        Layzee "I was not following any kind of diet"
        Layzee "I didn't want to loss wait!"
        Alice 'Grace, can you give me the {color=#00ff00}recipe{/color} to loss...'
        Layzee "No, Alice! I never want something bad happen to you..."
        Inner "It looks something pretty bad..."
        Bont "Sorry for the interruption, but we need to continue..."
        Layzee "I also noticed that I have fever during the afternoons"
        Alice "Grace! Why you didn't tell me!"
        Layzee "Alice!"
        Layzee "I didn't want to worry you!"
        Bont "Please continue..."
        Layzee "I also notice that my belly started to grow..."
        Inner "What?"
        Layzee "It is what you are imagining..."
        Inner "It looks like a {color=#ffff00}consumptive disease{/color}"
        Layzee "I can read it in your face: a {color=#ffff00}consumptive disease{/color}"
        Alice "What do you mean Grace?"
        Alice "What does Grace mean Dr. Bont"
        Inner "There are a lot of {color=#ffff00}consumptive diseases{/color}..."
        Inner "The most common are the deadliest..."
        Inner "but..."
        Bont "So, a {color=#ffff00}consumptive disease{/color}!"
        Bont "Can you give me a hint about..."
        Layzee "Sorry, but I am a humble anesthesiologist..."
        Layzee "I have some ideas in head... but"
        Alice "But Grace!"
        Bont "I would like to know more about the ananmnesis..."
        Bont "Of course, you are a doctor..."
        Bont "And took a lots of laboratories..."
        Layzee "... and I found nothing wrong"
        Layzee "except anemia (Hg 8 g/dl),"
        Layzee "leukocytes 15,000/mm3 (Normal value= 4,000-10,000/mm3),"
        Layzee "lymphocytes 95% (Normal value 15%-45%)"
        Inner "I think we need more data"
        Bont "Can I see your abdomen"
        Layzee "So you want to continue..."
        Bont "Of course"
        #Screen abdomen...
        Bont "So! it means that you have liquid in your abdomen..."
        Layzee "Do you want to hear what it means Alice?"
        Bont "Hold it!"
        Bont "I need a sample of that liquid..."
        #Screen ...
        Bont "Quick, send the liquid to pathology"
        "..."
        Alice "Dr. Mortimer want to speak with you..."
        Alice "Now..."
        Alice "He said something like {color=#ffff00}ZL{/color} stain"
        Layzee "A {color=#ffff00}ZL{/color} stain?"
        Bont "{color=#ffff00}ZL{/color} stain?"
        Bont "It sounds insteresting... don't you think Dr. Grace Layzee?"
        Alice "I am scare, what does it mean?"
        Bont "he he he... Let me talk to him!"
        Alice "Quick! Alice... He is in the line"
        Mortimer "Quick! Alice told me that this liquid comes is peritoneal fluid"
        Mortimer "Are you about the origin of this sample?"
        menu:
            "Of course, I took it myself...":
                $dr.current='damsel3'
            "I don't know":
                $dr.life_loss()
            "It comes from the stomach":
                $dr.life_loss()
    label damsel3:
        Bont "Have you done a Papanicolau stain?"
        Mortimer "I tried that, but it was negative!"
        Mortimer "I also tried a {color=#ffff00}Ziehl–Neelsen{/color} stain"
        Mortimer "And it was full of bacteria"
        Mortimer "you should..."
        Bont "...stop talking... I am very happy!"
        Bont "Dr. Mortimer found bacteria with a {color=#ffff00}Ziehl–Neelsen{/color}"
        Alice "What does it mean?"
        Bont "I give the honors to Dr. Grace Layzee..."
        Alice "Grace, what is Dr. Bont talking about"
        Layzee "I am a fool!"
        Layzee "I didn't want to worry you... but"
        Layzee "I thought I was going to die... but"
        Layzee "After the work made by my colleague Bont"
        Layzee "I learned that I will be cured"
        Layzee "I have a positive {color=#ffff00}Ziehl–Neelsen{/color} in peritoneal fluid that means..."
        Layzee "...that I am suffering {color=ffff00}peritoneal tuberculosis{/color}..."
        Bont "...and you can be treated with oral drugs"
        Alice "Really?"
        Bont "I am so happy, Dr. Grace Layzee"
        Layzee "Thank you! Dr. Bont!"
        "to be continued..."
    $persistent.Mad_Man=True
    return
label bigBoy:
    if check==False and persistent.checkpoint_6 != None:
        "Where do you want to start?"
        menu:
            "From the beginning of the chapter":
                $ dr=Player('bigBoy')
                $ check=True
                jump bigBoy
            "From the an earlier saved game":
                $ dr=Player(persistent.checkpoint_)
                $ renpy.jump(persistent.checkpoint_4)
    else:
        $ dr=Player('bigBoy')
    label boy1:
        Bont "Good morning, Dr. De Los Angeles..."
        manolo "Good morning, Dr. Bont"
        Alice "Good morning!"
        Alice "Quick doctors!!"
        Alice "A new pacient has arrived"
        Alice "A little boy unable to breathe"
        Bont "Let's take a look!"
        u2 "Hello Dr. Bont"
        manolo "Psst, Dr. Bont..."
        manolo "Why is she so calm?"
        Bont "Don't worry, just play along"
        Bont "Hello Mrs. Sweeny!"
        mom "Hello, Dr. Bont"
        Bont "Mrs. Sweeny, I really love the party"
        mom "Thanks, Dr. Bont, but my son..."
        Bont "I know... he cannot breathe"
        Bont "Could you allow my colleague Dr. De Los Angeles to listen to John's lungs?"
        mom "Whatever..."
        Bont "Excelent, Dr. De Los Angeles... listen to John's chest!"
        Bont "Just play along, manolo and listen to his chest"
        manolo "but..."
        Bont "Just play along!"
        Bont "Alice, come quick..."
        Alice "Yes, Dr. Bont"
        Bont "Prepare the usual recipe"
        Alice "Recipe..."
        manolo "nevermind! John can I listen to your lungs"
        john "...cannot breathe..."
        mom "Go John, show the chest to doctor..."
        manolo "{color=#ff69b4}This is so weird...{/color}"
        manolo "This is so weird"
        #Listening lungs
        Bont "Dr. De Los Angeles, what have you heard?"
        menu:
            "Nothing":
                $dr.life_loss()
            "Whistles and surreal sounds":
                $dr.current='boy2'
            "Drums":
                $dr.life_loss()
            "Why are you asking me?":
                $dr.life_loss()
    label boy2:
        Bont "These sounds are called {color=#ffff00}wheezing{/color}"
        manolo "{color=#ffff00}wheezing{/color}?"
        Bont "Indeed, it represents the obstruction of airways"
        manolo "It looks like an asthmatic to me!"
        Bont "You can hear that in a patient with {color=#ffff00}Chronic Pulmonary Obstructive Disease{/color} also known as {color=#ffff00}COPD{/color}."
        manolo "So, it means that the mechanism behind {color=ffff00}COPD{/color}"
        menu:
            "It's similar to asthma":
                $dr.current='boy3'
            "It's related to arrhythmias":
                $dr.life_loss()
            "It's similar to a pneumonia":
                $dr.life_loss()
    label boy3:
        Bont "Indeed, this poor fella is suffering an {color=#ffff00}asthma attack{/color}"
        manolo "So you ordered Alice"
        menu:
            "To prepare an inhalotherapy":
                $dr.current='boy4'
            "Looking for antibiotics":
                $dr.life_loss()
            "Calling the police":
                $dr.life_loss()
    label boy4:
        Bont "Are you ready Alice?"
        Alice "Roger!"
        manolo "Wao"
        "30 minutes later..."
        Alice "Quick! Dr. Bont"
        Bont "What is it?"
        Alice "Come!"
        Bont "Let's go manolo!"
        manolo "Let's go!"
        mom "My child!"
        mom "My child!"
        mom "he is complaining of stomach ache!"
        Bont "Damned! stomach ache... "
        Bont "Let's see his"
        mom "My child"
        Bont "We'll do our best"
        Bont "Dr. De Los Angeles..."
        Bont "Please perform a percusion of the abdomen"
    label boy5:
        Bont "Listen to the abdomen of the patient"
        manolo "Yes, sir"
        #Listening abdomen
        $ dr. current= 'boy6'
    label boy6:
        Bont "So it means that the abdomen is {color=#ffff00}distended{/color}, {color=#ffff00}silent{/color} and {color=#ffff00}tympanitic{/color}"
        manolo "So what it means?"
        if ("answer1" in locals()) or ("answer1" in locals()):
            Bont "Yes... I was going to ask that!"
        else:
            Bont "This is correct, but there is something else you forget to say!"
            manolo "What else did I forget to say?"
            menu:
                "The intestines are full of air":
                    if "answer1" in locals():
                        if "answer2" in locals():
                            $dr.current='boy7'
                        else:
                            jump boy6
                    else:
                        $answer1=True
                "The instestines are not moving":
                    if "answer2" in locals():
                        if "answer1" in locals():
                            $dr.current='boy7'
                        else:
                            jump boy6
                    else:
                       $answer2==True
                "The lungs are moved to the abdomen":
                    Bont "Don't be ridiculous!"
                    $dr.life_loss()
        label boy7:
            Bont "Indeed, the combination of intestines that are filled of air that does not move represent a {color=#ffff00}paralytic ileus{/color}."
            manolo "A {color=#ffff00}paralytic ileus{/color}?"
            Bont "There is only one thing we can do now..."
            #Nasogastric tube
            manolo "Done!"
            Bont "We cannot do anything else..."
            manolo "What?"
            Bont "So it means that we have to wait that John's body metabolize the drug..."
            mom "What does it means?"
            menu:
                "Your son is going to die!":
                    $dr.life_loss()
                "The drug will be transformed by the body":
                    $dr.current='boy_end'
                "We need to operate him {color=#ffff00}immediately{/color}":
                    $dr.life_loss()
        label boy_end:
           Bont "Indeed doctor, we need to wait"
           manolo '"Amaneceremos y veremos"'
           Bont "What does it means"
           manolo "We have to wait to see what happens tomorrow"
           Bont "You have grown up, my little grasshopper..."
           manolo "I still have a lot to learn"
    $persistent.Slow_Girl=True
    return
label madman_1:
    $check = True
    if check==False and persistent.checkpoint_5 != None:
        "Where do you want to start?"
        menu:
            "From the beginning of the chapter":
                $ dr=Player('madman_1')
                $ check=True
                jump madman_1
            "From the an earlier saved game":
                $ dr=Player(persistent.checkpoint_5)
                $ renpy.jump(persistent.checkpoint_5)
    else:
        $ dr=Player('madman_1')
            
    label blood_p:
        $config.overlay_functions.append(ticker)
        call screen gauge
        $ result_map = _return 
        $ ticker
        if result_map == '1':
            if pressure < 200:
                hide screen gauge
                $ needle += 16
                $ pressure += 10
            jump blood_p
        if result_map=='2':
            if deflate > 1000:
                $ deflate = 120
            if deflate > 60 and deflate <= 120:
                $ deflate -= 30
            jump blood_p
            
        if result_map == '3':
            #$ ticker()
            if deflate < 120:
                $ deflate += 30
            if deflate == 120:
                $ deflate = 10000
            jump blood_p
        if result_map=='4':
            jump calculate
        jump blood_p
        
    label calculate:
        hide screen gauge
        #$ config.overlay_functions.remove(ticker)
        $ dr.current='calculate bp'
        "Enter diastolic pressure (The highest value where you stop hearing after deflating\nthe Korokoff noises)"
        menu:
            "60":
                $dia_res=60
                jump dia
            '80':
                $dia_res=80
                jump dia
            "90":
                $dia_res=90
                jump dia
            "100":
                $dia_res=100
                jump dia
            "110":
                $dia_res=110
                jump dia
            "120":
                $dia_res=120
                jump dia
            "130":
                $dia_res=130
                jump dia
    label dia:
        if dia_res==diastolic:
            jump calculate_syst
        else:
            "Enter the correct value"
            $ dr.life_loss()
    label calculate_syst:
        "Enter systolic pressure (The highest value where you start hearing after deflating\nthe Korokoff noises)"
        menu:
            "110":
                $syst_res=110
                jump syst
            '120':
                $syst_res=120
                jump syst
            "130":
                $syst_res=130
                jump syst
            "140":
                $syst_res=140
                jump syst
            "150":
                $syst_res=150
                jump syst
            "160":
                $syst_res=160
                jump syst
            "170":
                $syst_res=170
                jump syst
        #$persistent.Big_belly_boy=True
        #return
    label syst:
        if syst_res==systolic:
            $ renpy.jump(dr.current)
        else:
            $ dr.life_loss()
    $persistent.Damsel_Distress =  True
label dev:
    scene happy dev
    Hedley "Hello! my name is Hedley Quintana"
    Hedley "I am the main developer of this game"
    Hedley "I am a medical doctor and I currently a PhD Student in Karolinska Institute"
    Hedley "The case you saw... actually happened"
    Hedley "..."
    Hedley "It has a happy ending!"
    Hedley "If you haven't killed the patient... "
    Hedley "..."
    Hedley "The patient I attended was admitted in a ground floor..."
    Hedley "To be honest, the band ending is just a hypothetical scenario that didn't happened!"
    Hedley "However, the patient spent less than 12 hours in the ward"
    Hedley 'I call that "record" time'
    Hedley "Hey! did you like the game?"
    menu:
        'I love it!':
            jump dev_1
        "No, I didn't like it...":
            jump dev_2
        "I like it but it can be improved!":
            jump dev_3
    label dev_1:
        scene happy dev
        Hedley "I am very happy you liked it!"
        Hedley "These are few cases I've dealt with a couple of years ago"
        Hedley "Well, if you plan to study medicine..."
        Hedley "This is the sort of things that you'll be doing to take care of patients."
        Hedley "It's kinda a detective work..."
        Hedley "asking questions, looking for evidence"
        Hedley "and IRL click and point"
        Hedley "Well, I don't think you'll see a case like this one"
        Hedley "But you never know!"
        jump dev_3
    label dev_2:
        scene sad dev
        Hedley "I am sorry you didn't like it"
        Hedley '...'
        Hedley ':('
        jump dev_3
    label dev_3:
        scene happy dev
        Hedley "My intention was to use this language to teach medicine to students"
        Hedley "BTW, do not play doctor, get a license and work!"
        Hedley "It's no so expensive as you think..."
        Hedley "The tuition cost me less than US$ 500.00"
        Hedley "But it takes a lot of time (it took me six years and a half),"
        Hedley "and Spanish is my native language (I studied medicine in Spanish)"
        Hedley "BTW... sorry for any misspelling or grammar error"
        Hedley "Regardless if you like it or not, I do think you can help me to improve this game"
        Hedley "Let me know how it can be improved"
        Hedley "You can contact me at Twitter"
        Hedley "Twitter @hedleyquintana"
        Hedley "Or if you download it from lemmaforum.com, you can reply to the forum"
        Hedley "Many thanks for playing this game!"
        return
