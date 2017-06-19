class Stack:
	def __init__(self):
		self.stack = []
	
	def push(self, val):
		self.stack.append(val)
	
	def pop(self):
		return self.stack.pop(len(self.stack)-1)

	def __str__(self):
		return str(self.stack)

	def size(self):
		return len(self.stack)

	def peek(self):
		return self.stack[len(self.stack)-1]

	def isEmpty(self):
		if len(self.stack) == 0:
			return True
		else:
			return False

#s = Stack()
#s.push(5)
#print(s)
#s.push(10)
#print(s)
#s.push(15)
#print(s)

#print(s)
#print(s.pop())
#print(s)

#print(s.peek())

#print(s)
#print(s.pop())
#print(s.pop())
#print(s.peek())
