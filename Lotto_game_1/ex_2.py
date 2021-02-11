from random import randint
def user_input():
    """
    get a number from the user and check if it is correct
    :rtype: list
    :return: a list of sorted numbers chosen by user
    """
    list = []
    while len(list) < 6:
        user_num = input("Insert a number from 1 to 49:")
        try:
            user_num = int(user_num)
            if user_num not in list and user_num > 0 and user_num <= 49:
                list.append(user_num)
            else:
                print("This is not a number from 1 to 49! Insert a correct one!")
        except ValueError:
            print("This is not a number! Insert a number from 1 to 49!")
    return sorted(list)

def winning_numbers():
    """
    draw 6 winning random different numbers
    :rtype: list
    :return: a list of sorted numbers chosen by the computer
    """
    winning_list = []
    while len(winning_list) < 6:
        draw = randint(1, 49)
        if draw not in winning_list:
            winning_list.append(draw)
    return sorted(winning_list)

def results():
    """ main function of the program """
    winning = winning_numbers()
    users = user_input()
    print(f"Your numbers:{users}")
    print(f"Winning number:{winning}")
    score = 0
    for number in users:
        if number in winning:
            score += 1
    print(score)
    if score == 1 or score == 2:
        print(f"Sorry your score is {score}")
    elif score == 3 or score == 4 or score == 5:
        print(f"Congratulations your score is {score}")
    elif score == 6:
        print(f"Congratulations, You win!!")



if __name__ == '__main__':
    results()

