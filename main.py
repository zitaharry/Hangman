#Step 1 
import random
from hangman_art import logo, stages 
from hangman_art import welcome
from hangman_art import logo

print(welcome)
print(logo)

word_list = [
    'abruptly', 
    'absurd', 
    'abyss', 
    'affix', 
    'askew', 
    'avenue', 
    'awkward', 
    'axiom', 
    'azure', 
    'bagpipes', 
    'bandwagon', 
    'banjo', 
    'bayou', 
    'beekeeper', 
    'bikini', 
    'blitz', 
    'blizzard', 
    'boggle', 
    'bookworm', 
    'boxcar', 
    'boxful', 
    'buckaroo', 
    'buffalo', 
    'buffoon', 
    'buxom', 
    'buzzard', 
    'buzzing', 
    'buzzwords', 
    'caliph', 
    'cobweb', 
    'cockiness', 
    'croquet', 
    'crypt', 
    'curacao', 
    'cycle', 
    'daiquiri', 
    'dirndl', 
    'disavow', 
    'dizzying', 
    'duplex', 
    'dwarves', 
    'embezzle', 
    'equip', 
    'espionage', 
    'euouae', 
    'exodus', 
    'faking', 
    'fishhook', 
    'fixable', 
    'fjord', 
    'flapjack', 
    'flopping', 
    'fluffiness', 
    'flyby', 
    'foxglove', 
    'frazzled', 
    'frizzled', 
    'fuchsia', 
    'funny', 
    'gabby', 
    'galaxy', 
    'galvanize', 
    'gazebo', 
    'giaour', 
    'gizmo', 
    'glowworm', 
    'glyph', 
    'gnarly', 
    'gnostic', 
    'gossip', 
    'grogginess', 
    'haiku', 
    'haphazard', 
    'hyphen', 
    'iatrogenic', 
    'icebox', 
    'injury', 
    'ivory', 
    'ivy', 
    'jackpot', 
    'jaundice', 
    'jawbreaker', 
    'jaywalk', 
    'jazziest', 
    'jazzy', 
    'jelly', 
    'jigsaw', 
    'jinx', 
    'jiujitsu', 
    'jockey', 
    'jogging', 
    'joking', 
    'jovial', 
    'joyful', 
    'juicy', 
    'jukebox', 
    'jumbo', 
    'kayak', 
    'kazoo', 
    'keyhole', 
    'khaki', 
    'kilobyte', 
    'kiosk', 
    'kitsch', 
    'kiwifruit', 
    'klutz', 
    'knapsack', 
    'larynx', 
    'lengths', 
    'lucky', 
    'luxury', 
    'lymph', 
    'marquis', 
    'matrix', 
    'megahertz', 
    'microwave', 
    'mnemonic', 
    'mystify', 
    'naphtha', 
    'nightclub', 
    'nowadays', 
    'numbskull', 
    'nymph', 
    'onyx', 
    'ovary', 
    'oxidize', 
    'oxygen', 
    'pajama', 
    'peekaboo', 
    'phlegm', 
    'pixel', 
    'pizazz', 
    'pneumonia', 
    'polka', 
    'pshaw', 
    'psyche', 
    'puppy', 
    'puzzling', 
    'quartz', 
    'queue', 
    'quips', 
    'quixotic', 
    'quiz', 
    'quizzes', 
    'quorum', 
    'razzmatazz', 
    'rhubarb', 
    'rhythm', 
    'rickshaw', 
    'schnapps', 
    'scratch', 
    'shiv', 
    'snazzy', 
    'sphinx', 
    'spritz', 
    'squawk', 
    'staff', 
    'strength', 
    'strengths', 
    'stretch', 
    'stronghold', 
    'stymied', 
    'subway', 
    'swivel', 
    'syndrome', 
    'thriftless', 
    'thumbscrew', 
    'topaz', 
    'transcript', 
    'transgress', 
    'transplant', 
    'triphthong', 
    'twelfth', 
    'twelfths', 
    'unknown', 
    'unworthy', 
    'unzip', 
    'uptown', 
    'vaporize', 
    'vixen', 
    'vodka', 
    'voodoo', 
    'vortex', 
    'voyeurism', 
    'walkway', 
    'waltz', 
    'wave', 
    'wavy', 
    'waxy', 
    'wellspring', 
    'wheezy', 
    'whiskey', 
    'whizzing', 
    'whomever', 
    'wimpy', 
    'witchcraft', 
    'wizard', 
    'woozy', 
    'wristwatch', 
    'wyvern', 
    'xylophone', 
    'yachtsman', 
    'yippee', 
    'yoked', 
    'youthful', 
    'yummy', 
    'zephyr', 
    'zigzag', 
    'zigzagging', 
    'zilch', 
    'zipper', 
    'zodiac', 
    'zombie',
]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
# print(f"Psst, the solution is {chosen_word}.")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


#Step 2
#TODO-1: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    print(display)

#Step 3
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

            if guess in display:
                lives -= 1
                print(f"You've already guessed {guess}")
                if lives == 0:
                    end_of_game = True
                    print("You lose.")

    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])