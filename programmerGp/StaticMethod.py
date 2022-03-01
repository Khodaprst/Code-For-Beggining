class MyMath:
    @staticmethod
    def AddNum(x, y):
       return x + y
print(MyMath.AddNum(6, 6))
#--------------------------------------------------------
class Dates:
    def DashDate(date):
        return date.replace('/', '-')

newdate = '8/9/2021'        
removedash = Dates.DashDate(newdate)

print(Dates.DashDate(newdate))
        #or
print(removedash)
