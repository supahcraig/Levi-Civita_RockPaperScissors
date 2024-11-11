import random
import time

choices = [0, 1, 2]
weapons = ['rock', 'paper', 'scissors']

while True:
    p1 = random.randint(0, 2)
    p2 = random.randint(0, 2)

    print(f'Player 1 has chosen {weapons[p1]}, Player 2 has chosen {weapons[p2]}....')

    # if players have made different choices
    #   then the 3rd index is just whatever choice hadn't already been made
    # if they have chosen the same item then the 3rd choice doesn't even matter, just pick an unused choice
    # in either case, the k-index is never actually needed.
    k_index = list(set(choices) - set([p1, p2]))[0]


    # Levi-Civita is +1 for even permutations, -1 for odd permutations, and 0 if there is a repeated index
    r = LeviCivita(p1, p2, k_index)
    if r == 0:
        print(f"It's a draw; both players picked {weapons[p1]}")
    elif r < 0:
        print(f'Player 1 wins; {weapons[p1]} defeats {weapons[p2]}')
    elif r > 0:
        print(f'Player 2 wins; {weapons[p2]} defeats {weapons[p1]}')

    print('-' * 10)

    time.sleep(3)
