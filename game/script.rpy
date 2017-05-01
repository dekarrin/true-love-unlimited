# You can place the script of your game in this file.
    
# The game starts here.
label start:
    window show
    $ love = 0
    jump beach
    scene bg black
    show megan normal at left
    "You are a 26-year old secretary."
    "Over the last few years, you've enjoyed a successful career as a secretary"
    show bg oldoffice
    "...as well as special 'friend' to your boss."
    show bg black
    "But after an incident at work..."
    show bg office
    show megan at right
    with dissolve
    show tattle angry at left
    with moveinleft
    tattle "I know what you're doing, slut! I found your clothes in his bed!"
    show tattle at Position(xpos=50)
    with move
    tattle "Better pay up or I'll tell everyone"
    show megan flip
    $ renpy.pause(0.5)
    show megan normal
    show knife at Position(xpos=500, ypos=510) behind tattle with moveinleft
    $ renpy.pause(2)
    show megan at Position(xpos=400)
    show knife at Position(xpos=150, ypos=510)
    with MoveTransition(0.2)
    play audio "audio/stab.ogg"
    $ renpy.pause(0.3)
    play sound "audio/scream.ogg"
    $ renpy.pause(0.2)
    scene bg black
    with dissolve
    $ renpy.pause(0.5)
    "..."
    show megan normal at left
    with dissolve
    $ renpy.pause(0.5)
    "You decide it might be best if you laid low and pursued other oppurtunities"
    show glasses at Position(xpos=135, ypos=105) with moveintop
    $ renpy.pause(0.5)
    "Unfortunately, with your new identity, you won't be able to rely on your past at all..."
    "Not even your Advertising and Marketing degree... not that it was worth much anyways."
    scene bg skyline with dissolve
    "Looks like you're on your own once again..."
    "Now get out there and find yourself a lucrative secretary job!"
    menu:
        "Where do you want to go first?"
        "The mall":
            jump mall
        "The beach":
            jump beach
        "The bar":
            "It's closed. You decide to go to the mall"
            jump mall
    
    return
    
label mall:
    scene bg mall
    "You're not gonna find any work HERE..."
    "Though you can't help but feel that you should have..."
    "Maybe it's the wrong mall..."
    "Hm..."
    "Ah well, this is no time to get introspective."
    menu:
        "What do you want to do?"
        "Look around":
            "You search the area furtively..."
            "Ah! You found a poster for a presidential meet-and-greet taking place at the beach..."
            jump beach
        "Dance on the escalator":
            "You dance on the escalator..."
            play sound "audio/scream.ogg"
            "...but fall over the edge and die."
            scene bg black with dissolve
            "Maybe you shouldn't have been slacking off so much!"
            jump dead_end

label beach:
    scene bg beach
    show titlegroup at left
    with dissolve
    show titlenixon at offscreenright
    with None
    show titlenixon at right
    with MoveTransition(0.2)
    "You find the presidents at the food stand."
    "You should be able to land a job pretty easily with one of them!"
    "Just be sure not to mention your dark stabby past"
    label .pick_a_prezzy:
        menu:
            "Who will you approach?"
            "Trump":
                jump .trump_pre_talk
            "Bush Sr.":
                jump .bush_pre_talk
            "Clinton":
                jump .clinton_pre_talk
            "Nixon":
                jump .nixon_pre_talk
    
    label .bush_pre_talk:
        show bush normal at right
        b "Hello there, young lady..."
        show bush sad
        b "Hey, do I know you? You seem familiar..."
        show bush normal
        menu:
            "Nope, I'm new here.":
                b "Weird... Ah well I'm too old to remember."
            "Yeah, I used to work for a friend of yours.":
                show bush sad
                b "I KNEW IT! YOU'RE THE ONE IN THE STABBING!"
                show bush normal
                b "Good job by the way. Worker #1 was a bitch."
                $ knows_stabbed = True
        b "Anyways, I'm a man of principle."
        b "And my answer no."
        b "Read the air, and read my lips:"
        show bush sad
        b "NO NEW SECRETARIES!"
        if knows_stabbed:
            show bush normal
            b "I don't wanna get stabbed, you freak..."
        hide bush
        jump .pick_a_prezzy
        
    label .trump_pre_talk:
        show trump normal at right
        t "Hi there, pretty girl."
        t "You might have heard of me..."
        show trump happy2
        t "Landed a little position called the President!"
        show trump happy
        t "Of the United States..."
        t "And might I add that you look very lovely..."
        show trump sad
        t "If not just a bit old..."
        show trump normal
        menu:
            "How dare you call me old!":
                show trump angry
                t "I'll call you whatever I want!"
                show trump happy2
                t "I'm the president, baby."
                show trump normal
                t "Look, is there something you wanted?"
            "Oh, I still got it if that's what you're after...":
                $ love += 1
                show trump love
                t "My first love is my country"
                show trump happy2
                t "But I don't mind having some pretty puss in my company too."
                show trump normal
                t "what did you need?"
            "Let's keep it to business":
                show trump sad
                t "Aw, see this is why girls like you are no fun..."
                t "You get all mature and shit..."
                show trump normal
                t "Anyways... was there somethin' you wanted?"
        m "Yeah, I'm lookin' to get into the secretary biz."
        show trump happy
        t "Aw, yeah, baby. I've been lookin' for one."
        show trump normal
        t "Why don't we head over to my bar to discuss the details"
        scene bg black with dissolve
        jump trump
        
    label .clinton_pre_talk:
        show clinton normal at right
        c "Hello."
        c "It's a beautiful day here on the beach."
        show clinton happy
        c "How can I help you?"
        menu:
            "Hey, you're not a president! Why are you here?":
                show clinton angry
                c "That's not important right now!"
                show clinton sad
                c "Why must you bring up such painful memories?"
                c "Are we done here?"
            "Naw girl; how can *I* help *you*?":
                show clinton happy2
                c "I don't exactly know what you mean by *that*..."
                show clinton happy
                c "But you're HILARY-ous."
                show clinton normal
                c "You're like half my age."
                c "Get real now, what did you need?"
            "I just wanted to tell you how amazing you are for being female.":
                show clinton love
                c "Yeah, it's pretty great."
                show clinton normal
                c "My party tells me I can pretty much do no wrong..."
                show clinton happy
                c "Just 'cause I'm female!"
        m "Yeah, so anyways I was wondering if you're in the market for a secretary?"
        show clinton happy2
        c "Hmm, you know I have actually been looking for a new one."
        show clinton sad
        c "Ever since the election, it feels like my whole staff has abandoned me..."
        c "..."
        show clinton happy
        c "I really think you could bring some life back into the office."
        show clinton normal
        c "I was about to head to my flower garden, if you wanted to accompany me?"
        c "We can discuss it further there."
        scene bg black with dissolve
        jump clinton
        
    label .nixon_pre_talk:
        show nixon normal at right
        n "Greetings, fellow American."
        show nixon happy
        n "I sure am glad to be a real human like you."
        n "I can feel things like the air and atmosphere on my human skin."
        hide nixon with Dissolve(0.1)
        show nixon normal at right, Transform(alpha=0.75)
        with None
        "*FLICKER*"
        n "What sort of human things would you like to discuss with me?"
        menu:
            "Are... are you a robot?":
                show nixon angry
                with None
                hide nixon with Dissolve(0.1)
                show nixon normal at right
                with None
                n "*bleep* *bloop*"
                show nixon happy
                n "Of course not, human female!"
                show nixon normal
                n "I am a regular human-person such as yourself."
                n "Now what can I help you with?"
            "(pass your hand through Nixon)":
                show nixon angry
                with None
                hide nixon with Dissolve(0.1)
                show nixon angry at Transform(zoom=1.5, xpos=400)
                with None
                hide nixon with Dissolve(0.1)
                show nixon angry at Transform(zoom=2.0, xpos=300)
                with None
                hide nixon with Dissolve(0.1)
                show nixon angry at Transform(zoom=2.5, xpos=200)
                with None
                hide nixon with Dissolve(0.1)
                show nixon angry at Transform(zoom=3.0, xpos=100)
                with None
                n "You should NOT have done that, foolish human!"
                n "My master will be most displeased."
                hide nixon with dissolve
                scene bg black with dissolve
                jump dead_end
            "Fine weather we've been having lately!":
                show nixon happy2
                n "Indeed, human-female."
                show nixon normal
                n "It is days like this that make me happy to be back in the past."
                show nixon sad
                n "Er, I mean in the present."
                show nixon happy
                n "Ahahaha! *bleep* *bloop*"
                show nixon normal
                n "Would you like to change to subject for me?"
        m "Uh... yeah... do you even need a secretary?"
        show nixon happy
        n "Of course! I would love to install myself as a normal member of society."
        show nixon normal
        n "I will do this by employing you!"
        show nixon sad
        n "Oh, but I must do the human interview process!"
        n "It's a formality you see."
        show nixon normal
        n "Come! Let us travel to the interview location!"
        scene bg black with dissolve
        jump nixon
            
label dead_end:
    scene bg dead_end with dissolve
    "YOU LOSE - YOU ARE DEAD"
    return
    