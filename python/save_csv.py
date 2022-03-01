import csv

def save_csv(data="",path="",mode="w"):
    path=(str(path).strip()).lower()
    mode=(str(mode).strip()).lower()
    msg=""
    if type(data)==list:
        
        if type(data[0])==list:
            with open(path, mode, newline='') as file:
                
                #writer = csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=';')
                writer = csv.writer(file,delimiter=';')
                writer.writerows(data) ### all list
            file.close()
            return msg + "  list to list"
        else:
            with open(path, mode, newline='') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,delimiter=';')
                #writer = csv.writer(file, delimiter=';')
                writer.writerow(data) ### one 1list
            file.close()
            return msg + "  one list"
    else:
        if type(data)==str:
            data=[str(data)]
            with open(path, mode,newline='') as file:
                
                writer = csv.writer(file, quoting=csv.QUOTE_NONE,delimiter=';')
                #writer = csv.writer(file,delimiter=';')
                writer.writerow(data) ### one str
            file.close()
            return msg + "  on str"
#ss="hello"
#ss=[1,2,3,4]
ss=[[1,2,3,4],[111,"aa"]]


save_csv(ss,"test.csv","w")

