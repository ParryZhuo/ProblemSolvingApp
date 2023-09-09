# ProblemSolvingApp

Designed and developed an app that helps users solve difficult/big problems by providing them with
a template to break problems into smaller/easier ones, then to break those sub-problems into even
smaller ones continuing this process until the problems are at a manageable level.

• Programmed in Python. Implemented a tree using double linked lists and 
traversed through this tree using DFS/BFS(AKA breadth first/ depth first search)

• Explored and implemented a variety of data-structures while creating iterations of
the app including linked lists, dictionaries, hash tables, and many ways of using arrays

• Gained practical experience in optimizing code for performance and scalability while maintaining a focus on readability and maintainability

• Created the GUI in TKINTER gaining exposure to the structure of GUI's are programmed


![image](https://user-images.githubusercontent.com/36753290/170846460-1703f019-fa4b-4351-bf40-a6230a6f68ed.png)

Here is a code snippet from "selectedButton.py" 
```python
    def deleteSelf(self,cow):#deletes itself as well as all descendents of self utilizing DFS
        deleteThis = []
        findParent = self
        curr = self
        self.txt.destroy()
        if(self.child is not None):#here we are seeing if it has children so we can delete it and the rest of it's descendents using dfs
            deleteThis.append(self.child)
        self.parent.child = None
        if(self.sibling is not None):#here we replace the link between the parent and the self with either none or it's sibling.
            self.parent.child = self.sibling
        else:		
            self.parent.sibling =None
        while deleteThis:
            curr = deleteThis.pop(0)
            curr.txt.destroy()
            if(curr.child is not None):
                deleteThis.append(curr.child)
            if(curr.sibling is not None):
                deleteThis.append(curr.sibling)
            curr = None # DELETES REFERENCE To child
            sortButtons(head,0,0) #reorganizes GUI to fit the new structure created
