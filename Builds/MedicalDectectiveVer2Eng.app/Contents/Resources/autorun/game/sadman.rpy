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