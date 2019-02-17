from tkinter import*
import operator
from settings import storeObject
from borderButtons import borderButtons
from MalleuableTextBox import AutoResizedText
from MouseWheel import Scrolling_Area
# from borderButtons import borderButtons
# lst = []

# save function doesn't work that well, doesn't save twice - DONEEEEEEEEEEEEEE
#save function doesn't take into account the width of the word.
# we need to make textbox work take into account of width of word
#id digits only work up till 10

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
		nlines = word.count('\n')
		nlines = (nlines * 25)+25
		nWidth = word.split("\n")
		maxLineLength = findMaxLine(nWidth)
		self.txt = AutoResizedText(root, family="Arial",size=15, width = maxLineLength , height = nlines) #how to make int go by characters or something similar
		# scrollbar = scrollbar(root,command = test._textarea)
		self.txt.grid(row = self.height, column = self.width)
		self.txt.insert(word)
		self.txt._fit_to_size_of_text(word)
		self.txt.focus_set()
		self.txt.bind("<Tab>", self.rAppendArr)
		self.txt.bind("<Shift-Return>", self.lAppendArr)
		# we need to bind each click, enter, or return.
		#whichever command they call will save that button, being called so next time we call that command. It'll put it into settings.py
	def insertText(self,):#insert word into Text
		self.txt = AutoResizedText(root, family="Arial",size=15, width = maxLineLength , height = nlines)
		self.txt.grid(row = self.height, column = self.width)
	def saveButton(self,bob):
		try: # if there is something in temp, we insert txt into settings.py
			# must find the lst location in settings that matches bob.id. Then insert bob.txt.get into lst[x]
			foundIdLoc=searchForIdLoc(bob.id)
			if( not (foundIdLoc == 0)):
				a.changeTxt(foundIdLoc , bob.txt.get("1.0",END))
		except:#if there's nothing in temp, we just put that into bob
			temp = bob
	def mButton(self,height,width,colour,master): #when button is pressed, compresses or expands all the buttons that are underneath it
		self.colour = "yellow"
		self.middleB = Button(root,bg = "yellow", width = 1,command = lambda: self.toggle_txt(master))
		self.middleB.grid(row = self.height, column = self.width+1,sticky = W)
	def toggle_txt(self,master):#yeah, so we
		subGoalId = self.id + "0"
		subGoalCompare = conversion(subGoalId)
		if(self.colour == "yellow"):
			subGoalLst = findMYCHILDRENPLEASE(subGoalId)
			for x in range(0,len(subGoalLst)): # loop from id0 - idN
				currentId=conversion(lst[subGoalLst[x]].id)
				if currentId >= subGoalCompare: # error is here
					lst[subGoalLst[x]].word =  lst[subGoalLst[x]].txt.get("1.0",END)
					lst[subGoalLst[x]].middleB.grid_forget()
					lst[subGoalLst[x]].txt.grid_forget()
					self.colour = "red"
					self.middleB.configure(bg = self.colour)
		else:
			subGoalLst = findMYCHILDRENPLEASE(subGoalId)
			for x in range(0,len(subGoalLst)):	
				currentId=conversion(lst[subGoalLst[x]].id)
				if currentId >= subGoalCompare:
					lst[subGoalLst[x]].txtBox(master,lst[subGoalLst[x]].word)
					lst[subGoalLst[x]].mButton(0,0,"yellow",master)
					self.colour = "yellow"
					self.middleB.configure(bg = self.colour)

	def lAppendArr(self,cow):
		ArrWidth =int(self.width/2)
		temp = self.word[0:len(self.word)-1]
		temp = conversion(self.id)+1
		temp = conversion(temp)
		bob  = PythonApplication2(root,self.height+1,self.width,"",temp)#an appended id)
		
		lst.append(bob)
		self.moveDown()
						 
	def rAppendArr(self,cow):

		# case 1. There is one directly underneath; appends underneath all the buttons underneath directly
		# we simply move everything underneath by 1, and append it normally
		findThis = conversion(self.id)+1
	#	orThis
		temp =self.id + "0"
		self.word = self.word[0:len(self.word)-2]
		bob = PythonApplication2(root,self.height+1, self.width+2,"",temp)
		lst.append(bob)
		self.moveDown()
		self.txt.removeLastChars(2)
		#case 2, there's one diagonally
		#case 3, there's no next button underneath
	def moveDown(self):#moves all elements underneath the self.id
		sortedList = sortButtons() # use this to match id to x
		for x in range(0,len(lst)):
			print("\n")
		for x in range(0,len(lst)):
			print(sortedList[x][1])
			lst[sortedList[x][1]].height = x #[x][1] is looking at the x'th element and the items in the dictionary is [1]
			lst[sortedList[x][1]].txt.grid_configure(row = x, column = lst[sortedList[x][1]].width)
			lst[sortedList[x][1]].middleB.grid_configure(row = x, column = lst[sortedList[x][1]].width+1)
			
		# increaseId = findWidthId(self.id)
		# for x in range(0,len(increaseId)):
		# 	temp = conversion(lst[increaseId[x]].id)+1  # problem is here, is possibly, it's searching for all elements.
		# 	lst[x].id = temp
def addOpenFile(master):
	gui.subMenu.add_command(label = "save", command = save)
	gui.subMenu.add_command(label = "Open", command = lambda: createEmptyLst(master))
def createEmptyLst(master):
	lst = []
	openTheFile(master)
def openTheFile(master):
	file = "daily.txt"
	with open(file) as f:
		content = f.readlines()
		content = [x.strip() for x in content]
	for x in range(0,len(content)):
		line = content[x]
		bobData = line.split(",")
		bobData[0] = int(conversion(bobData[0]))
		bobData[1] = int(conversion(bobData[1]))
		temp = str(bobData[3])
		# print(temp)
		putIntoLines = bobData[2].replace("!@#","\n")
		print(putIntoLines)
		bob = PythonApplication2(master,bobData[0],bobData[1],putIntoLines,temp) # I think the reason is because we are using a different root each time?)
		lst.append(bob)

def save():
	file = open("daily.txt", "w+")
	for x in range(0,len(lst)):#height,width,word,id - order of object
		lst[x].word = lst[x].txt.get("1.0",END)
		putInALine = lst[x].word.replace("\n","!@#") #pu6s next lines as !@#
		# print(lst[x].height)
		file.write( str(lst[x].height) + ","  + str(lst[x].width) + "," + putInALine+"," + str(lst[x].id) + "\n")
	file.close()

# def delete(): ok im done. 4 duh day I guess :(-)

def sortButtons():
	#we group all elements with [0],[1],.....[n]
	#look at second dimension of [0], and group from empty-max element. afterwards append into sortedArr#
	temp = {}
	print(len(lst))
	for x in range(0,len(lst)): 
		temp[lst[x].id] = x
	sorted_x = sorted(temp.items(), key=operator.itemgetter(0))
	return sorted_x	

def searchForIdLoc(findId): #goes through entire array searching for a specific id. Returns the location in lst
	for x in range(0,len(a.retLst)):													# returns false if it's in list
		temp  = conversion(a.retId(x))	
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
def findMYCHILDRENPLEASE(findId):#this returns all the id's with a given width. Returned in an list
	arrLocations = []
	# for y in range(0,len(lst)):
	# 	print(lst[y].id)
	# print("end")
	for x in range(0,len(lst)):
		#criteria for being a child is, and same characters up till len-1
		if(findId[0:len(findId)-1] == lst[x].id[0:len(findId)-1]):
			if(findId[len(findId)-1]) <= lst[x].id[0:len(findId)-1]:
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

def findMaxLine(myList):
	try:
		for x in range(1,len(myList)):
			if myList[0] < myList[x]:
				myList[0] = myList[x]
		return int(myList[0])
	except ValueError:
		return 100
def printLst():
	for x in range(0,len[lst]):
		print(lst[x].id)
root = Tk()
lst = []
mouse = Scrolling_Area(root)
mouse.grid(row = 0, column = 999)
bob  = PythonApplication2(root,0,0,"","1")
lst.append(bob)
gui = borderButtons(root)
addOpenFile(root)
#bob.bothButtons()
root.mainloop()
#so here are some actual problems i'll be attempting to save
#i'll be attempting to save it so that it is exactly the same
	#currently the list isn't being appended in the same order?