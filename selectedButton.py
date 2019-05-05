import tkinter as tk
import operator
import json
from settings import storeObject
from borderButtons import borderButtons
from MalleuableTextBox import AutoResizedText
import copy

class object:
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
		self.txt.bind("<Shift-Delete>",self.deleteSelf)
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
		bob = object(self.master,self.height+1,self.width,parent = self)
		self.sibling = bob
		findParent= self
		while findParent.parent is not None:#I don't call the global "head" just incase head is referenced to another canvas or something
			findParent = findParent.parent
		sortButtons(findParent,0,0)

	def insertChild(self,cow):
		bob = object(self.master,self.height+1,self.width+1,parent = self)
		self.child = bob
		findParent = self
		while findParent.parent is not None:
			findParent = findParent.parent
		sortButtons(findParent,0,0)#what's the purpose of this? Well looks through all the buttons EVERY SINGLE ONE. Determines the num of descendents then can you  you know.
	def deleteSelf(self,cow):
		deleteThis = []
		findParent = self
		curr = self
		self.middleB.grid_forget()
		self.txt.grid_forget()
		if(self.sibling is not None):
			self.parent.child = self.sibling
		else:
			self.parent.child = None
		if(self.child is not None):
			deleteThis.append(self.child)
			curr = self.child
		while deleteThis:
			curr = deleteThis.pop(0)
			curr.middleB.grid_forget()
			curr.txt.grid_forget()
			if(curr.child is not None):
				deleteThis.append(curr.child)
			if(curr.sibling is not None):
				deleteThis.append(curr.sibling)
			curr = None
		print(head.height)
		sortButtons(head,0,0)
def addOpenFile(master,head):
	gui.subMenu.add_command(label = "save", command = save)
	gui.subMenu.add_command(label = "Open", command = lambda: openTheFile(master))
def insertNode(height,width):#inserts node into correct spot on tree given height and width
	global head
	#bfs search
	stack.append(head)
	while stack:
		curr = stack.pop(0)

		if((curr.child is not None) and (curr.child.height <=height) and (curr.child.width <=width)):
			stack.append(curr.child)
		if((curr.sibling is not None) and (curr.sibling.height <=height) and (curr.sibling.width <=width)):
			stack.append(curr.sibling)
def ancestor(curr,deltaW):
	for x in range(0,deltaW):
		curr = curr.parent
	return curr
def openTheFile(master):
	print("cow")
	with open(globFile) as json_file:  
		data = json.load(json_file)
		global head
		head = object(master,data[0]["height"],data[0]["width"],data[0]["word"])
		curr = head
		descendentCounter = 0
		for index in range(1,len(data)):
			if((curr.height+1 == data[index]["height"]) and (curr.width+1==data[index]["width"])):#if the next node is a child to curr
				bob = object(master,data[index]["height"],data[index]["width"],data[index]["word"],parent = curr)
				curr.child = bob
				curr = curr.child
			else:#it's a sibling to someone
				deltaW = curr.width - data[index]["width"]
				curr = ancestor(curr,deltaW)
				bob = object(master,data[index]["height"],data[index]["width"],data[index]["word"],parent = curr)
				curr.sibling = bob
			# else: # if the next node not a direct family member of curr

				
		#we need to determine if it's a child, a sibling, or someone elses direct family.
def traverse(curr,diction):#sorts in preorder(except reveresed sides)
	# if((curr.child is None) and (curr.sibling is None) and (curr is not None)):#deals with the end of a tree branch
	# 	diction.append({"height": curr.height,"width": curr.width, "word": curr.word})

	if(curr.child is not None):
		word= curr.child.txt.get("1.0",tk.END)
		diction.append({"height": curr.child.height,"width": curr.child.width, "word": word})
		traverse(curr.child,diction)
	if(curr.sibling is not None):
		word= curr.sibling.txt.get("1.0",tk.END)
		diction.append({"height": curr.sibling.height,"width": curr.sibling.width, "word": word})
		traverse(curr.sibling,diction)
	return diction


def save():
	file = open(globFile, "w+")
	global head
	copyOfT = copy.copy(head)#copies the entire tree onto copyOfT
	curr = copyOfT
	diction = {}
	diction["bob"]= []
	curr.word = head.txt.get("1.0",tk.END)
	diction["bob"].append({"height": curr.height,"width": curr.width, "word": curr.word})
	hold = traverse(curr,diction["bob"])
	json.dump(hold,file,indent = 4)
	file.close()	
	
def sortButtons(curr,height,width):#this sorts out bobs starting from curr(usually head)
	# print(str(height) + " " + str(width))
	if curr.child is not None:
		sortButtons(curr.child,height+1,width+1)#for each bob created from this child temp will increase by
	if curr.sibling is not None:
		temp1=countChildren(curr)+1
		sortButtons(curr.sibling,height+temp1,width)

	curr.height = height
	curr.width = width
	curr.txt.grid_configure(row = height, column = width)
	curr.middleB.grid_configure(row = height, column = width+1)


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
	return count

root = tk.Tk()
globFile = "daily.txt"
mainCanvas = tk.Canvas(root, background = 'gray30')# there are still methods that have master in them which we will not use anymore
frame = tk.Frame(mainCanvas, background="gray30")
initializeScollbar()
head  = object(frame,0,0)
gui = borderButtons(root)
addOpenFile(frame,head)
root.mainloop()