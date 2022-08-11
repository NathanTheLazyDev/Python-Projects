import time
#note from the dev: I quit this project now, I have posted it on github for archive. You can modify it as you wish however credit is still required.
lif = 10
amongus = True
brutal = False
mojangemploy = False
nptd = False
hasreachedmojang = False
loopcheck = True
def check():
    global amongus
    if lif <= 0:
        print("Normal death ending, You just... died normally")
        exit()
    elif lif <= 0 and brutal == True:
        print("poo ending, You died of diarrhea before you noticed it")
        exit()
    elif lif <= 0 and mojangemploy == True:
        print("Unemployment Ending, Mojang hates you unless you restart")
        exit()
    elif lif <= 0 and nptd == True:
        print("9 + 10 is not 21 ending, You die but you answered 9 + 10 incorrectly before you do")
    ##
    elif lif <= 0 and mojangemploy == True and nptd == True:
        print("Mojang just unemployed you because he realized you're not 9 + 10 kid ending, the longest ending name\non this game")
        exit()
    elif lif <= 0 and brutal == True and nptd == True and hasreachedmojang == True:
        print("depression ending, you thought about how mojang killed two of your lives but you get depressed and died")
        exit()
def quiz():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    global lif
    global brutal
    global mojangemploy
    global nptd
    global hasreachedmojang
    aa = (input("What's 9 + 10?\n"))
    if aa == "21":
        print("Good job\n\n\n")
    else:
        print("Wrong")
        lif -= 1
        nptd = True
        print("you now have", lif, "lives\n\n\n")
        ##
    ab = (input("What's the hexadecimal equivalent of the space character?\n"))
    if ab == "20":
        print("Good job\n\n\n")
    else:
        print("Wrong\n\n\n")
        lif -= 1
        print("you now have ", lif, "lives")
        ##
    ac = (input("Three letter word that amogus :flushed:\n"))
    if ac == "sus":
        print("Good job\n\n\n")
    else:
        print("Wrong")
        lif -= 1
        print("you now have ", lif, "lives\n\n\n")
        ##
    ad = (input("My Github Username, again ALL lowercase\n"))
    if ad == "nathanthelazydev":
        print("Good job\n\n\n")
    else:
        print("Wrong")
        lif -= 1
        print("you now have ", lif, "lives\n\n\n")
        ##
    ae = (input("unscramble the word: ineps\n"))
    if ae == "pines":
        print("Good job\n\n\n")
    elif ae == "penis":
        print("Half right, I'll take away 0.5 lives")
        lif -= 0.5
        print("you now have ", lif, "lives\n\n\n")
    else:
        print("Wrong")
        lif -= 1
        print("you now have ", lif, "lives\n\n\n")
    ##
    af = (input("What does TPOT stand for?\n\n\n"))
    if af == "the power of two":
        print("Good job\n\n\n")
    elif af == "the power of poo":
        print("Good jo- wait what the...\n\n\n")
    else:
        print("Wrong")
        brutal = True
        lif -= 1
        print("you now have ", lif, "lives\n\n\n")
    ##
    ag = (input("Konami code in wasd, no start button :)\n\n\n"))
    if ag == "wwssadab":
        print("Good job\n\n\n")
    elif ag == "wwssadabstart":
        print("+1 life for effort\n\n\n")
        lif += 1
        print("You now have", lif, "lives")
    else:
        print("Wrong")
        lif -= 1
        print("you now have ", lif, "lives\n\n\n")
    ##
    ah = (input("goofy ahh\n\n\n"))
    if ah == "quandale dingle":
        print("Good job\n\n\n")
    else:
        print("Wrong")
        lif -= 1
        print("you now have ", lif, "lives\n\n\n")
    ##
    ai = (input("I've been coding this for 2 hours staright, i need a b_e_k\n"))
    if ai == "break":
        print("Finally, some peace for 30 minutes aaaaaaaaaaaaauuughhhhhhh\n\n\n")
    elif ai == "bek":
        print("Congrats! you found an easter egg, Take this 2x hp\n")
        lif *= 2
        print("Cool!, Your HP multiplied to", lif, "\n\n\n")
    else:
        print("no rest? ;-;\n\n\n")
        lif -= 1
        print("you now have ", lif, "lives\n\n\n")
    ##
    aj = (input("dun dun dun dun dun dun dun...\n"))
    if aj == "dun dun dun":
        print("bussy saka\n\n\n")
    else:
        print(">:), -10 lives because no sus")
        lif -= 10
        print("you now have ", lif, "lives\n\n\n")
        ##
    ak = (input("I have to get more creative with questions... will you help?\nsay ok if yes\n"))
    if ak == "ok":
        print("Thanks\n\n\n")
    else:
        print("That's Alright, No lives taken away")
        print("you still have ", lif, "lives\n\n\n")
    ##
    al = (input("Whats 80 + 20\n"))
    if al == "100":
        print("You're good at math, Try the next one\n\n\n")
    else:
        print("This time, 9 + 10 is'nt 21 >:)")
        lif -= 1
        print("you now have ", lif, "lives\n\n\n")
    ##
    am = (input("what is the square root of 81?\n"))
    if am == "9":
        print("Seems like math dosent stop you.\n\n\n")
    else:
        print("Wrong")
        lif -= 1
        print("you now have ", lif, "lives\n\n\n")
    ##
    an = (input("Mojang interviews you\n[ mojang ] - What comes after 1.9?\n"))
    if an == "1.10":
        print("[ mojang ] - Congrats you're hired!\n\n\n")
        mojangemploy = True
        print("The boolean ` mojangemploy ` has been set to ` true ` ( if you know what that means )")
    elif brutal == True:
        print("mojang brutally shoots 2 of your lives without saying a thing")
        lif -= 2
    else:
        print("[ mojang ] - this is gonna hurt\n")
        time.sleep(2)
        print("mojang pulls a gun and shoots one of your lives")
        lif -= 1
        print("you now have ", lif, "lives\n\n\n")
    ##
    am = (input(" \n"))
    if am == "dun dun dun":
        print("\n\n\n")
    else:
        print("")
        lif -= 1
        print("you now have ", lif, "lives\n\n\n")
print("#####################################")
print("##    Nathan's never ending quiz   ##")
print("#####################################")
print("## A - Begin your suffering        ##")
print("## X - Not ready yet               ##")
print("#####################################")
print("")
inp = (input("## your selection:"))
if inp == "A" or inp == "a":
    print("Get your fingers ready, if you miss 10 questions\nyou have to restart all over again\n\nPro tip: always answer in lowercase ;)")
    quiz()