class Student :
    
    def __init__ (self,name,homeTown,age,height,favoriteIceCream):

        self.name= name
        self.homeTown = homeTown
        self.age = age
        self.height = height
        self.favoriteIceCream = favoriteIceCream

    def print_summary(self):
        print("the name of the student is "+self.name+" he is age is "+self.age+" and home town is "+self.homeTown+" he is heigh "+self.height+"and his favorute ice cream is "+self.favoriteIceCream)

    def get_giraffe_gap(self, heigh):
        self.heigh = heigh
        average = 500-self.heigh
        return average
        
        


