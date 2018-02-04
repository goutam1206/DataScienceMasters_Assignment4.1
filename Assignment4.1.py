class Shape:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.sides=[]
    
    def setsides(self):
        self.sides = [self.a,self.b,self.c]
        return self.sides
    
class Triangle(Shape):
    def __init__(self,a,b,c):
        Shape.__init__(self,a,b,c)
        super(Triangle,self).__init__(a,b,c)

    def findArea(self):
        # calculate the semi-perimeter
        s = (self.a+self.b+self.c)/2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        
        print('The area of the triangle is %0.2f' %area)
        
t = Triangle(3,4,5)
t.setsides()
t.findArea()


########

myList = ['Here','is','a','function','which','takes','a','list','of','words','and','an','integer','as','arguments','and','returns','all','the','words','whose','length','is','greater','than','the','integer']
limit = 0
while True:
    try:
        limit = int(input("Enter an integer: "))
        break
    except:
        print ("Please enter an integer value")

mySizeList = [ element for element in  myList if len(element) > limit]
print (mySizeList)
