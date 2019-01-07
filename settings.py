# settings.py
class storeObject:
	def __init__(self,height,width,word,id):
		self.height = height
		self.width = width
		self.word = word
		self.id = id
	def initGlobal(self):
		global lst
		lst = []
		# global waitForFile
		waitForFile = False
	def add(self): # height,width,word,id - order of object
		addingObject = {}
		addingObject["height"] = self.height
		addingObject["width"] = self.width
		addingObject["word"] = self.word
		addingObject["id"] = self.id
		lst.append(addingObject)
	def openTheFile(master):
		file = "cow.txt"
		with open(file) as f:
			content = f.readlines()
		content = [x.strip("") for x in content] 
		for x in range(0,len(content)):
			line = content[x]
			bobData = line.split(",")
			bobData[0] = conversion(bobData[0])
			bobData[1] = conversion(bobData[1])
			bob = PythonApplication2(root,bobData[0],bobData[1],bobData[2],bobData[3])
			a = storeObject(-1,-1,"","-1")
	def retLst(self):
		return lst
	def retH(self,location):# we need lst location in order for this to work. Fortunately we are given 
		return lst[location]["height"]

	def retW(self,location):
		return lst[location]["width"]

	def retWord(self,location):
		return lst[location]["word"]

	def retId(self,location):
		return lst[location]["id"]

	def changeH(self,location):
		self.height = delta
	def changeTxt(self,location,word):
		lst[location]["word"] = word

	# def waitingForFile(self):
	# 	return waitForFile	
	# def changeWaitForFile(self,what):
	# 	waitForFile = what
	def retLine(self,location):
		return str(lst[location]["height"]) + "," + str(lst[location]["width"]) + "," + str(lst[location]["word"]) + "," + str(lst[location]["id"])
   #how to implement this global variable? Do I need it?
   # the problem here is when I store the obj into global variable, it doesn't hold the object and thus, we cannot get any properties out of it
   #so we need some way to either decrypt the object or to store it b4.
   #so, unfortunately. Unless I can make the global variable hold the actual class.
   #I don't see another way
   #so what i'll do
   #1. I'll straight up import it
   #2. access work needed to be done when we save properties
   #accessing accessing. So, what we can do is make this into a dictionary. Make a method that stores everything, and spits it out perfectly
   # we have an access id, or access height method. Simple.  
