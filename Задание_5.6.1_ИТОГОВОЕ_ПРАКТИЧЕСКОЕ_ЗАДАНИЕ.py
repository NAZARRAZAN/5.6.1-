pass_symbol = "x"
list_ = ["  ", 0, 1, 2]
line = [0, "-", "-", "-","\n", 1, "-", "-", "-","\n", 2, "-", "-", "-"]
print(*list_, "\n", *line)


def winner(check_element):
    list_of_winner = [1] + [i for i in range(4, 7)]
    for k in list_of_winner:
        if k == 1:
            for n in range(len(line) - 2):
                if check_element == line[n] and check_element == line[n + k] and check_element == line[n + k * 2]:
                    return True
        if k == 4:
            n = 3
            if check_element == line[n] and check_element == line[n + k] and check_element == line[n + k * 2]:
                return True
        if k == 5:
            for n in range(4):
                if check_element == line[n] and check_element == line[n + k] and check_element == line[n + k * 2]:
                    return True
        if k == 6:
            n = 1
            if check_element == line[n] and check_element == line[n + k] and check_element == line[n + k * 2]:
                return True





while True:
    position = list(map(int, input("print two number from 0 to 2-->").split()))


    if len(position) > 2:
        print("Too much numbers")
        continue
    elif position[0] > 2  or position[1] >  2 or position[0] < 0  or position[1] < 0:
        print("Number not in diapason")
        continue

    x = line.index(position[0]) + position[1] + 1

    if line[x] == "x" or line[x] == "o":
        print("Choose empty space")
        continue

    line[x] = pass_symbol
    print(*list_, "\n", *line)

    if winner(pass_symbol):
        print("Game Over\nWinner--> " + pass_symbol)
        break
    elif not "-" in line:
        print("Draw")
        break

    if pass_symbol == "x":
        pass_symbol = "o"
    else:
        pass_symbol = "x"