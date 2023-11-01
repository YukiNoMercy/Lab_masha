text = open("16.txt", "r")
count = 0
maximum = 0
max_i = 0
for lines in text:
    for i in range(len(lines)):
        if lines[i] == " ":
            if count > maximum:
                maximum = count
                max_i = i - count
        count += 1
text.close()