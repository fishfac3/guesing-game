import random


def main():
    # Prompt user for level n
    try:
        number = prompt_level()
        if number < 1:
            raise ValueError
        # Generate random number between 1 and n
        rand_num = random_num(number)
        #print(rand_num)
        # prompt user to guess number ("Guess: ")
        guess_num = prompt_guess()
        # Validate user guess_num
        guess(rand_num, guess_num)
    except ValueError:
        number = prompt_level()


def guess(rand_num, guess_num):
    # if guess < random number ("Too small!")
    if rand_num > guess_num:
        print("Too small!")
        guess(rand_num, prompt_guess())
    # elif number > random number ("Too large!")
    elif rand_num < guess_num:
        print("Too large!")
        guess(rand_num ,prompt_guess())
    # else ("Just right!")
    elif rand_num == guess_num:
        print("Just right!")
        quit()


def prompt_guess():
    try:
        return int(input("Guess: "))
    except ValueError:
        prompt_guess()


def prompt_level():
    try:
        return int(input("Level: "))
    except ValueError:
        prompt_level()


def random_num(num):
    return random.randint(1, num)


if __name__ == "__main__":
    main()


