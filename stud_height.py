
class Student:
	global dictionary
	dictionary={}
	def __init__(self, regd, name, height):
		self.regd=regd
		self.name=name
		self.height=height
		dictionary[self.regd]=[self.name,self.height]

menu=""
while (menu!=5):
	print("""
1. Add Student Height.
2. Modify Student Height.
3. Remove Student record.
4. Display the records.
5. exit
""")
	try:
		menu=int(input("Enter your choice: "))
		if menu==1:
			student_regd=input("Enter the student registration number: ")
			student_name=input("Enter the student name: ")
			student_height=input("Enter the student height: ")
			student=Student(student_regd,student_name,student_height
		elif menu==2:
			modify_regd=input("Enter the registration number: ")
			if modify_regd in dictionary:
				modify_height=input("Enter the modified height: ")
				dictionary[modify_regd][1]=modify_height
				print("Name Modified Successfully")
			else:
				print("Please enter a valid Registration Number.")
		elif menu==3:
			if dictionary=={}:
				print("Cannot Remove from an empty dictioanry.")
			else:
				remove=input("Enter the registration number: ")
				if remove in dictionary:
					dictionary.pop(remove)
					print("Removed Successfully")
				else:
					print("Please enter a valid Registration Number.")
		elif menu==4:
			print(dictionary)
	
	except ValueError:
		print("Please enter a valid number.")
			
