def chanch_string():
    text = open("16.txt", "r")
    text_write = open("res.txt", "w+")
    count = 0
    maximum = 0
    max_i = 0
    for lines in text:
        print(lines, end='')
        for i in range(len(lines)):
            if lines[i] == " ":
                if count > maximum:
                    maximum = count
                    max_i = i - count
                count = 0
            count += 1

        for i in range(max_i, maximum):
            if lines[i] == 'o':
                lines = lines.replace('o', 'y')
            if lines[i] == 'i':
                lines = lines.replace('i', 'j')
        print(lines, end='')
        text_write.write(lines)

    text_write.close()
    text.close()

chanch_string()