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
		self.txt.grid(row = self.height, column = self.width)
		self.txt.insert(0,word)
		self.txt.focus_set()
		self.txt.bind("<Tab>", self.rAppendArr)
		self.txt.bind("<Return>", self.lAppendArr)
	def mButton(self,height,width,colour,master): #when button is pressed, compresses or expands all the buttons that are underneath it
		self.colour = "yellow"
		self.middleB = Button(root,bg = "yellow", width = 1,command = lambda: self.toggle_txt(master))
		self.middleB.grid(row = self.height, column = self.width+1,sticky = W)
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
		#case 1. There's no next button underneath
		#case 2. There is one directly underneath
		#	testId = conversion(self.id)+1
		#	count = 0
		# 		for x in range(0,len(lst)):
		# 	if(lst[x].id==testId):
		# 		count=+1						
		# 		testId=+1
		# if(count != 0):
		# 	bob = PythonApplication2(root,self.height+count, self.width+2,"",temp)
		# 	lst.append(bob)	
		#case 3, there's one diagonally
						 
	def rAppendArr(self,cow):

		# case 1. There is one directly underneath; appends underneath all the buttons underneath directly
		# we simply move everything underneath by 1, and append it normally
		findThis = conversion(self.id)+1
	#	orThis
		if(not(searchForId(0,findThis)==0)): # check if there's button underneath
			temp =self.id + "0"
			bob = PythonApplication2(root,self.height, self.width+2,"",temp)
			lst.append(bob)
			self.moveDown()
		else :		# if there's a button diagonally needs to be implemented in the future
			temp =self.id + "0"
			bob = PythonApplication2(root,self.height+1, self.width+2,"",temp)
			lst.append(bob)
		#case 2, there's one diagonally
		#case 3, there's no next button underneath
	def moveDown(self):#moves all elements underneath the self.id
		translateId = conversion(self.id)
		for x in range(0,len(lst)):
			compare1 = conversion(lst[x].id)
			# print(compare1)
			if compare1 > translateId:#what we do here is simply increment it's height(not id)
				print(lst[x].height)
				lst[x].height +=1
				lst[x].txt.grid_configure(row = lst[x].height, column = lst[x].width)
				lst[x].middleB.grid_configure(row = lst[x].height, column = lst[x].width+1)
		# increaseId = findWidthId(self.id)
		# for x in range(0,len(increaseId)):
		# 	temp = conversion(lst[increaseId[x]].id)+1  # problem is here, is possibly, it's searching for all elements.
		# 	lst[x].id = temp
	def sortButtons(self):
	#we group all elements with [0],[1],.....[n]
	#look at second dimension of [0], and group from empty-max element. afterwards append into sortedArr					  #
		temp = []
		for x in range(0,len(lst)-1):
			temp.append(lst[x].id)
		return temp.sort()	

def searchForId(startFromHere,findId): #goes through entire array searching for a specific id. Returns the location in lst
	for x in range(0,len(lst)):													# returns false if it's in list
		temp  = conversion(lst[x].id)	
		if findId == temp:
			return x
	return 0

def findWidthId(findId):#this returns all the id's with a given width. Returned in an list
	arrLocations = []
	# for y in range(0,len(lst)):
	# 	print(lst[y].id)
	# print("end")
	for x in range(0,len(lst)):
		#criteria for being in the same row is same length, and same characters up till len-1
		if(len(findId)==len(lst[x].id)):
			if(findId[0:len(findId)-1] == lst[x].id[0:len(lst[x].id)-1]):
				if(findId[len(findId)-1]) <= lst[x].id[len(lst[x].id)-1]:
					arrLocations.append(x)
	return arrLocations				 

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
