# import random
# import re
# def choosing_difficulty():
#    level = input("choose a difficulty level! type 1 for easy, 2 for medium and 3 for hard")
#    if level.isdigit and int(level)>0 and int(level)<4:
#       if int(level)==1:
#          word_list=["light, might, white, flake, poise, noise, voice, vocal, abode, chase, cabin, right, focal, focus, train, waste, eight, yacht, adopt, crate, sedan, paste, paint, faint, whale, quail, image, zebra, brave, crave, dream, steam, stare, flare, great, shale, frail, grail, night, sight, fight, chain, break, brake, trace, satin, haste, urban, eland, extra, hover, cover, lover"]
#       elif int(level)==2:
#          word_list=["absent,absurd,adjust, admire,admits, backed,backer, backup,dancer, dances, danger,garden, garish, garlic,scrape, scrawl, screak, scream, screwy, scribe"]
#       elif int(level)==3:
#          word_list=["amplify, quality, voyager, angrily, stranger, crowned, elastic, dialect, naively, zealous, website, network, healthy, section, working, donate, plastic, journal, friends, caption, kingdom, quickly, journey, tangled, history, auction, natural, therapy, justice, century, variety, virtual, anxiety, imagine, company, payment, tonight, upgrade, picture, organic, product, quality, anxious, kitchen, protein, victory, student, mystery, liberty"]
#    else:
#       print("type again")
#       choosing_difficulty()
#    return word_list
# def hangman_game():
#    print('Hello! You are playing Hangman!')
#    tries=10
#    for cycle in range(0, tries + len(blank) - 1):
#       a = input("Guess a letter")
#       if a in letters:
#          place = word.find(a)
#          blank.pop(place)
#          blank.insert(place, a)
#          print('You guessed right!', ''.join(blank))
#          if "_" not in blank:
#             print("You've won! The word is", word)
#             break
#       else:
#          tries -= 1
#          if tries == 0:
#             print("You've made a mistake! You've lost!")
#             break
#          else:
#             print("You've made a mistake! You have", tries, "tries left.", ''.join(blank))
# def play_again():
#    a=input("Do you want to play again? If yes type 1, if no type 2")
#    if a.isdigit and int(a)>0 and int(a)<3:
#       if int(a)==1:
#          hangman_game()
#       if int(a)==2:
#          print ("Thank you for playing!")
# def processing():
#    words=choosing_difficulty()
#    words= words[0].split(',')
#    word = random.choice(words)
#    print(word)
#    if word.startswith(" ")==True:
#       word= word.replace(" ", "")
#    letters=[]
#    letters[:0]=word
#    quesses=[]
#    blank="_"*len(letters)
#    blank=list(blank)
#    return blank
# words=choosing_difficulty()
# processing()
# hangman_game()
# play_again()

import random
import re


# def choosing_difficulty():
#    print('Hello! You are playing Hangman!')
#    level = input("choose a difficulty level! type 1 for easy, 2 for medium and 3 for hard")
#    if level.isdigit and int(level)>0 and int(level)<4:
#       if int(level)==1:
#          word_list=["light, might, white, flake, poise, noise, voice, vocal, abode, chase, cabin, right, focal, focus, train, waste, eight, yacht, adopt, crate, sedan, paste, paint, faint, whale, quail, image, zebra, brave, crave, dream, steam, stare, flare, great, shale, frail, grail, night, sight, fight, chain, break, brake, trace, satin, haste, urban, eland, extra, hover, cover, lover"]
#       elif int(level)==2:
#          word_list=["absent,absurd,adjust, admire,admits, backed,backer, backup,dancer, dances, danger,garden, garish, garlic,scrape, scrawl, screak, scream, screwy, scribe"]
#       elif int(level)==3:
#          word_list=["amplify, quality, voyager, angrily, stranger, crowned, elastic, dialect, naively, zealous, website, network, healthy, section, working, donate, plastic, journal, friends, caption, kingdom, quickly, journey, tangled, history, auction, natural, therapy, justice, century, variety, virtual, anxiety, imagine, company, payment, tonight, upgrade, picture, organic, product, quality, anxious, kitchen, protein, victory, student, mystery, liberty"]
#       words = word_list[0].split(',')
#       word = random.choice(words)
#       if word.startswith(" ") == True:
#          word = word.replace(" ", "")
#       letters[:0] = word
#    else:
#       print("type again")
#       choosing_difficulty()
#    return letters
#
# def hangman_game():
#    tries=10
#    while tries>0:
#       a = input("Guess a letter")
#       if a in letters:
#          place = letters.find(a)
#          blank.pop(place)
#          blank.insert(place, a)
#          print('You guessed right!', ''.join(blank))
#          if "_" not in blank:
#             print("You've won! The word is", hangman_word)
#             break
#       else:
#          tries -= 1
#          if tries == 0:
#             print("You've made a mistake! You've lost!")
#             break
#          else:
#             print("You've made a mistake! You have", tries, "tries left.", ''.join(blank))
#
# def play_again():
#    play=input("do you want to play again? if yes type 1. if no type 2")
#    if play.isdigit and int(play)>0 and int(play)<3:
#       if int(play)==1:
#          hangman_word_again=choosing_difficulty()
#          hangman_game()
#       elif int(play)==2:
#          print("Thank you for playing")
#    else:
#       print("please, type 1 for yes or 2 for no")
#       play_again()
#
# letters=[]
# # hangman_word=choosing_difficulty()
# # letters[:0]=hangman_word
# quesses=[]
# blank="_"*len(letters)
# blank=list(blank)
# choosing_difficulty()
# print(blank)
# print(letters)
# hangman_game()
# play_again()

word_list = {1: "light, might, white, flake, poise, noise, voice, vocal, abode, chase, cabin, right, focal, focus, train, "
                "waste, eight, yacht, adopt, crate, sedan, paste, paint, faint, whale, quail, image, zebra, brave, crave, "
                "dream, steam, stare, flare, great, shale, frail, grail, night, sight, fight, chain, break, brake, trace, "
                "satin, haste, urban, eland, extra, hover, cover, lover",
             2: "absent,absurd,adjust, admire,admits, backed, backer, backup,dancer, dances, danger,garden, garish, garlic,"
                "scrape, scrawl, screak, scream, screwy, scribe",
             3: "amplify, quality, voyager, angrily, stranger, crowned, elastic, dialect, naively, zealous, website, network, "
                "healthy, section, working, donate, plastic, journal, friends, caption, kingdom, quickly, journey, tangled, "
                "history, auction, natural, therapy, justice, century, variety, virtual, anxiety, imagine, company, payment, "
                "tonight, upgrade, picture, organic, product, quality, anxious, kitchen, protein, victory, student, "
                "mystery, liberty"}

def difficulty():
   print('You are playing Hangman!')
   level = int(input("Choose a difficulty level! type 1 for easy, 2 for medium and 3 for hard"))
   words = word_list.get(level)
   words=words.split(",")
   return words

words = difficulty()

def choose_word():
      word = random.choice(words)
      if word.startswith(" ") == True:
         word = word.replace(" ", "")
      letters=[]
      letters[1:0] = word
      return letters, word

letters, word = choose_word()
blank="_"*len(letters)
blank=list(blank)
print(letters, word)
def hangman_game():
    tries=10
    while tries>0:
          letter = input("Guess a letter")
          if letter in letters:
             place = word.find(letter)
             blank.pop(place)
             blank.insert(place, letter)
             print('You guessed right!', ''.join(blank))
             if "_" not in blank:
                print("You've won! The word is", word)
                break
          else:
             tries -= 1
             if tries == 0:
                print("You've made a mistake! You've lost!")
                break
             else:
                print("You've made a mistake! You have", tries, "tries left.", ''.join(blank))

hangman_game()