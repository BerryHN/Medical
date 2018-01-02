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