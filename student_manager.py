import sys
import json
try:
	with open("example.json") as f:
		data = json.load(f)
except FileNotFoundError:
	data=[]
class student_manager:

	def __init__(self, name="", id="", age="", clas="", marks=""):
		self.name = name
		self.id = id
		self.age = age
		self.clas = clas
		self.marks = marks

	def get_input(self):
		try:
			self.name = input("enter name of student:\t")
			self.id= input("enter id of student:\t")
			self.age = input("enter age of student:\t")
			self.clas= input("enter class of student:\t")
			self.marks = input("enter marks of student:\t")

		except Exception:
			print("you have done something wrong")
			self.get_input()

	def info_true(self):

		while True:

			print(
				f"name : {self.name}\n"
				f"id : {self.id}\n"
				f"Age : {self.age}\n"
				f"Class : {self.clas}\n"
				f"Marks : {self.marks}"
			)

			print("Is this information true (yes or no)")
			true = input("> ")

			if true.lower() == "yes":

				data.append({
					"name": self.name,
					"id": self.id,
					"age": self.age,
					"class": self.clas,
					"marks": self.marks
				})

				break

			elif true.lower() == "no":

				print("give input again")
				self.get_input()

			else:

				print("invalid choice!")
				continue

	def search_student(self):

		print("enter id of student to search")
		sc = input("> ")

		for i in data:

			id= i.get("id")

			if sc == id:

				for items in i.items():
					print(items)

				return

		print("student not found")

	
	def view_all_students(self):
		for student in data:
			for k,v in student.items():
				print(k ,":" ,v)
	def update_student(self):
		g=input("enter id of student:\t")
		found=False
		for student in data:
			if student.get("id")==g:
				student["name"]=input("enter name of student:\t")
				student["age"]=input("enter age if student:\t")
				student["class"] = input("enyer class of student:\t")
				student["marks"]=input("enter marks of student:\t")
				found=True
				print("student updated!")
		if not found:
			print("student not found!")
				
	def delete_student(self):

		print("enter id of client to delete:\t")
		im = input("> ")

		for m in data:

			if im == m.get("id"):

				p = data.index(m)
				data.pop(p)

				print("student deleted successfully!")
				return

		print(f"there is no student of id {im}")
	def save_in_file(self):
		with open("example.json","w") as f:
			json.dump(data,f,indent=2)
object = student_manager()


if __name__ == "__main__":

	print("welcome!")

	print(
		"you can do following operations\n"
		"add\n"
		"delete\n"
		"search\n"
		"view all\n"
		"update\n"
		"exit"
	)

	while True:

		print("what do you want to do?")
		l = input("> ")

		if l.lower() == "add":

			object.get_input()
			object.info_true()
			object.save_in_file()

		elif l.lower() == "delete":

			object.delete_student()
			object.save_in_file()

		elif l.lower() == "search":

			object.search_student()
		
		elif l.lower()=="view all":
			object.view_all_students()
		
		elif l.lower()=="update":
			object.update_student()
			object.save_in_file()
		
		elif l.lower() == "exit":

			import sys
			sys.exit()

		else:

			print("invalid choice!")			