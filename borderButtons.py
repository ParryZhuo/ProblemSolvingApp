from tkinter import*
import operator
from settings import storeObject
# from selectedButton import PythonApplication2
class borderButtons:
	def __init__(self,master):
		self.master = master
		def new():
			# file = open("test.txt",w+)
			# a = storeObject(0,0,"",1)
			print("asdf")

		def delete():
			print("HAHA it doesn't work yet")

		def Exit():
			print("HAHA it doesn't work yet")
		def conversion(converting):#this method converts string to int, or int to string
			try:
		#if it is a string with a number it will run this, changing it to an int
				converted = converting + ""
				converted = int(converting)
			except :# if it is a int, it'll convert to a string
				converted = str(converting)
			return converted
# def save():
# 	file = open("cow.txt", "w+")
# 	a = storeObject(-1,-1,"","-1")
# 	for x in range(0,len(a.retLst())):#height,width,word,id - order of object
# 		file.write(a.retLine(x) + "\n")
		
# 	file.close()





# with open(fname) as f:
#     content = f.readlines()
# # you may also want to remove whitespace characters like `\n` at the end of each line
# content = [x.strip("") for x in content] 
# # content.strip(",")
# for x in range (0,len(content)):
# 	line = content[x].split(",")
		# ******** Menu ************
		menu = Menu(master)
		master.config(menu = menu) 

		self.subMenu = Menu(menu,tearoff = 0) # creating a menu item within the menu
		menu.add_cascade(label = "Edit", menu = self.subMenu) #Name of drop down menu
		self.subMenu.add_command(label = "new", command = new)
		# self.subMenu.add_command(label = "Save", command = save)
		self.subMenu.add_command(label = "delete", command = delete)
	
		self.subMenu.add_separator()
		self.subMenu.add_command(label = "Exit", command = Exit)


		# #  ******** TOOLBAR ************
		# toolbar = Frame(master, bg = "blue")
		# insertButton = Button(toolbar, text="N", command = TBD)
		# insertButton.pack(side = LEFT, padx=2, pady = 2)
		# printButton = Button(toolbar, text="TBD", command = TBD)
		# printButton.pack(side = LEFT, padx=2, pady = 2)

		# toolbar.pack(side = TOP, fill = X)

		# # *********STATUS BAR***********
		# status = Label(master, text = "numbers of goals completed", bd =1, relief = SUNKEN, anchor = W)
		# status.pack(side = BOTTOM, fill = X)

# master = Tk()
# #lst = []
# settings.init()
# bob  = PythonApplication2(master,0,0,"")
# lst.append([bob])
# #bob.bothButtons()
# master.mainloop()