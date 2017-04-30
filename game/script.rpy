# You can place the script of your game in this file.
    
# The game starts here.
label start:
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
    
    
    return
