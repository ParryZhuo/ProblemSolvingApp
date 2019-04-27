class Node: 
	def __init__(self,height,width,child = None, sibling = None,parents = None,word=""):
		self.height = height
		self.width = width
		self.parents = parents 
		self.sibling = sibling # reference to sibling node in DLL 
		self.child = child
		self.word = word 
	def countChildren(curr):#
		count = 0
		stack = []
		if curr.child is not None:
			stack.append(curr.child)
		while stack:
			noder = stack.pop(0)
			if noder.child is not None:
				stack.append(noder.child)
				count+=1
			if noder.sibling is not None:
				stack.append(noder.sibling)
				count+=1
		
		return count
	def insertWord(self,word):
		self.word = word
		print(self.word)
def insertSibling(prevNode):
	count = Node.countChildren(prevNode)+1
	print("\n" + str(count))
	prevNode.sibling = Node(prevNode.height+count,prevNode.width,parents = prevNode)	
	return prevNode.sibling

def insertChild(prevNode):
	temp = prevNode
	prevNode.child = Node
	def delete(self):
		self.parents.child = None
	def printLinked(head):
		print(str(head.height) + " " + str(head.width))
		if head.child is not None:
			printLinked(head.child)
		if head.sibling is not None:
			printLinked(head.sibling)

# the probl
#    #
# head = Node(0,0)
# curr = insertSibling(head)
# head.insertWord("wat")
# curr.insertWord("FUCK YOU")
# print(curr.word)
# head.insertSibling()
# insertChild(head)
# head = insertChild(head.child)
# while head.parents is not None:
# 	head = head.parents
# printLinked(head)

