def change_file():
    text = open("16.txt", "r")
    text_write = open("res.txt", "w+")
    max_i = 0

    for lines in text:
        maximum = 0
        count = 0
        # print(lines, end='')
        for i in range(len(lines)):
            if lines[i] == " ":
                if count > maximum:
                    maximum = count
                    max_i = i - count
                count = 0
            count += 1

        for i in range(max_i, max_i + maximum):
            if lines[i] == 'o':
                lines = lines[:i] + 'y' + lines[i + 1 : ]
            if lines[i] == 'i':
                lines = lines[:i] + 'j' + lines[i + 1 : ]
        # print(lines)
        text_write.write(lines)
    # print("\n")
    text_write.close()
    text.close()

def numbers():
    text = open("int16.txt", "r")
    text_write = open("res.txt", "w+")

    temp_array = []
    for lines in text:
        s = ""
        # print(lines, end='')
        temp = lines.split()
        for i in temp:
            if int(i) % 2 == 0:
                temp_array.append(int(i))
    temp_array.sort(reverse=True)
    for i in temp_array:
        s += (str(i) + " ")
    # print("\n", s)
    text_write.write(s)


    text.close()
    text_write.close()
change_file() #Надо функции вызывать по очереди
numbers()