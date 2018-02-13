import random

coub = {1: """
            *******
            *     *
            *  0  *
            *     *
            *******
            """,
        2: """
            *******
            * 0   *
            *     *
            *   0 *
            *******
            """,
        3: """
            *******
            *0    *
            *  0  *
            *    0*
            *******
            """,
        4: """
            *******
            * 0 0 *
            *     *
            * 0 0 *
            *******
            """,
        5: """
            *******
            * 0 0 *
            *  0  *
            * 0 0 *
            *******
            """,
        6: """
            *******
            * 0 0 *
            * 0 0 *
            * 0 0 *
            *******
            """
        }


# coub = (1, 2, 3, 4, 5, 6)


def greating():
    print("Hello!")


def cast():
    return random.randint(1, 6)


def get_player_name():
    result = []
    while True:
        name = input("Enter your name, please: ")
        if not name.strip():
            break
        result.append(name)
    return result


def start_game():
    greating()
    players = get_player_name()
    repeats = int(input("Write number of attempts: "))
    count_bones = int(input("Write number of bones: "))
    for q in range(repeats):

        for player in players:
            input("{} Press enter for cast".format(player))
            for z in range(count_bones):
                print(cast(), end=' ')
            print(player)


if __name__ == '__main__':
    start_game()
