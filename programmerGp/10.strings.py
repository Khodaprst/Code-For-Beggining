def char(kalame):
    nu = 0
    for words in kalame[:4]:
        if words.upper() in words:
            nu += 1
            print('%d mored Okeye, ' %nu, end= ' ')
        
    if nu >= 2:
        return kalame.upper()
    else:
            return kalame
    
print(char('AmiRhossein'))