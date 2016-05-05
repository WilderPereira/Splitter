from stack import Stack

s = Stack()
with open('selects.sql') as fp:
    for line in fp:
        s.push(line)


out = open('reversed.txt','w')
while not s.isEmpty():
	out.write(s.pop())
out.close()
