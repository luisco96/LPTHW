from textwrap import dedent
from sys import exit

# Base class for all the game scenes 
class Scene(object):

    def enter(self):
        print("This scene has not been written yet")
        print("Try another one. Bye!")

# First Scene of the game, based on the book "Red Rising" by Pierce Brown
class Lykos(Scene):

    def enter(self):
        print(dedent("""
            Welcome to the world of Red Rising, your name is Darrow
            and you are a Red. Basically the human race has expand 
            its domain to the whole Solar system. But you dont know
            that, 'cus you are a Red. Social herarqy goes like this:
            1. GOLDS - They are the pinacle of the human race and the ruling class
            2. SILVERS - Second to Golds they gobern smaller places and managed the money
            3. Coopers -  Like your sheriff.
            4. Here we start to see a lot of colors:
            \tBlues: Engineers and splace travelers
            \tGreys: Police and warriors
            \tPinks: Service people
            \tYellows: Pretty sure this are medics
            \tBrowns: dont remember
            \tWhites: Religion dudes
            \tThere are more but thats all you get, buy the books to learn more.
            5. Obsidians - This are like modified warriors trated like slaves, they big, they kill all, personal guards to the golds
            6. Red - Lowest of the lowest, pretty much slaves, miners and constructors, the majority 
            think the are building the society for the future generations but boy oh boy, that already happended
            """))
        print(dedent("""
            So you are Darrow, you did something that you shouldnt have done.
            Your wife is aobut to get murdered in a public execution. There is a 
            Copper and a Gold, the gold is the Governor of planet Mars, yep the dude
            basiccaly owns Mars. What do you do?
            """))

        action = input("> ")

        if(action == "Save wife"):
            print(dedent("""
            You cant let this happen so you run to your wife, trying to set
            her free. But your weak body can do nothing to the Gold and Cooper 
            supervicing the execution. The gold stops you with just one hand,
            he lift you by the neck, see you directly in the eye and brake your neck
            like it was nothing. You fall to the gorund dead, knowing that your wife 
            is next
            """))
            exit(0)