#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random # random numbers
import sys # system stuff for exiting

player = {
    "name": "p1",
    "score": 0,
}

def printGraphic(name):
    if (name == "cat"):
        print '                      '
        print ' 　    　／ ＞　 　フ     '
        print '  　　   | 　-　 -|     '
        print ' 　　    ／  ミ＿Yノ     '
        print '  　    /　　　 　 |     '
        print '    　 /　 ヽ　　 ﾉ      '
        print '  　  │　　 |　|　|      '
        print '   /￣|　  |　|　|      '
        print ' 　| (￣ヽ＿_ヽ_)__)    '
        print '  　＼二つ              '
        print '                      '
        print '---------A-cat--------'
        print '-----You-are-right----'
        print '                      '


    if (name == "spongebob"):
        print  '                  '
        print  '  ▕▔▔▔▔▔▔▔▔▔▔▔╲   '
        print  '  ▕╮╭┻┻╮╭┻┻╮╭▕╮╲  '
        print  '  ▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏ '
        print  '  ▕╭┻┻┻┛┗┻┻ ▕ ╰ ▏ '
        print  '  ▕╰━━━┓┈┈┈╭╮▕╭╮▏ '
        print  '  ▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏ '
        print  '  ▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏ '
        print  '----spongebob-----'
        print  'How-did-you-get-it'
        print  '                  '

    if (name == "cryingface"):
    	print  '                         '
        print  '       ╭┈┈┈┈╯   ╰┈┈┈╮    '
        print  '                         '
        print  '        ╰┳┳╯    ╰┳┳╯     '
        print  '                         '
        print  '        O 　    　　 O     '
        print  '       ○  　    　　 ○     '
        print  '            ╰┈┈╯         '
        print  '       O  ╭━━━━━╮　 O     '
        print  '            ┈┈┈┈         '
        print  ' 　   　o     　　   o      '
        print  '                         '
        print  '------A-crying-face------'
        print  '---Such--a--genius-!-!-!-'
        print  '                         '

    if (name == "nooo"):
        print  '                         '
        print  'N                        '
        print  '　 O                      '
        print  '　　　 O                   '
        print  '　　　　 o                 '
        print  '　　　　　o                 '
        print  '　　　　　 o                '
        print  '　　　　　o                 '
        print  '　　　　 。                 '
        print  '　　　 。                  '
        print  '　　　.                    '
        print  '　　 .                    '
        print  '　　  .                   '
        print  '　　   .                  '

    if (name == "title"):
        print '------------------------------'
        print '-G-U-E-S-S--W-H-A-T--I--A-M-?-'
        print '------------------------------'


def firstGame():
    #Quiz 1
    print "I have 4 legs" 
    print "Guess what I am?"

    question = raw_input("I know the answer. Choose [Y or N]")

    if (question == "N"):
        print "Do you need more clues?"
        raw_input("press enter >")

        #Quiz 2
        print "I like catching mice" 

        question2 = raw_input("I know the answer. Choose [Y or N]")

        if (question2 == "Y"):
            print "Then, what I am?"
            ans = raw_input(">")
            if (ans == "cat"):
                printGraphic("cat")
            else:
                printGraphic("nooo")
                print "Good try but NO!"

        if (question2 == "N"):
            print "Do you need more clues?"
            raw_input("press enter >")
            
            #Quiz 3
            print "MEOW MEOW" 

            print "It is the last hint. Answer the question."
            print "Then, what I am?"
            ans = raw_input(">")
            if (ans == "cat"):
                printGraphic("cat")
            else:
                printGraphic("nooo")
                print "Good try but NO!"

    elif (question == "Y"):
        print "Then, what I am?"
        ans = raw_input(">")
        if (ans == "cat"):
            printGraphic("cat")
        else:
            printGraphic("nooo")
            print "Good try but NO!"

def secondGame():
    #Quiz 1
    print "I am a cartoon character." 
    print "Guess what I am?"

    question = raw_input("I know the answer. Choose [Y or N]")

    if (question == "N"):
        print "Do you need more clues?"
        raw_input("press enter >")

        #Quiz 2
        print "I live in the ocean." 

        question2 = raw_input("I know the answer. Choose [Y or N]")

        if (question2 == "Y"):
            print "Then, what I am?"
            ans = raw_input(">")
            if (ans == "spongebob"):
                printGraphic("spongebob")
            else:
                printGraphic("nooo")
                print "Good try but NO!"

        if (question2 == "N"):
            print "Do you need more clues?"
            raw_input("press enter >")
            #Quiz 3
            print "I am made of a sponge." 
            print "It is the last hint. Answer the question."
            print "Then, what I am?"
            ans = raw_input(">")
            if (ans == "spongebob"):
                printGraphic("spongebob")
            else:
                printGraphic("nooo")
                print "Good try but NO!"

    elif (question == "Y"):
        print "Then, what I am?"
        ans = raw_input(">")
        if (ans == "spongebob"):
            printGraphic("spongebob")
        else:
            printGraphic("nooo")
            print "Good try but NO!"


def thirdGame():
    print "I am a face." #Quiz 1
    print "Guess what I am?"

    question = raw_input("I know the answer. Choose [Y or N]")

    if (question == "N"):
        print "Do you need more clues?"
        raw_input("press enter >")
        #Quiz 2
        print "I am so sad." 
        question2 = raw_input("I know the answer. Choose [Y or N]")
        
        if (question2 == "Y"):
            print "Then, what I am?"
            ans = raw_input(">")
            if (ans == "crying face"):
                printGraphic("cryingface")
            else:
                printGraphic("nooo")
                print "Good try but NO!"

        if (question2 == "N"):
            print "Do you need more clues?"
            raw_input("press enter >")

            #Quiz 3
            print "I am expressing my feeling." 
            print "It is the last hint. Answer the question."
            print "Then, what I am?"
            ans = raw_input(">")
            if (ans == "crying face"):
                printGraphic("cryingface")
            else:
                printGraphic("nooo")
                print "Good try but NO!"

    elif (question == "Y"):
        print "Then, what I am?"
        ans = raw_input(">")
        if (ans == "crying face"):
            printGraphic("cryingface")
        else:
            printGraphic("nooo")
            print "Good try but NO!"


def introGame():
    global player

    print "Hello. What should I call you?"
    player["name"] = raw_input("Please enter your name >")

    print "Let's start the game, " + player["name"] + "!"
    print "Guess what I am with 3 clues"

    pcmd = raw_input("Are you ready to play? [Y/N]")

    if (pcmd == "Y"):
        print "You can choose the level [easy/medium/extremeHard]"
        pcmd = raw_input(">")

        if (pcmd == "easy"):
        	firstGame()

        elif (pcmd == "medium"):
        	secondGame()

        elif (pcmd == "extremeHard"):
        	thirdGame()

    else:
        print "It will be fun. Give me a chance."
        pcmd = raw_input("press enter >")
        introGame()


def main():
    printGraphic("title")
    introGame()

if __name__ == "__main__":
    main()
