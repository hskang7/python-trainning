with open('movie_quotes.txt', 'r') as file:    
    lines = file.readlines()
    line = ''
    for line in lines:
        print(line, end='')