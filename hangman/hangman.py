import random

def play_hangman():
    words = ['python', 'java', 'javascript', 'php']
    word = random.choice(words)
    hidden_word = ['-', '-'] * (len(word) // 2) + ['-'] * (len(word) % 2) # or simply ['-' for _ in word]
    hidden_word = list('-' * len(word))
    
    attempts = 8
    guessed_letters = set()
    
    while attempts > 0:
        print()
        print(''.join(hidden_word))
        guess = input("Input a letter:\n> ")
        
        if len(guess) != 1:
            print("You should input a single letter")
            continue
            
        if not guess.islower() or not guess.isalpha():
            print("Please enter a lowercase English letter")
            continue
            
        if guess in guessed_letters:
            print("You've already guessed this letter")
            continue
            
        guessed_letters.add(guess)
        
        if guess in word:
            # Check if it actually improved the word or if it's new
            # In Stage 5/6/7, if guess is in word, we reveal it.
            improved = False
            for i, letter in enumerate(word):
                if letter == guess and hidden_word[i] == '-':
                    hidden_word[i] = guess
                    improved = True
            
            # If all letters guessed
            if '-' not in hidden_word:
                print()
                print(''.join(hidden_word))
                print(f"You guessed the word {word}!")
                print("You survived!")
                return
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1
            
    print("You lost!")

def main():
    print("HANGMAN")
    while True:
        choice = input('Type "play" to play the game, "exit" to quit:\n> ').strip()
        if choice == "play":
            play_hangman()
            print()
        elif choice == "exit":
            break
        else:
            continue

if __name__ == "__main__":
    main()
