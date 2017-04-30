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

# Declare characters used by this game.
define m = Character('Megan', color="#c8ffc8")
define n = Character('Nixon', color="#540f05")
define b = Character('Bush Sr.', color="#408401")
define c = Character('Clinton', color="#9035e0")
define t = Character('Trump', color="#20562c")


# The game starts here.
label start:

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
