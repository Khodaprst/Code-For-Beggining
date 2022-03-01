try:
    file = open('my_text.txt')
    
except(ModuleNotFoundError, FileNotFoundError) as e:
    print(e)

else:
    print(file.read())
    file.close()
    print('Done')