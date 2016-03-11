with open('greetings_utf8.txt', 'r', encoding='ascii', errors='ignore') as file:
    lines = file.readlines()
    line = ''
    for line in lines:
        print(line, end='')