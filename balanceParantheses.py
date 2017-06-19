from Stack import Stack

expr = input();
print(expr)

stack = Stack()

for l in expr:
	if l == '(':
		print("Opening")
		stack.push("(")
	elif l == ')':
		print("Closing")
		if stack.pop() != '(':
			print("Not Balanced")
			exit(0)

if stack.isEmpty():		
	print("Balanced")
else:
	print("Unbalanced")	
