import turtle

myPen = turtle.Pen() #make pen object


#open file1 in read mode
file1 = open('file1.rtf', 'r')

#for every line in the file do the following code 
for line in file:
    
    #split each line on spaces
    words = line.split()
    
    #for every word in the line
    for word in words:
        
        #do the correct code based on the instruction
        if word[0] == 'goto':
            x = int(word[1])
            y = int(word[2])
            myPen.goto(x,y)
        if word[0] == 'forward':
            dist = int(word[1])
            myPen.forward(dist)
        if word[0] == 'right':
            degree = int(word[1])
            myPen.right(degree)
        if word[0] == 'left':
            degree = int(word[1])
            myPen.left(degree)
    