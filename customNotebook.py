from tkinter import ttk
import tkinter as tk
class CustomNotebook(ttk.Notebook):
    """A ttk Notebook with close buttons on each tab"""
    
    __initialized = False
    def __init__(self, *args, **kwargs):
        # self.__newCustomWidget()
        if not self.__initialized:
            self.__initialize_custom_style()# FIRST they create the style labeled as CustomNoteBook.tab
            self.__inititialized = True
            self.headLst = []
            
        kwargs["style"] = "CustomNotebook"# now they somehow to do this.
        ttk.Notebook.__init__(self, *args, **kwargs) # and now they do this.
#so essentially I need to change customNoteBOOK.Tab
        self._active = None
        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)
    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)
        index = self.index("@%d,%d" % (event.x, event.y))
        if "close" in element:
            self.state(['pressed'])
            self._active = index
        global headLst
        global head
        head = headLst[index]
    def on_close_release(self, event):
        """Called when the button is released over the close button"""
        # if not self.instate(['pressed']):
        #   return
        try:
            index = self.index("@%d,%d" % (event.x, event.y))
            element =  self.identify(event.x, event.y)
        except:
            return


        if "close" in element and self._active == index:
            self.forget(index)
            self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None
        global headLst
        global head
        head = headLst[index]
    def getIndex(self,event):
        try:
            return self.index("@%d,%d" % (event.x, event.y))
        except:
            return -1
    def newCustomWidget(self):#SO I'M GOING TO TRY TO BE ABLE TO SWITCH BETWEEN STATES.
        style = ttk.Style()
        style.layout("new.Tab", [
            ("new.tab", {
            "sticky": "w", 
            "children": [
                ("new.padding", {
                "side": "bot", 
                "sticky": "w",
                "children": [
                    ("new.focus", {
                    "side": "top", 
                    "sticky": "w",
                    "children": [
                        ("new.label", {"side": "left", "sticky": ''}),
                        # ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                    ]
                })
                ]
            })
            ]
        })
        ])
    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            tk.PhotoImage("img_close", data='''
            R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
            d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
            5kEJADs=
            '''),
            tk.PhotoImage("img_closeactive", data='''
            R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
            AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
            '''),
            tk.PhotoImage("img_closepressed", data='''
            R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
            d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
            5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close",("active", "pressed", "!disabled", "img_closepressed"),("active", "!disabled", "img_closeactive"), border=8, sticky='')#so this creates the x
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [("CustomNotebook.tab", {
            "sticky": "nswe", 
            "children": [
                ("CustomNotebook.padding", {
                "side": "top", 
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.focus", {
                    "side": "top", 
                    "sticky": "nswe",
                    "children": [
                        ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                        ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                    ]
                })
                ]
            })
            ]
        })
        ])
        style.map('CustomNotebook.tab',image = [('disabled',[("CustomNotebook.tab", {
            "sticky": "nswe", 
            "children": [
                ("CustomNotebook.padding", {
                "side": "top", 
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.focus", {
                    "side": "top", 
                    "sticky": "nswe",
                    "children": [
                        ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                    ]
                })
                ]
            })
            ]
        })
        ] )])