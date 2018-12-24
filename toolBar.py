from tkinter import*
lst = []
class PythonApplication2:
    def __init__(self, master,height,width):
        self.width=width
        self.height=height
        #frame = Frame(master,height = 1)
        self.rButton()
        self.lButton()
        self.txtBox(master)
        self.mButton("yellow",master)
    #so one thing I remembered was that my arrays are not changing as my buttons change.
        #what's the difference between left button and right button which make it so hard to delete?
            #well what's changing is the width of the next instance
            #way the list is being appended lBut appends within the [width][here], meanwhile right appends [here][]
            #when destroying our object we are calling using the width of the button we pressed.
    def txtBox(self,master):
        self.txt = Entry(master, width = 50)
        self.txt.grid(row = self.height, column = self.width+1)

    def lButton(self): #when pressed, pushes one set of the class down

        self.leftB = Button(root,bg = "blue", width = 1,command = self.lAppendArr) #trying something new currently here
        self.leftB.grid(row = self.height, column =  self.width,sticky = E)

    def rButton(self): # when pressed, pushes left and 1 down

        self.rightB = Button(root,bg = "green", width = 1,command = self.rAppendArr)
        self.rightB.grid(row = self.height, column =  self.width+3,sticky = W)

    def mButton(self,colour,master): #when button is pressed, compresses or expands all the buttons that are underneath it
        self.colour = "yellow"
        temp = [] 
        self.middleB = Button(root,bg = "yellow", width = 1,command = lambda: self.deleteIt(master))
        self.middleB.grid(row = self.height, column = self.width+2,sticky = W)
    def deleteIt(self,master):#yeah, so we
        #self.deleteMe
        ArrWidth =int(self.width/2)
        if(self.colour == "yellow"):
            try:
                for x in range(0,len(lst[ArrWidth+1])):
                    print("debug1")
                    lst[ArrWidth+1][x].middleB.destroy()
                    lst[ArrWidth+1][x].leftB.destroy()
                    lst[ArrWidth+1][x].rightB.destroy()
                    lst[ArrWidth+1][x].txt.destroy()
                    self.colour = "red"
                    self.middleB.configure(bg = self.colour)
            except IndexError:
                print("asd")
        else:
            try:
                for x in range(0,len(lst[ArrWidth+1])):
                    print("debug1")
                    lst[ArrWidth+1][x].lButton()
                    lst[ArrWidth+1][x].rButton()
                    lst[ArrWidth+1][x].txtBox(master)
                    lst[ArrWidth+1][x].mButton("yellow",master)
                    #lst[ArrWidth][x].leftB.grid(row = self.height, column =  self.width,sticky = E)
                    #lst[ArrWidth][x].rightB.grid(row = self.height, column =  self.width+3,sticky = E)
                    #lst[ArrWidth][x].txt.grid(row = self.height, column =  self.width+1,sticky = E)
                    self.colour = "yellow"
                    self.middleB.configure(bg = self.colour)
            except IndexError:
                print("asd")         
    def deleteMe(self): #supposed to remove all 3 buttons,when mid one is being pressed
        #there's a case where there's no elements within therefore nothing will be deleted
        #try:
        
        lst[self.width-1][0].middleB.destroy()
        lst[self.width-1][0].leftB.destroy()
        lst[self.width-1][0].rightB.destroy()
        lst[self.width-1][0].txt.destroy()
        #except IndexError:
        #    return
        #now we must delete all the other buttons within the same width
    
    def lAppendArr(self):
        ArrWidth =int(self.width/2)
        #1 scenario there's a button underneath [self.width][self.height+1]
            #we look [][here], find the last element, and call lAppend on that object
        #2 scenario, there's a button underneath [self.width+1][self.height+1]
            #what we could do here is actually append the button right above the current one?
            #what do we do about contraction of right buttons?
        #3 scenario, there's no button underneath
        bob  = PythonApplication2(root,self.height+1,self.width)
        lst[ArrWidth].append(bob)
        print(lst)
        #difference between how lst is orientated vs self.width/self.height
            #   # - f(0,0)  lst[0][0] f(x,y) lst[width][height]
                    # - f(2,1) lst[1][0]
                        # - f(4,2) lst[2][0]
                        # - f(4,3) lst[2][1]
                            # - f(6,4) lst[3][0]
                            # - f(6,5) lst[3][1]

            #Problem 1st time we delete, it deletes all buttons within the lst[][here]
            #second time we delete, it deletes from 1-length lst[][here]
                #what changes when we delete the first time and second time
                    #
    def rAppendArr(self):
        #scenario 1, next button is [][self.height+1]
            #[we increase this by 1][]
        #scenario 2, next button is [self.width+1][self.height+1]
            #we append onto here [self.width+1][self.height+2] duh.
        if(len(lst[ArrWidth])> 
        bob = PythonApplication2(root,self.height+1, self.width+2)
        lst.append([bob])
        print(lst)
    
root = Tk()
#lst = []
bob  = PythonApplication2(root,0,0)
lst.append([bob])
#bob.bothButtons()
root.mainloop()
#2ND GOAL
    #how should my buttons work?
    #1. the left button should append regardless of which button is pressed as long as it is lst[][here]
    #2. the rest of the buttons underneath the lst[][x] should move downwards once if the right button is pressed
    #3. the buttons should then compress when mid but is pressed. 

#broader goals. for end of winter break
    #make buttons organize themselves correctly
    #make a save option
    # make the buttons expand themselves
    #make way to delete buttons entirely.

#1ST GOAL
    #Create buttons that work not by button presses, but instead with just the keyboard mainly.
    #1. we need a way to select a button. That way we can do the button presses.
    #2. so pressing tab will be like the right button
    #3. pressing enter will make the textbox move to the next line?
    #4 pressing space bar will be like the left button

#Implementing 1st goal
    #so I want the buttons to organize themselves correctly
        #when right button is presesd with other meta goals underneath how do.