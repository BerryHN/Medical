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
