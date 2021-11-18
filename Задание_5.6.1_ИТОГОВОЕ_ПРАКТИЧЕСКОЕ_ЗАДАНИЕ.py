pass_symbol = "x"
list_head = ["  ", 0, 1, 2]
line = [0, "-", "-", "-", "\n", 1, "-", "-", "-", "\n", 2, "-", "-", "-"]
print(*list_head, "\n", *line)


def winner(check_element):
    list_of_winner = [1] + [i for i in range(4, 7)]
    for k in list_of_winner:
        if k == 1:
            for n in range(len(line) - 2):
                if check_element == line[n] and check_element == line[n + k] and check_element == line[n + k * 2]:
                    return True
        elif k == 4:
            n = 3
            if check_element == line[n] and check_element == line[n + k] and check_element == line[n + k * 2]:
                return True
        elif k == 5:
            for n in range(4):
                if check_element == line[n] and check_element == line[n + k] and check_element == line[n + k * 2]:
                    return True
        elif k == 6:
            n = 1
            if check_element == line[n] and check_element == line[n + k] and check_element == line[n + k * 2]:
                return True


while True:
    coordinata_y = int(input("Select one number on the VERTICAL (Y) axis-->"))
    coordinata_x = int(input("Select one number on the HORIZONTAL (X) axis-->"))
    x = coordinata_y * 5 + coordinata_x + 1

    if not (0 <= coordinata_y <= 2) or not (0 <= coordinata_x <= 2):
        print("Number not in diapason")
        continue
    elif line[x] == "x" or line[x] == "o":
        print("Choose empty space")
        continue

    line[x] = pass_symbol
    print(*list_head, "\n", *line)

    if winner(pass_symbol):
        print("Game Over\nWinner--> " + pass_symbol)
        break
    elif "-" not in line:
        print("Draw")
        break
    elif pass_symbol == "x":
        pass_symbol = "o"
    else:
        pass_symbol = "x"
