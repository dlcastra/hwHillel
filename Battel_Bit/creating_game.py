import random


def start():
    class Archer:

        def __init__(self):
            self.heals = 100
            self.armor = 30
            self.damage = random.randint(30, 40)

    class Wither:

        def __init__(self):
            self.heals = 100
            self.armor = 20
            self.damage = random.randint(20, 45)

    class Knight:

        def __init__(self):
            self.heals = 100
            self.armor = 20
            self.damage = random.randint(40, 50)

    def creating_fight():
        class Army:
            blue_team = []
            red_team = []

        iteration = int(input("How many units you want create?\n""I want: "))
        count = 0
        count_iter = iteration

        while count < count_iter + 1:
            count += 1

            def creating_first_team():
                first_team = Army.blue_team
                second_team = Army.red_team

                r = random.randint(1, 3)
                (
                    first_team.append(Archer()) if r == 3

                    else first_team.append(Wither()) if r == 2

                    else first_team.append(Knight())
                )

                (
                    second_team.append(Archer()) if r == 3

                    else second_team.append(Wither()) if r == 2

                    else second_team.append(Knight())
                )

        def fight():
            pass

            creating_first_team()

    creating_fight()


start()
