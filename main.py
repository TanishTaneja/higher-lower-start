from art import logo, vs
from game_data import data
from random import randint
from replit import clear

SCORE = 0

#Game process using recursion
def game_process():
    random_a = randint(0, len(data) - 1)
    random_b = randint(0, len(data) - 1)

    def compare(following_a, following_b):
        if following_a > following_b:
            winner = following_a
        else:
            winner = following_b
        comparing_followers = str(input("Who has more followers? A or B\n"))

        if (comparing_followers == 'A'.lower() and winner == following_a or
                comparing_followers == 'B'.lower() and winner == following_b):

            global SCORE
            SCORE += 1
            clear()
            print(f"You got it right.Current score = {SCORE} ")

            game_process()
        else:
            print(f"You lose.Current score = {SCORE}")

    def random_data():
        char_a = data[random_a]
        char_b = data[random_b]

        print(logo)

        print(
            f"Compare A {char_a['name']}, {char_a['description']}, from {char_a['country']}."
        )

        print(vs)

        print(
            f"Against B {char_b['name']}, {char_b['description']},from {char_b['country']}."
        )

        compare(char_a['follower_count'], char_b['follower_count'])

    random_data()


game_process()
