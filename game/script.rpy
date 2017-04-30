# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# bush
image bush normal = "images/bush/bush_normal.png"
image bush sad = "images/bush/bush_sad.png"

# clinton
image clinton angry = "images/clinton/clinton_angry.png"
image clinton happy = "images/clinton/clinton_happy.png"
image clinton happy2 = "images/clinton/clinton_happy_2.png"
image clinton love = "images/clinton/clinton_love.png"
image clinton normal = "images/clinton/clinton_normal.png"
image clinton sad = "images/clinton/clinton_sad.png"

# megan
image megan normal = "images/megan/megan_normal.png"

# nixon
image nixon angry = "images/nixon/nixon_angry.png"
image nixon happy = "images/nixon/nixon_happy.png"
image nixon happy2 = "images/nixon/nixon_happy_2.png"
image nixon love = "images/nixon/nixon_love.png"
image nixon normal = "images/nixon/nixon_normal.png"
image nixon sad = "images/nixon/nixon_sad.png"

# trump
image trump angry = "images/trump/trump_angry.png"
image trump happy = "images/trump/trump_happy.png"
image trump happy2 = "images/trump/trump_happy_2.png"
image trump love = "images/trump/trump_love.png"
image trump normal = "images/trump/trump_normal.png"
image trump sad = "images/trump/trump_sad.png"

# others
image titlegroup = "images/other/titlegroup.png"
image titlenixon = "images/other/titlenixon.png"

# bg
image bg beach = "images/bg/beach.jpg"

# Declare characters used by this game.
define m = Character('Megan', color="#c8ffc8")
define n = Character('Nixon', color="#540f05")
define b = Character('Bush Sr.', color="#408401")
define c = Character('Clinton', color="#9035e0")
define t = Character('Trump', color="#20562c")




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
    show trump normal
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
    show clinton normal
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
    show nixon normal
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
    show bush normal
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
