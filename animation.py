from cs1graphics import *
from time import sleep

paper = Canvas(300,200,'skyBlue','Rioanimation')
fish = Layer()


def draw_animal():
    
    water = Rectangle(300, 100, Point(150, 150))
    water.setFillColor('blue')
    water.setDepth(100)
    paper.add(water)

    Building = Rectangle(40, 80, Point(150, 80))
    Building.setFillColor('white')
    Building.setDepth(99)
    paper.add(Building)

    Cone = Polygon(Point(120,40),Point(150,20), Point(180,40))
    Cone.setFillColor('Red')
    Cone.setDepth(98)
    paper.add(Cone)

    FootBuilding = Rectangle(50, 20, Point(150, 115))
    FootBuilding.setFillColor('Red')
    FootBuilding.setDepth(98)
    paper.add(FootBuilding)

    Window = Circle(10, Point(150,60))
    Window.setFillColor('yellow')
    Window.setDepth(98)
    paper.add(Window)

    Sun = Circle(30, Point(210,101))
    Sun.setFillColor('Orange')
    Sun.setDepth(101)
    paper.add(Sun)

    

    Body = Circle(15, Point(50,150))
    Body.setFillColor('Green')
    Body.setDepth(98)
    fish.add(Body)

   

    Eye = Circle(6, Point(59,150))
    Eye.setFillColor('White')
    Eye.setDepth(98)
    fish.add(Eye)

    pupil = Circle(2, Point(61,150))
    pupil.setFillColor('black')
    pupil.setDepth(98)
    fish.add(pupil)

    paper.add(fish)

    Tail = Polygon(Point(35,150),Point(28,140), Point(25,160))
    Tail.setFillColor('Yellow')
    Tail.setDepth(98)
    fish.add(Tail)
    
    timedelay = 1


        
    sleep(timedelay)
    fish.move(20,0)
    Tail.rotate(20)
    sleep(timedelay)
    fish.move(20,0)
    Tail.rotate(-20)
    sleep(timedelay)
    fish.move(20,0)
    Tail.rotate(-20)
    sleep(timedelay)
    fish.move(20,0)
    Tail.rotate(20)
    sleep(timedelay)
    fish.move(20,0)
    Tail.rotate(20)
    sleep(timedelay)
    fish.move(20,0)
    Tail.rotate(-20)
    sleep(timedelay)
    fish.move(20,0)
    Tail.rotate(-20)
    sleep(timedelay)
    fish.move(20,0)
    Tail.rotate(20)
    
    

   



    
def show_animation():
    pass
    
    
    
    
draw_animal()
# show_animation()