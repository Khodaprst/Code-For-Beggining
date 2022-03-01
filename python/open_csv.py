import csv

def open_csv(path=""):
    try:
        path=(str(path).strip()).lower()
        msg=""
        with open (path) as file:
            reader = csv.reader(file, quoting=csv.QUOTE_ALL,delimiter=';')
            check_true=True
            data=[]
            n_list=0
            for i in range (2):
                try:
                    test1=(next(reader))
                    n_list=n_list+1
                except:
                    pass
                
            file.close()
        with open (path) as file:
            reader = csv.reader(file, quoting=csv.QUOTE_ALL,delimiter=';')
            while check_true==True:
                try:
                    if n_list>1:
                        data.append(next(reader))
                    else:
                        data=next(reader)
                except:
                    check_true=False
                
            file.close()
        return data
    except:
        print( "csv File not found to read" )

a=open_csv("test.csv")
print(a)

