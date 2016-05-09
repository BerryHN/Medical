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
            $dr.current='fat2_'
    label fat2_:
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