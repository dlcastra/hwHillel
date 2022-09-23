import random


# import math


class Archer:
    def __init__(self):
        self.name = Archer
        self.health = 100
        self.armor = 30
        self.damage = random.randint(30, 40)
        # self.damage = random.randint(150,200)


class Wither:
    def __init__(self):
        self.name = Wither
        self.health = 100
        self.armor = 20
        self.damage = random.randint(20, 45)
        # self.damage = random.randint(150, 200)

class Knight:
    def __init__(self):
        self.name = Knight
        self.health = 100
        self.armor = 40
        self.damage = random.randint(40, 50)
        # self.damage = random.randint(150, 200)

class Army:
    units = [Archer, Wither, Knight]

    def __init__(self, units, army_name):
        self.team: list = [
            random.choice(self.units)()
            for unit in range(units)
        ]

        self.name = army_name
        print(self.team)

    def attack(self, target):
        index_attacker = random.randint(0, len(self.team) - 1)
        index_target = random.randint(0, len(target.team) - 1)

        target_obj = target.team.pop(index_target)
        attacker_obj = self.team.pop(index_attacker)
        attack = attacker_obj.damage

        target_obj.health = target_obj.health
        attacker_obj.health = attacker_obj.health


        # shows the state of the target
        print(
            f"{target_obj.name}",
            f"Health: {target_obj.health}",
            f"Damage: {target_obj.damage}"
        )

        # shows the state of the attacker
        print(
            f"{attacker_obj.name}",
            f"Health: {attacker_obj.health}",
            f"Damage: {attacker_obj.damage}"
        )

        if target_obj.armor == 20:  # 40 * 0.85 == 34
            target_obj.health -= (attack * 0.85)

        elif target_obj.armor == 30:  # 40 * 0.75 == 30
            target_obj.health -= (attack * 0.75)

        elif target_obj.armor == 40:  # 40 * 0.7 == 28
            target_obj.health -= (attack * 0.7)

        if target_obj.health > 0:
            target.team.append(target_obj)
            print(f'Target get damage: {attack}\n')

        else:
            print('Unit dead\n')


def fight():
    units = int(input("How many units you want create?\n""I want: "))
    # units = 3
    red_army = Army(units, 'red_army')
    blue_army = Army(units, 'blue_army')

    while len(red_army.team) or len(blue_army.team) != 0:
        r = random.randint(10,100)

        if r % 2 == 1:
            red_army.attack(blue_army)

        elif r % 2 == 0:
            blue_army.attack(red_army)

        if not (red_army.team and blue_army.team):
            break

        if r % 2 == 0:
            blue_army.attack(red_army)

        elif r % 2 == 1:
            red_army.attack(blue_army)

    print(
        f"{red_army.name if red_army.team else blue_army.name}".title(),
        f"IS WON!!!"
    )


fight()
