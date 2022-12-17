#Najib Azharun Najwa IG @najibazharun I made this project because gabut WKWKWKW

#let's get it
import turtle

# we will create object for this turtle

tu = turtle.Turtle() #meke sure to keep this T capital
tu.screen.bgcolor("black") #background color will change to black

tu.pensize(2) #size of pen
tu.color("green") #intially the color off turtle will be green
#now we start our turtle will be in the right direction
#so make it in upword direction we will make to turn left at 90
tu.left(90) 
#so now it will go in upward direction
#we will bring turtle down so we can see whole tree which covers the screen 
tu.backward(100)
tu.speed(200) #speed of turtle
tu.shape('turtle') #this make out arrow in the shape turtle

# we will use here recursion function to draw the tree
def tree(i):
    if i<10:
        return
        #this is base conditon to stop recursion because if we don't give this condition turtle will draw it infinite times as this loop recursion loop is infinite untill same base condisition is not given
    else:
        tu.forward(i) #we will move our tree in forward dir
        tu.color("orange") #after it has drown that straight line we will make a fruit or flower orange color which will be circle
        tu.circle(2)
        #after the flower or fruit is drawn we want our color back to brown as we want to drawn branch 
        tu.color("brown")
        #till here it is drawn this much
        #now we want to draw it is left direction
        tu.left(30) #so when it goes to left it will again draw the flower and it will go on till the value of i becomes less then 10
        tree(3*i/4) #3*100/4 = 75 now value of i 75 again 3*75/ = 56.25 now valou of i is 56.25 again 56.25*/4 so like this it will go on
        tu.right(60) #once left part is done it will come back by backward() than it will go in right dir
        tree(3*i/4)
        tu.left(30)
        tu.backward(i)
        
tree(100)     
turtle.done()