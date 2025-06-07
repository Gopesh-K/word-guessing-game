import random

def main():
    print("🎮 Welcome to the AI Word Guessing Game! 🎮")
    print("I'll think of a word and give you AI-powered hints!")
    print("-" * 50)
    
    # List of words to guess
    words = ["python", "computer", "rainbow", "elephant", "mountain", 
             "ocean", "guitar", "butterfly", "volcano", "library",
             "chocolate", "adventure", "sunshine", "keyboard", "dragon"]
    
    # Pick a random word
    secret_word = random.choice(words)
    word_length = len(secret_word)
    
    # Create display word with dashes
    guessed_word = ["_"] * word_length
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6
    
    print(f"The word has {word_length} letters: {' '.join(guessed_word)}")
    print(f"You have {max_wrong} wrong guesses allowed.")
    
    # Game loop
    while wrong_guesses < max_wrong and "_" in guessed_word:
        print("\n" + "=" * 40)
        print(f"Word: {' '.join(guessed_word)}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
        
        # Get user input
        choice = input("\nEnter 'h' for AI hint, or guess a letter: ").lower().strip()
        
        # Handle hint
        if choice == 'h':
            print("\n🤖 Getting hint...")
            hint = get_hint(secret_word)
            print(f"💡 Hint: {hint}")
            continue
        
        # Validate input
        if len(choice) != 1 or not choice.isalpha():
            print("❌ Please enter a single letter!")
            continue
        
        if choice in guessed_letters:
            print("❌ You already guessed that letter!")
            continue
        
        # Add to guessed letters
        guessed_letters.append(choice)
        
        # Check if letter is in word
        if choice in secret_word:
            print(f"✅ Great! '{choice}' is in the word!")
            # Update display word
            for i in range(word_length):
                if secret_word[i] == choice:
                    guessed_word[i] = choice
        else:
            wrong_guesses += 1
            print(f"❌ Sorry, '{choice}' is not in the word.")
            draw_hangman(wrong_guesses)
    
    # Game over - check if won or lost
    print("\n" + "=" * 50)
    if "_" not in guessed_word:
        print("🎉 CONGRATULATIONS! You guessed the word!")
        print(f"The word was: {secret_word.upper()}")
        celebrate_win()
    else:
        print("💀 Game Over! You ran out of guesses.")
        print(f"The word was: {secret_word.upper()}")
        print("Better luck next time!")
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    if play_again == 'y' or play_again == 'yes':
        print("\n" * 3)
        main()  # Start a new game
    else:
        print("Thanks for playing! 👋")

def get_hint(word):
    """Get a helpful hint for the word"""
    hints = {
        "python": "A programming language named after a comedy group, or a large snake! 🐍",
        "computer": "An electronic device you're probably using right now! 💻",
        "rainbow": "You see this colorful arc in the sky after rain! 🌈",
        "elephant": "The largest land animal with a long trunk! 🐘",
        "mountain": "A tall natural elevation of the earth's surface! ⛰️",
        "ocean": "A vast body of salt water covering most of Earth! 🌊",
        "guitar": "A stringed musical instrument you can strum! 🎸",
        "butterfly": "A colorful flying insect that starts as a caterpillar! 🦋",
        "volcano": "A mountain that can erupt with hot lava! 🌋",
        "library": "A quiet place full of books and knowledge! 📚",
        "chocolate": "A sweet treat that melts in your mouth! 🍫",
        "adventure": "An exciting journey or experience! ⚔️",
        "sunshine": "Bright light and warmth from our star! ☀️",
        "keyboard": "You use this to type letters and numbers! ⌨️",
        "dragon": "A mythical fire-breathing creature from legends! 🐲"
    }
    
    return hints.get(word, "This is a really cool word! Keep guessing! 🤔")

def draw_hangman(wrong_count):
    """Draw simple hangman ASCII art"""
    stages = [
        "",
        "  +---+\n      |\n      |\n      |\n      |\n  =========",
        "  +---+\n  |   |\n      |\n      |\n      |\n  =========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n  =========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n  =========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n  =========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n  =========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n  =========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n  ========="
    ]
    
    if wrong_count < len(stages):
        print(stages[wrong_count])

def celebrate_win():
    """Simple celebration animation"""
    print("🎊 🎉 🎊 🎉 🎊 🎉 🎊")
    print("   YOU'RE AMAZING!   ")
    print("🎊 🎉 🎊 🎉 🎊 🎉 🎊")

if __name__ == '__main__':
    main()