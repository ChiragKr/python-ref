__author__ = 'Chirag'
import datetime


class Person(object):
	def __init__(self, name):
		"""create a person called name"""
		self.name = name
		self.birthday = None
		self.last_name = name.split(' ')[-1]

	def get_last_name(self):
		"""return self's last name"""
		return self.last_name

	def __str__(self):
		"""return self's name"""
		return self.name

	def set_birthday(self, month, day, year):
		"""sets self's birthday"""
		self.birthday = datetime.date(year, month, day)

	def get_age(self):
		""""return self's current age in days"""
		if self.birthday is None:
			raise ValueError
		return (datetime.date.today() - self.birthday).days

	def __lt__(self, other):  # overriding the comparison operator '<'
		"""return True if self's name is lexicographically
		less that other's name, False otherwise"""
		if self.last_name == other.last_name:
			return self.name < other.last_name
		return self.last_name < other.last_name


p1 = Person("Mark Zuckerberg")
p1. set_birthday(5, 14, 84)
p2 = Person("Drew Houston")
p2.set_birthday(3, 4, 83)
p3 = Person("Bill Gates")
p3.set_birthday(10, 28, 55)
p4 = Person("Andrew Gates")
p5 = Person("Steve Wozniak")

personList = [p1, p2, p3, p4, p5]

for person in personList:
	print(person)
print()

personList.sort()  # uses the Person.__lt__()

for person in personList:
	print(person)
print()


class MITPerson(Person):
	nextIdNum = 0

	def __init__(self, name):
		Person.__init__(self, name)
		self.idnum = MITPerson.nextIdNum
		MITPerson.nextIdNum += 1

	def getIdNum(self):
		return self.idnum

	# sorting MIT people uses their id rather than names
	def __lt__(self, other):
		return self.idnum < other.idnum

	def speak(self, utterance):
		return self.get_last_name() + " says: " + utterance


m3 = MITPerson('Mark Zuckerberg')
Person.set_birthday(m3, 5, 14, 84)
# calling "Person" class method "set_birthday" method requires manually specifying "self" object
m2 = MITPerson("Drew Houston")
Person.set_birthday(m2, 3, 4, 83)
m1 = MITPerson("Bill Gates")
Person.set_birthday(m1, 10, 28, 55)

MITPersonList = [m1, m2, m3]
print(m1.speak("Hi There!"))
print()

for person in MITPersonList:
	print(person)
print()

MITPersonList.sort()  # uses the MITPerson.__lt__()

for person in MITPersonList:
	print(person)
print()

p1 = MITPerson("Eric")
p2 = MITPerson("John")
p3 = MITPerson("John")
p4 = Person("John")

print(p1 < p2)  # True. MITPerson.__lt__() called and the calling object is 'p1'
# print(p1 < p4)
'''AttributeError: 'Person' object has no attribute 'idnum' since 
MITPerson.__lt__() is called and the calling object is 'p1'''
print(p4 < p1)  # False. Person.__lt__() is called and the calling object is 'p4'
print()


'''Substitution Principle : 
important behaviour of superclass should be supported by all subclasses'''


class Student(MITPerson):  # Helps implement the 'Substitution Principle'
	pass


class UG(Student):
	def __init__(self, name, class_year):
		MITPerson.__init__(self, name)
		self.year = class_year

	def get_class(self):
		return self.year

	def speak(self, utterance):
		return MITPerson.speak(self, "Dude, " + utterance)  # UG.speak() further calls MITPerson.speak()


class Grad(Student):
	pass


class TransferStudent(Student):
	pass


def is_student(obj):
	# return isinstance(obj, UG) or isinstance(obj, Grad)
	return isinstance(obj, Student)  # after cleaning up the hierarchy


s1 = UG("Matt Damon", 2017)
s2 = UG("Ben Affleck", 2017)
s3 = UG("Lin Manuel Miranda", 2018)
s4 = Grad("Leonardo di Caprio")
s5 = TransferStudent("Robert deNiro")

print(s1)
print(s1.get_class())
print(s1.speak('Where is the quiz?'))
print(s2.speak("I have no clue!"))
print()


class Professor(MITPerson):
	def __init__(self, name, department):
		MITPerson.__init__(self, name)
		self.department = department

	def speak(self, utterance):
		new = 'In course ' + self.department + " we say "
		return MITPerson.speak(self, new + utterance)  # using MITPerson.speak()

	def lecture(self, topic):
		# using Professor.speak() [which in turn uses MITPerson.spreak
		return self.speak("It is obvious that " + topic)


faculty = Professor("Dr. Arrogant", 'six')
print(m1.speak("Hi There!"))  # MITPerson.speak() called
print(s1.speak("Hi There!"))  # UG.speak() called which in turn calls MITPerson.speak()
print(faculty.speak("Hi There!"))  # Professor.speak() called which in turn calls MITPerson.speak()
print(faculty.lecture("Hi There!"))  # Professor.lecture() which uses Professor.speak() which uses MITPerson.speak()
print()

'''USING CLASS THAT INCLUDES INSTANCE FROM ANOTHER CLASS'''


class Grades(object):
	"""A mapping from students to a list of grades"""
	def __init__(self):
		"""Create empty grade book"""
		self.students = []  # list of Student objects
		self.grades = {}  # maps idNum -> list of grades
		self.isSorted = True  # True if self.students is sorted

	def add_student(self, student):
		"""Assumes: 'student' is of the type
		Student Add student to the grade book"""
		if student in self.students:
			raise ValueError("Duplicate student")
		self.students.append(student)
		self.grades[student.getIdNum()] = []
		self.isSorted = False

	def add_grade(self, student, grade):
		"""Assumes: grade is a float.
		Add grade to the list of grades of student"""
		try:
			self.grades[student.getIdNum()].append(grade)
		except KeyError:
			raise ValueError("Student not in grade book")

	def get_grades(self, student):
		"""return a list of grades for a student"""
		try:  # return copy of the students grades
			return self.grades[student.getIdNum()][:]
		except KeyError:
			raise ValueError("Student not in grade book")

	def all_students(self):
		"""Return a list of the students in the grade book"""
		if not self.isSorted:
			self.students.sort()
			self.isSorted = True
		# return self.students[:] # return copy of the list of students
		for s in self.students:
			yield s


def grade_report(course):
	"""Assumes: course is of the type grades"""
	report = []
	for s in course.all_students():
		tot = 0.0
		num_grades = 0
		for g in course.get_grades(s):
			tot += g
			num_grades += 1
		try:
			average = tot/num_grades
			report.append(str(s) + '\'s mean grade is ' + str(average))
		except ZeroDivisionError:
			report.append(str(s) + ' has no grades')
	return '\n'.join(report)


ug1 = UG("Matt Daemon", 2018)
ug2 = UG("Ben Affleck", 2019)
ug3 = UG("Drew Houston", 2017)
ug4 = UG("Mark Zuckerberg", 2017)
g1 = Grad("Bill Gates")
g2 = Grad("Steve Wozniak")

six00 = Grades()
six00.add_student(g1)
six00.add_student(ug1)
six00.add_student(ug2)
six00.add_student(g2)
six00.add_student(ug3)
six00.add_student(ug4)

six00.add_grade(g1, 100)
six00.add_grade(g2, 25)
six00.add_grade(ug1, 95)
six00.add_grade(ug2, 85)
six00.add_grade(ug3, 75)

print(grade_report(six00))
print()

six00.add_grade(g1, 90)
six00.add_grade(g2, 45)
six00.add_grade(ug1, 80)
six00.add_grade(ug2, 75)

print(grade_report(six00))
print()
