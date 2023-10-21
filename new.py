import random

def get_user_input(prompt):
    while True:
        try:
            user = int(input(prompt))
            if user > 0:
                return user
            else:
                print("negative_integer")
        except ValueError:
            print("enter a valid input!")

def main():
    print("welcme_to_the_game>>> ")
    num = get_user_input("chose a number ")
    gen_num = random.randint(1, num)

    attempts = 0
    while True:
        guess = get_user_input("guess_THE_number (1 - {}): ".format(num))
        attempts += 1

        if guess > gen_num:
            print("greater_than THE NUMBER")
        elif guess < gen_num:
            print("less_than THE NUMBER")
        else:
            print("CORRECT !")
            break

if __name__ == "__main__":
    main()