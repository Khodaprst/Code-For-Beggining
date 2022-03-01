class Pop():
    def __init__(self, name):
        self.__name = name

    #@property
    def name(self):
        return self.__name

    #@name.setter
    def namee(self, name):
        self.__name = name

#print your favorite artist
artist = Pop('javad nekayi')
print(artist.name())
artist.name = 'Arana'
print(artist.name)
