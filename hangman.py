import random

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

def difficulty(level=1):
    with open('data/hangman_results.txt', 'r') as f:
        print(f.read())
    words = word_list.get(level)
    words = words.split(",")
    return words

def choose_word(words):
    word = random.choice(words)
    if word.startswith(" ") == True:
        word = word.replace(" ", "")
    letters=[]
    letters[1:0] = word
    return letters, word

def gameplay(letters, word, blank):
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
                    with open('data/hangman_results.txt', 'w') as f:
                        f.write(f'last result: win, word:{word}\n')
                    break
              else:
                 tries -= 1
                 if tries == 0:
                    print(f"You've made a mistake! You've lost! The word was {word}")
                    with open('data/hangman_results.txt', 'w') as f:
                        f.write(f'previous result: loss, word:{word}\n')
                    break
                 else:
                    print(f"You've made a mistake! You have {tries} tries left.", ''.join(blank))

def hangman_game():
    answer = input('If you want to play, type \'yes\'')
    if answer=='yes':
        level = int(input("Choose a difficulty level! type 1 for easy, 2 for medium and 3 for hard"))
        words = difficulty(level)
        letters, word = choose_word(words)
        blank = "_" * len(letters)
        blank = list(blank)
        gameplay(letters, word, blank)
        hangman_game()
    else:
        print('Thank you for playing')

with open('data/hangman_results.txt','w') as f:
    f.write("")
print('Welcome to Hangman!')
hangman_game()