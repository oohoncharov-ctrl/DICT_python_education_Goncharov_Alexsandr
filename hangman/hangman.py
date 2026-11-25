import random

def play_hangman():
    print("H A N G M A N")
    words = ['python', 'java', 'javascript', 'php']
    word = random.choice(words)
    hidden_word = list('-' * len(word))
    guessed_letters = set()
    attempts = 8

    while attempts > 0:
        print()
        print(''.join(hidden_word))
        guess = input("Input a letter: ")
        
        if len(guess) != 1:
            print("Please, input a single letter.")
            continue
            
        if not guess.islower() or not guess.isalpha():
            print("Please, enter a lowercase English letter.")
            continue
            
        if guess in guessed_letters:
            print("You've already guessed this letter.")
            continue
            
        guessed_letters.add(guess)
        
        if guess in word:
            improved = False
            for i, letter in enumerate(word):
                if letter == guess and hidden_word[i] == '-':
                    hidden_word[i] = guess
                    improved = True
            
            if '-' not in hidden_word:
                print()
                print(''.join(hidden_word))
                print(f"You guessed the word {word}!")
                print("You survived!")
                return
        else:
            print("That letter doesn't appear in the word.")
            attempts -= 1

    print("You lost!")

if __name__ == "__main__":
    play_hangman()
