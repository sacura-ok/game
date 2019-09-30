#!/usr/bin/env python3

import random

HEALTH = 100
LIST_STEPS = ['Medium damage', 'Big damage', 'Heal']


class Member:
    # class for creating members, which upon initialization takes the name of the participant and the amount of health

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __str__(self):
        return f'{self.name} - {self.health}'

    def get_damage(self, amount, step):
        # method that does amount of damage and checks the health of the member
        self.health -= amount
        print(f' - Member {self.name} {LIST_STEPS[step - 1]} done: {amount}')
        if self.health <= 0:
            print(f'Member {self.name} lost the game')
            self.health = False

    def heal(self, amount, step):
        # heals the member on amount if his health is less than 35%
        if self.health < HEALTH * 35 / 100:
            self.health += amount
            print(f' - {LIST_STEPS[step - 1]} {self.name} on {amount}')

    def is_alive(self):
        if self.health:
            return True
        else:
            return False


def damage(player, amount, step):
    print(f'Members health: {player1.__str__()}, {player2.__str__()}')
    player.get_damage(amount, step)
    if player.is_alive():
        random_move()


def random_step(player):
    # randomly selects a step:
    #  1 - deals damage of a small range
    #  2 - deals damage of a large range
    #  3 - heals in a small range
    step = random.randint(1, 3)
    if step == 1:
        damage(player, random.randint(18, 25), step)
    elif step == 2:
        damage(player, random.randint(10, 35), step)
    else:
        if player.is_alive():
            player.heal(random.randint(18, 25), step)
            random_move()


def random_move():
    # Random choise player
    if random.randint(1, 2) == 1:
        random_step(player2)
    else:
        random_step(player1)


if __name__ == '__main__':
    player1 = Member('Computer', HEALTH)
    player2 = Member('Player', HEALTH)
    random_move()
