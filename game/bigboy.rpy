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
        
        u2 "Good morning, Dr. Bont"
        Bont "Good morning, Dr. Manuel De Los Angeles..."
        Alice "Good morning!"
        Alice "Quick doctors!!"
        Alice "A new pacient has arrived"
        Alice "A little boy unable to breathe.."
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
            "To prepare an inhalotherapy to release the obstruction in the airways":
                $dr.current='boy4'
            "Looking for antibiotics":
                $dr.life_loss()
            "Calling the police":
                $dr.life_loss()
    label boy4:
        Bont "Indeed, Dr. De Los Angeles"
        manolo "Don't do that, just call me Manolo"
        Bont "I can't do that with one of my colleagues"
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
        mom "And his tummy has grown big!"
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
        $ diastolic_pressure = ""
        $ dr.press = "calculate"
        hide screen gauge
    label calculate:
        
        if diastolic_pressure:
            if re.match("\d{1,3}",diastolic_pressure):
                if diastolic == diastolic_pressure:
                    "The value [diastolic_pressure] is correct!" 
                    "Now measure the systolic pressure"
                    $ dr.press= "calculate_syst"
                    jump calculate_syst
                else:
                    $ dr.life_loss()
            else:
                "Please, give a valid value"
                $ dr.life_loss()
        python:
            import re
            diastolic_pressure=renpy.input("Enter diastolic pressure (The highest value where you stop hearing after deflating\nthe Korokoff noises)")
            diastolic_pressure.strip()
            renpy.jump("calculate")
        
    label calculate_syst:
        if sys_pressure:
            if re.match("\d{1,3}",sys_pressure):
                if diastolic == sys_pressure:
                    "The value [sys_pressure] is correct!" 
                    $ renpy.jump(dr.current)
                else:
                    $ dr.life_loss()
                    $ renpy.jump("calculate_syst")
            else:
                "Please, give a valid value"
                $ dr.life_loss()
        python:
            import re
            #dr.current='calculate bp'
            sys_pressure=renpy.input("Enter systolic pressure (The lowest value where you stop hearing after deflating\nthe Korokoff noises)")
            sys_pressure.strip()
            renpy.jump("calculate")
        #return
    $persistent.Damsel_Distress =  True