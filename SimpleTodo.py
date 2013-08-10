#Git Example
#Class creation with Insert, Delete, View Methods
class Todo:
  def __init__(self,name,date,time,c):
		self.name = name
		self.date = date
		self.time = time
		self.c	  = c

	def Insert(self):
		fi = open('todo.dat','a')
		t = self.name + ' ' + self.date + ' ' + self.time + '\n'
		fi.write(t)
		print "saved!!"
		fi.close()


#Display the list
print "1 - Insert New Task"
print "2 - Delete Task"
print "3 - View Task"
print "4 - Exist App"
#Get the input
while True:
	n = input()
	if n == 1:
		#Insert new task
		name = raw_input("Enter Task Name: ")
		date = raw_input("Enter Date: ")
		time = raw_input("Enter Time: ")
		tmp = Todo(name,date,time,n)
		tmp.Insert()
	elif n == 2:
		#Delete Task
		pass
	elif n == 3:
		f=open('todo.dat','r')
		for i in f.readlines():
			print i
	else:
		exit()


#Check for condition (Pending)


#Perform operation (Pending)


#Display the result (Pending)


#Features upcoming..(GUI based TODO list)
