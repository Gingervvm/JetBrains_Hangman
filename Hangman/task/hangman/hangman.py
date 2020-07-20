import random


print("H A N G M A N")
while True:
    menu_item = input('Type "play" to play the game, "exit" to quit:')
    if menu_item == "play":
        words_list = ["python", "java", "kotlin", "javascript"]
        correct_word = random.choice(words_list)
        input_letters = set()
        word_letters = set(correct_word)
        i = 1
        while i <= 8:
            print()
            word_to_print = ""
            for char in correct_word:
                if char in input_letters:
                    word_to_print = word_to_print + char
                else:
                    word_to_print = word_to_print + "-"
            print(word_to_print)
            input_letter = input("Input a letter: ")
            if len(input_letter) != 1:
                print("You should input a single letter")
                continue
            if not input_letter.islower() or not input_letter.isascii():
                print("It is not an ASCII lowercase letter")
                continue
            if input_letter in input_letters:
                print("You already typed this letter")
                continue
            elif input_letter in word_letters and input_letter not in input_letters:
                input_letters.add(input_letter)
                if word_letters.issubset(input_letters):
                    print(f"You guessed the word {correct_word}!")
                    print("You survived!\n")
                    break
                continue
            input_letters.add(input_letter)
            print("No such letter in the word")
            i += 1
        else:
            print("You are hanged!\n")
        continue
    elif menu_item == "exit":
        break
    else:
        continue
