label hangman:
    $ chart= []
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
    l "That sound suspicious, let's take a look, Sergeant... be quiet!"
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
    l "We seize him, called ER and we book… I mean submit you for medical treatment"
    scene black
    show text 'ER chart "Physical examination"' with Pause(2.5)
    show text 'ER chart "Physical examination"\n"Inform by Dr. Layzee"' with Pause(2.5)
    ""
    Inner "Grr! Dr Layzee… I hate that woman!"
    scene er_img
    show layzee at right
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
        $ dr.current = "hang_q1"
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
        python:
            question_1 = "Which of the following statements seems to contradict each other? and they may point out Mr. Bolt’s problem?"
            options= ["My garage is having normal clients as usual", "You know, the city is quite small",
                "My employees are young and require guidance", "But I don't like they take care of me"]
            correct=sorted(options[2:])
            selected_option=[]
        label menu_1:
            if selected_option:
                if len(selected_option) == 1:
                    $ question_1 += "\nYou have selected\n{color=ff0}"+selected_option[0] + "{/color}"
                else:
                    $ selected_option = sorted(selected_option)
                    if selected_option == correct:
                        jump hang_q9
                    else:
                        $ dr.life_loss()
                        jump menu_1
            scene w
            show bont normal
            "[question_1]"
            menu:
                "[options[0]]" if not options[0] in selected_option:
                    $ selected_option.append(options[0])
                    jump menu_1
                "[options[1]]" if not options[1] in selected_option:
                    $ selected_option.append(options[1])
                    jump menu_1
                "[options[2]]" if not options[2] in selected_option:
                    $ selected_option.append(options[2])
                    jump menu_1
                "[options[3]]" if not options[3] in selected_option:
                    $ selected_option.append(options[3])
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
            [(304, 263,394, 303, 'correct'),
             (356, 193,496, 301, 'correct'),
             (388, 294,596, 250,'correct'),
             (0, 0, 304, 600,'incorrect'),
             (315, 0, 800, 199,'incorrect'),
             (315, 418, 800, 600,'incorrect')
             ])
      
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
            [(361, 209,506,355, 'correct'),
             (0,0, 800, 209, "incorrect"),
             (0,600, 361, 209,"incorrect"),
             (506,355, 800, 600,"incorrect")
             ])
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
        Bont "He is not able to see because..."
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
