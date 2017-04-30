# You can place the script of your game in this file.
    
# The game starts here.
label start:
    call test
    return

# test out vars
label test:
    menu:
        "Sprite"
        "Trump":
            call trump_test
        "Nixon":
            call nixon_test
        "Clinton":
            call clinton_test
        "Bush":
            call bush_test
        "(Exit)":
            return
    jump test
        
label trump_test:
    show trump normal at right
    menu .menu_start:
        "Expression"
        "Normal":
            show trump normal
        "Angry":
            show trump angry
        "Happy":
            show trump happy
        "Happy 2":
            show trump happy2
        "Love":
            show trump love
        "Sad":
            show trump sad
        "(Back)":
            hide trump
            return
    jump .menu_start

label clinton_test:
    show clinton normal at right
    menu .menu_start:
        "Expression"
        "Normal":
            show clinton normal
        "Angry":
            show clinton angry
        "Happy":
            show clinton happy
        "Happy 2":
            show clinton happy2
        "Love":
            show clinton love
        "Sad":
            show clinton sad
        "(Back)":
            hide clinton
            return
    jump .menu_start

label nixon_test:
    show nixon normal at right
    menu .menu_start:
        "Expression"
        "Normal":
            show nixon normal
        "Angry":
            show nixon angry
        "Happy":
            show nixon happy
        "Happy 2":
            show nixon happy2
        "Love":
            show nixon love
        "Sad":
            show nixon sad
        "(Back)":
            hide nixon
            return
    jump .menu_start
    
label bush_test:
    show bush normal at right
    menu .menu_start:
        "Expression"
        "Normal":
            show bush normal
        "Sad":
            show bush sad
        "(Back)":
            hide bush
            return
    jump .menu_start
