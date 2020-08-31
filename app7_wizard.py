import random
import time

from app7_actorsclass import Wizard, Creature, SmallAnimal, Dragon, Matija


def main():
    print_header()
    game_loop()


def print_header():
    print('----------------------')
    print('\t WIZARD BATTLE!')
    print('----------------------')
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Fire Dragon', 50, 75, True),
        Dragon('Whelp', 50, 25, False),
        Wizard('Evil Wizard!', 100),


    ]
    # print(creatures)
    hero = Wizard('Gandolf style', 100)
    antihero = Matija('MacHiNe LEArniNg pRoGrammEr', 666)

    while creatures:

        active_creature = random.choice(creatures)
        print(f"A {active_creature.name} of level {active_creature.level} has appeared from dark foggy forest...")
        print()

        cmd = input("Do you [a]ttack, [r]unaway, or [l]ook around? ").lower()

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(2)
                print("The wizard returns revitalized!")

        elif cmd == 'r':
            print('psycho killer...runawaaaaay!')
        elif cmd == 'l':
            print(f"The wizard Opa - {hero.name} of level {hero.level} takes in the surroundings and sees: ")
            for c in creatures:
                print(f" * A {c.name} of level {c.level}")
        else:
            print("OK, exiting game.... bye!")
            break

        if not creatures:
            print("THE SECRET BOSS APPEARS.")
            print(antihero)
            roll, command = antihero.get_defensive_roll()
            if command == 'continue':
                print('FUCK YOU ' * 69)
            elif command == 'break':
                break


if __name__ == '__main__':
    main()
