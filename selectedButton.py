import tkinter as tk
# from tkinter import *
import operator
# from Node import Node
from settings import storeObject
from borderButtons import borderButtons
from MalleuableTextBox import AutoResizedText
# from MouseWheel import Scrolling_Area
# from borderButtons import borderButtons
class PythonApplication2:
	def __init__(self, master,height,width,word= "",child= None,parent = None, sibling= None):
		self.master = master
		self.child = child
		self.parent = parent
		self.sibling = sibling
		self.width=width
		self.height=height
		self.word = word
		self.txtBox(word)
		self.mButton(0,0,"yellow")

	def txtBox(self,word):
		nlines = word.count('\n')
		nlines = (nlines * 25)+25
		nWidth = word.split("\n")
		maxLineLength = findMaxLine(nWidth)
		self.txt = AutoResizedText(self.master, family="Arial",size=12, width = maxLineLength , height = nlines,background = "gray40") #how to make int go by characters or something similar
		# scrollbar = scrollbar(master,command = test._textarea)
		self.txt.grid(row = self.height, column = self.width)
		self.txt.insert(word)
		self.txt._fit_to_size_of_text(word)
		self.txt.focus_set()
		self.txt.bind("<Tab>", self.insertChild)
		self.txt.bind("<Shift-Return>", self.insertSibling)
		# we need to bind each click, enter, or return.
		#whichever command they call will save that button, being called so next time we call that command. It'll put it into settings.py
	def insertText(self):#insert word into Text
		self.txt = tk.AutoResizedText(self.master, family="Arial",size=12, width = maxLineLength , height = nlines,background = "gray40")
		self.txt.grid(row = self.height, column = self.width)
	def saveButton(self,bob):
		try: # if there is something in temp, we insert txt into settings.py
			# must find the lst location in settings that matches bob.id. Then insert bob.txt.get into lst[x]
			foundIdLoc=searchForIdLoc(bob.id)
			if( not (foundIdLoc == 0)):
				a.changeTxt(foundIdLoc , bob.txt.get("1.0",END))
		except:#if there's nothing in temp, we just put that into bob
			temp = bob

	def mButton(self,height,width,colour): #when button is pressed, compresses or expands all the buttons that are underneath it
		self.colour = "yellow"
		self.middleB = tk.Button(self.master,bg = "coral", width = 1,command = lambda: self.toggle_txt)
		self.middleB.grid(row = self.height, column = self.width+1,sticky = "w")

	def toggle_txt(self):#yeah, so we
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
					self.colour = "purple"
					self.middleB.configure(bg = self.colour)
		else:
			subGoalLst = findMYCHILDRENPLEASE(subGoalId)
			for x in range(0,len(subGoalLst)):	
				currentId=conversion(lst[subGoalLst[x]].id)
				if currentId >= subGoalCompare:
					lst[subGoalLst[x]].tk.txtBox(self.master,lst[subGoalLst[x]].word)
					lst[subGoalLst[x]].tk.mButton(0,0,"blue",self.master)
					self.colour = "yellow"
					self.middleB.configure(bg = self.colour)	

	def moveDown(self):
		curr = self
		while curr.parent is not None:
			curr = curr.parent
		sortButtons(curr,0,0)

	def insertSibling(self,cow):
		bob = PythonApplication2(self.master,self.height+1,self.width,parent = self.parent)
		self.sibling = bob
		findParent= self
		if self.height == 0:#deals with case of heads siblings.
			bob.parent = self
		while findParent.parent is not None:
			findParent = findParent.parent
		sortButtons(findParent,0,0)

	def insertChild(self,cow):
		bob = PythonApplication2(self.master,self.height+1,self.width+1,parent = self)
		self.child = bob
		findParent = self
		while findParent.parent is not None:
			findParent = findParent.parent
		sortButtons(findParent,0,0)#what's the purpose of this? Well looks through all the buttons EVERY SINGLE ONE. Determines the num of descendents then can you  you know.

def addOpenFile(master,head):
	gui.subMenu.add_command(label = "save", command = save(head))
	gui.subMenu.add_command(label = "Open", command = lambda: createEmptyLst(master))
def createEmptyLst(master):
	lst.clear()
	openTheFile(master)

def openTheFile(master):
	file = "csc225Exam.txt" 
	with open(file) as f:
		content = f.readlines()
		content = [x.strip() for x in content]
	for x in range(0,len(content)):
		line = content[x]
		bobData = line.split("<|?s?|>")
		bobData[0] = int(conversion(bobData[0]))#HOLDS POSITION
		bobData[1] = int(conversion(bobData[1]))
		temp = str(bobData[3])#holds id
		putIntoLines = bobData[2].replace("<|/n|>","\n") #HOLDS THE WORD
		bob = PythonApplication2(master,bobData[0],bobData[1],putIntoLines,temp)
		lst.append(bob)
	printLst(lst)
	print("this is length of lst: " + str(len(lst)))

def save(head):
	file = open("daily.txt", "w+")
	stack = []
	stack.append(head)
	move = head
	while stack:
		move =stack.pop(0)
		print("this is in save " + move.word)
		putInALine = move.word.replace("\n","<|/n|>") 
		file.write( str(move.height) + " <|?s?|> "  + str(move.width) + " <|?s?|> " + putInALine+ " <|?s?|> " + "\n")
		if move.child is not None: # 
			stack.append(move.child)
		elif move.sibling is not None:
			stack.append(move.sibling)
	file.close()

def sortButtons(curr,height,width):#this sorts out bobs starting from curr(usually head)
	print(str(height) + " " + str(width))
	if curr.child is not None:
		sortButtons(curr.child,height+1,width+1)#for each bob created from this child temp will increase by
	if curr.sibling is not None:
		temp1=countChildren(curr)+1
		sortButtons(curr.sibling,height+temp1,width)

	curr.height = height
	curr.width = width
	curr.txt.grid_configure(row = height, column = width)
	curr.middleB.grid_configure(row = height, column = width+1)

def searchForIdLoc(findId): #goes through entire array searching for a specific id. Returns the location in lst
	for x in range(0,len(a.retLst)):													# returns false if it's in list
		temp  = conversion(a.retId(x))	
		if findId == temp:
			return x
	return 0

def findWidthId(findId):#this returns all the id's with a given width. Returned in an list
	arrLocations = []
	for x in range(0,len(lst)):
		#criteria for being in the same row is same length, and same characters up till len-1
		if(len(findId)==len(lst[x].id)):
			if(findId[0:len(findId)-1] == lst[x].id[0:len(lst[x].id)-1]):
				if(findId[len(findId)-1]) <= lst[x].id[len(lst[x].id)-1]:
					arrLocations.append(x)
	return arrLocations
def findMYCHILDRENPLEASE(findId):#this returns all the id's with a given width. Returned in an list
	arrLocations = []
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

def printLst(lst):
	for x in range(0,len(lst)):
		print(lst[x].id)

def onFrameConfigure(canvas):
	'''Reset the scroll region to encompass the inner frame'''
	canvas.configure(scrollregion=canvas.bbox("all"))

def _on_mousewheel(event):
	mainCanvas.yview_scroll(-1*(int)(event.delta/120), "units")

def initializeScollbar():
	mainCanvas.grid(row = 0,column = 0,sticky = "ew")
	mainCanvas.bind_all("<MouseWheel>", _on_mousewheel)
	vsb = tk.Scrollbar(root, orient="vertical",command=mainCanvas.yview)
	vsb.grid(column = 1,row = 0,sticky = "news")
	hsb = tk.Scrollbar(root, orient="horizontal",command=mainCanvas.xview)
	hsb.grid(column=0,row = 1,sticky = "ew")
	vsb.rowconfigure(0, weight=1)
	hsb.columnconfigure(0, weight=1)
	mainCanvas.configure(yscrollcommand=vsb.set,xscrollcommand = hsb.set,height = 700,width = 1400)	
	mainCanvas.create_window((12,12), window=frame, anchor="nw")
	frame.bind("<Configure>", lambda event, canvas=mainCanvas: onFrameConfigure(mainCanvas))

def delete(self):
	self.parents.child = None

def printLinked(head):
	print(str(head.height) + " " + str(head.width))
	if head.child is not None:
		printLinked(head.child)
	if head.sibling is not None:
		printLinked(head.sibling)
def countChildren(curr):#looks at relatives that are either same level(siblings) or descendents 
	count = 0
	stack = []
	if curr.child is not None:
		count+=1
		stack.append(curr.child)
	# if curr.sibling is not None:
	# 	count+=1
	# 	stack.append(curr.sibling)
	while stack:#uses dfs
		noder = stack.pop(0)
		if noder.child is not None:
			stack.append(noder.child)
			count+=1
		if noder.sibling is not None:
			stack.append(noder.sibling)
			count+=1
	print("count : " + str(count))	
	return count

root = tk.Tk()
mainCanvas = tk.Canvas(root, background = 'gray30')# there are still methods that have master in them which we will not use anymore
frame = tk.Frame(mainCanvas, background="gray30")
initializeScollbar()
head  = PythonApplication2(frame,0,0)
gui = borderButtons(root)
addOpenFile(frame,head)
root.mainloop()