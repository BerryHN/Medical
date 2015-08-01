#Hangman        
init python:
   #s import random from random
    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    from operator import attrgetter # we need this for sorting items
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
    
    class Item(store.object):
        def __init__(self, name, description, image, submitted, symptom=True,  imageneology=False):
            self.name         = name
            self.description  = description
            self.image        = image
            self.symptom      = symptom
            self.submitted    = submitted
            self.imageneology = imageneology
        def imageneology(self):
            if self.imageneology:
                renpy.show_screen(self.imageneology)
            
               
#Images
image city = "first bg.jpg"
image w = "ward.jpeg"
image garage ="garage.png"
image black= "#000000"
image bont = "oslor0001t.png"
image layzee = 'layzee0001.png'
image bontw = "oslor0001t.png"
image bolt ='bolt closed0001.png'
image bolt_f ='bolt open0001.png'
image alice = 'alice_normal0001.png'
image alice angry = 'alice_angry.png'
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
#Characters
define u1 = Character('?????', color="#0000ff")
define u2 = Character('?????', color="#00ff00")
define u3 = Character('?????', color="#00ffa5")
define l = Character("Liutenant", color="#0000ff")
define s = Character("Sargent", color="#00ff00")
define Layzee = Character("Dr Layzee", color="#de64da")
define Bont = Character("Dr. John Bont", color="#ffffff")
define Inner = Character("Dr. John Bont -thoughts-", color="#999666")
define Alice = Character("Ms. Alice", color="#00ffa5")
define Layzee = Character("Dr. Lazy", color="#aaff55")
define Bolt = Character("Mr. Bolt", color="#ffffff")
define Bad_m = Character("Mr. Bad", color="#ffffff")
define Bad_f = Character("Mrs. Bad", color="#ffffff")
define vlad = Character("Dr. Vladd", color="#ffffff")
define Hedley = Character("Dr. Hedley Quintana", color="#ffffff")
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
    play music 'Splash.mp3'
    
    jump main_menu
    return
    
    
label fail:
    show bontw
    
    show text 'Easy! I have to be careful!' with Pause(1.0)
    show text 'Easy! I have to be careful!\nyou have [dr.life] point of life' with Pause(1.0)
    hide bontw
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

label hangman:
    $ chart= []
    show screen chart_button
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
    play music "W.ogg"
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
    show bont
    u3 "Miss Alice, a week here and I have nothing to do"
    hide bont
    show alice
    Alice "Tell me your orders Dr. Bont"
    hide alice
    show bont
    Bont "Orders?"
    hide bont
    show alice
    Alice "We have a new patient!"
    hide alice
    show bont
    Bont "A new patient?"
    hide bont
    show alice
    Alice "Yes this is the chart"
    hide alice
    show bont
    Bont "What?"
    hide alice
    show bont
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
        show bont
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
        show bont
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
        show bont
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
        show bont
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
        show bont
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
        show bont
        $ dr.current = 'hang_q6'
        Bont "It seems that as usual, we need a long talk with Mr. Bolt, don't you think so Alice?" 
        hide bont
        show alice
        Alice "The patient is ready, what are your orders?" 
        hide alice
        show bont
        Bont "No Alice, I need to speak with patient first... no injection needed (c)" 
        Bolt "..."
    label hang_q7:
        scene w
        show bont
        $ dr.current = 'hang_q7'
        "How can we follow?"
        hide bont
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
        hide bont
        hide bolt
        show alice
        Alice "Have you requested a shot"
        show bont
        hide alice
        Bont "No! get back to your business, Alice"
        jump hang_q8
    label hang_q8:
        $ dr.current = 'hang_q8'
        scene w
        show bolt
        Bolt "I can see your kind intentions, but I have a problem you cannot solve" 
        hide bolt
        show bont
        Bont "What's your problem?" 
        show bolt
        hide bont
        Bolt "My garage is having normal clients as usual"
        Bolt "You know, the city is quite small" 
        Bolt "My employees are young and require guidance" 
        Bolt "But I don't like they take care of me" 
        Bolt "I am too old..." 
        hide bolt
        show bont
        $ question_1 = "Which of the following statements seems to contradict each other? and they may point out Mr. Bolt’s problem?"
        $ correct_a=False
        $ correct_b=False
        label menu_1:
            scene w
            show bont
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
        show bont
        Bont "So it means that you are old and experience person"
        Bont "It doesn’t make sense to me that your employees require guidance" 
        Bont 'And they have to "take care" of you'
        hide bont
        show bolt
        Bolt "Because I am too old..."
        Bolt "I am not able to identify the tools and the car parts"
        hide bolt
        show bont
        Bont "That’s sounds horrible… but…"
        hide bont
        show bolt
        Bolt "What?"
        hide bolt
        show bont
        Bont 'Why are you not able to do such do such "trivial" tasks'
        hide bont
        show bolt
        Bolt "Because, I cannot see"
        hide bont
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
        show bont
        Inner "Indeed I have to look as his eyes"
        Inner "It seems a very complicated situation"
        Inner "Let's take a look of his left eye"
        hide bont
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
        show bont at right
        Inner "So it means that Mr Bolt is cannot see in his left eye"
        Inner "So it means that Mr Bolt is cannot see in his left eye"
        Inner "But, what's going on in the other eye?"
        "Click in the area causing the visual loss"
        hide bont
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
        show bont
        Inner "So this poor fella is indeed blind!"
        Bont "Alice! Quick!"
        show alice
        hide bont
        Alice "Gimme your orders, Dr. Bont!"
        hide alice
        show bont
        Bont "Could you give the form BA-27F"
        show alice
        hide bont
        Alice "What kind of order is that?"
        Alice "The patient has just been admitted due to suicide attempt!"
        Alice "Do you know what does the form does?"
        hide alice
        show bont
        Bont "I am ordering it! I know what it does!"
        'What do you think the form BA-27F does?'
        hide bont
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
        hide alice
        show bont
        Bont "This ward has nothing to offer to this patient"
        show alice
        hide bont
        Alice "I cannot obey such order"
        Alice "We are responsible for his safety"
        Alice "I can be sued if he tries to kill himself"
        hide alice
        show bont
        Bont "He cannot kill himself if he listen to me first"
        Bont "If he listen what to what I say!"
        "Mr Bolt was deeply depressed because..."
        hide bont
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
        #hide alice
        show bont
        Bont "The reason he could not do such activities is because ..."
        hide bont
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
        show bont
        Bont "So the real reason behind his problem is..."
        hide bont
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
        show bont
        Bont "He lost his sight"
        Bont "so, he wanted to kill himself"
        Bont "I can guess he tried glasses without success"
        Bont "So decided to kill himself by hanging because..."
        hide bont
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
        show alice
        hide bont
        Alice "Really!"
        hide alice
        show bolt
        Bolt "Is as the doctor says"
        Bolt "I am too old and my blindness is incurable"
        show bont
        hide bolt
        Bont "He he he"
        show alice
        hide bont
        Alice "Why are you laughing to that poor soul?"
        
        Alice "You are so mean"
        show bont
        hide alice
        
        Bont "And you are so naïve, Miss Alice!"
        stop music 
        play music "conga.mp3"
        Bont "Mr. Bolt is indeed wrong!"
        Bont "He is not able to see menu because..."
        hide bont
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
        show bont
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
        hide bont
        show bolt
        scene w
        Bolt "So it means that..."
        show bont
        hide bolt
        Bont "you were going to kill yourself for a problem"
        Bont "That can be easily cured with a simple surgery"
        hide bont
        show alice
        Alice "So..."
        hide alice
        show bont
        Bont "So Alice, can I have the forms?"
        hide bont
        show alice
        Alice "You are a very good doctor!"
        hide alice
        
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
                $ dr=Player(persistent.checkpoint_2)
                $ renpy.jump(persistent.checkpoint_2)
    else:
        $ dr=Player('sadman')
    $ systolic=120
    $ diastolic=80
    stop music
    $ death_1='{color=#f00}Mr. Bad\'s sister didn\'t allow Dr. Bont to proceed.\n3 days after the consult the patient died.{/color}'
    $ dr=Player('sadman')
    label intro:
        screen black
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
        Bad_m "I cann't!"
        Bont "Mr. Bad, can you raise your right arm?"
        Bad_m "..."
        Bad_m "I cann't!"
        Inner "Inner"
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
                    jump sadman_q7
                "Stomach ulcer":
                    Bont "Are you c-rious?"
                    $dr.life_loss()
        label sadman_q7:
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
            menu:
                "Do you want to save your progress?"
                "Yes":
                    $persistent.checkpoint_2=True
                "No":
                    pass
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
                    $dr.current="sadman_q11"
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
                "The need to sleep":
                    vlad "Me too!"
                    $dr.life_loss()
                ""
                ""
                ""
        $persistent.Slow_Girl=True
        return
label slowGirl:
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
    $ input_value = "x"
    label first:
        scene black
        $ overriding_on=True
        $ counter = 5
        $ times = 4
        $ duration = float(6.0/times)
        
        label pulse1:
            python:
                while counter < times:
                    renpy.vibrate(0.2)
                    renpy.pause(duration, hard=True)
                    counter += 1
                renpy.jump('eval')
        
    label eval:
        "wait"
        #$ overriding_on = None
     #   $ persistent.Question = "How many waves have you counted?"
        #$ success = 'cont'
      #  $ fail = 'first'
       # $ answer = '0'
        #call screen input_softkeyboard
        
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
    #$persistent.Damsel_Distress =  True
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

        
