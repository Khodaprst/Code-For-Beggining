with open ('my_text.txt', 'r') as ReadFile:
    with open('mine_text.txt', 'w') as WriteFile:
        for line in ReadFile:
            WriteFile.write(line)

    