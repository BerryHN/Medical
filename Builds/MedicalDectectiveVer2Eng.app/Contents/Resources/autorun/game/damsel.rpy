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
