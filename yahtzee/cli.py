import random


def main():
    roll = new_roll()
    print('%d %d %d %d %d' % tuple(roll))
    keepers_positions = input('What positions do you want to keep?')


def new_roll():
    return random.choices(range(1,7), k=5)


if __name__ == '__main__':
    main()
