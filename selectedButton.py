from tkinter import*
lst = []
class PythonApplication2:
	def __init__(self, master,height,width,word,id):
		self.width=width
		self.height=height
		self.word = word
		self.txtBox(master,word)
		self.mButton(0,0,"yellow",master)
		self.id = id
	#so one thing I remembered was that my arrays are not changing as my buttons change.
		#what's the difference between left button and right button which make it so hard to delete?
			#well what's changing is the width of the next instance
			#way the list is being appended lBut appends within the [width][here], meanwhile right appends [here][]
			#when destroying our object we are calling using the width of the button we pressed.
	def txtBox(self,master,word):
		self.txt = Entry(master, width = 60)
		self.txt.grid(row = self.height, column = self.width+1)
		self.txt.insert(0,word)
		self.txt.focus_set()
		self.txt.bind("<Tab>", self.rAppendArr)
		self.txt.bind("<Return>", self.lAppendArr)
	def mButton(self,height,width,colour,master): #when button is pressed, compresses or expands all the buttons that are underneath it
		self.colour = "yellow"
		self.middleB = Button(root,bg = "yellow", width = 1,command = lambda: self.toggle_txt(master))
		self.middleB.grid(row = self.height, column = self.width+2,sticky = W)
	def toggle_txt(self,master):#yeah, so we
		subGoalId = self.id + "0"
		subGoalId = conversion(subGoalId)
		if(self.colour == "yellow"):
			for x in range(0,len(lst)): # loop from id0 - idN
				currentId=conversion(lst[x].id)
				if currentId >= subGoalId: # error is here
					lst[x].word =  lst[x].txt.get()
					lst[x].middleB.grid_forget()
					lst[x].txt.grid_forget()
					self.colour = "red"
					self.middleB.configure(bg = self.colour)
		else:
			for x in range(0,len(lst)):
				currentId=conversion(lst[x].id)
				if currentId >= subGoalId:
					lst[x].txtBox(master,lst[x].word)
					lst[x].mButton(0,0,"yellow",master)
					self.colour = "yellow"
					self.middleB.configure(bg = self.colour)
	def lAppendArr(self,cow):
		ArrWidth =int(self.width/2)
		temp = conversion(self.id)+1
		temp = conversion(temp)
		bob  = PythonApplication2(root,self.height+1,self.width,"",temp)#an appended id)
		lst.append(bob)

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
					
	def rAppendArr(self,cow):
		temp =self.id + "0"
		bob = PythonApplication2(root,self.height+1, self.width+2,"",temp)
		lst.append(bob)

def conversion(converting):#this method converts string to int, or int to string
	try:
		#if it is a string with a number it will run this, changing it to an int
		converted = converting + ""
		converted = int(converting)
	except :# if it is a int, it'll convert to a string
		converted = str(converting)
	return converted

root = Tk()
#lst = []
bob  = PythonApplication2(root,0,0,"","1")
lst.append(bob)
#bob.bothButtons()
root.mainloop()

#2ND GOAL
	#how should my buttons work?
	#1. the left button should append regardless of which button is pressed as long as it is lst[][here]
	#2. the rest of the buttons underneath the lst[][x] should move downwards once if the right button is pressed
	#3. the buttons should then compress when mid but is pressed. 

#broader goals. 
	#should i start implementing the intuitive buttons, or should I make the buttons work correctly?. Well lets start from the bottom
	# which one uses the otherone.
	#well, I would say the intuitive buttons. I'm feeling pretty scared about implementing this part because this is reallllly difficult.


#1ST GOAL
	#Create buttons that work not by button presses, but instead with just the keyboard mainly.
	#1. we need a way to select a button. That way we can do the button presses.
	#2. so pressing tab will be like the rig ht button
	#3. pressing enter will make the textbox move to the next line?
	#4 pressing space bar will be like the left button

#Implementing 1st goal
	#there are these functions, creating new goal, creating meta goals, expending/contracting meta-goals, deleting goals, and finishing goals
	#finishing goals will be done with a regular button.
	#deleting goals will be done with possibly a more complex way
	#
