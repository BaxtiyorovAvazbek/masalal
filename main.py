# 1-masala
# 2-masala
# 3-masala
# class Calculator:
#     def __init__(self, son1, son2):
#         self.son1 = son1
#         self.son2 = son2
#     def qoshish(self):
#         return self.son1 + self.son2
#     def ayirish(self):
#         return self.son1 - self.son2
#     def kopaytirish(self):
#         return self.son1 * self.son2
#     def bolish(self):
#         return self.son1 // self.son2
#
#
# calculator1 = Calculator(10, 5)
# calculator2 = Calculator(10, 5)
# calculator3 = Calculator(10, 5)
# calculator4 = Calculator(10, 5)
# print(calculator1.qoshish())
# print(calculator2.ayirish())
# print(calculator3.kopaytirish())
# print(calculator4.bolish())
# 4-masala
# 5-masala
# class Player:
#     def __init__(self, name, num, num2, num3):
#         self.name = name
#         self.num = num
#         self.num2 = num2
#         self.num3 = num3
#     def get_age(self):
#         return f"{self.name} is age {self.num}"
#     def get_height(self):
#         return f"{self.name} is {self.num2}cm"
#     def get_weight(self):
#         return f"{self.name} weighs {self.num3}kg"
#
#
# p1 = Player("David Jones", 25, 175, 75)
# print(p1.get_age())
# print(p1.get_height())
# print(p1.get_weight())
# 6-masala
# class Employee:
#     def __init__(self, name, name2):
#         self.name = name
#         self.name2 = name2
#
#     def fullname(self):
#         return self.name + self.name2
#     def email(self):
#         x = self.name.lower()
#         y = self.name2.lower()
#         return f"{x}.{y}@company.com"
#
#     def firstname(self):
#         return self.name
#
#
# emp_1 = Employee("John", "Smith")
# emp_2 = Employee("Mary",  "Sue")
# emp_3 = Employee("Antony", "Walker")
# print(emp_1.fullname())
# print(emp_2.email())
# print(emp_3.firstname())
# 7-masala
# class Name:
#     def __init__(self, name, name2):
#         self.name = name
#         self.name2 = name2
#     def fname(self):
#         return self.name.capitalize()
#     def Iname(self):
#         x = self.name2.lower()
#         return x.capitalize()
#     def fullname(self):
#         y = self.name.capitalize()
#         m = self.name2.lower()
#         return y + m.capitalize()
#     def initials(self):
#         n = self.name.capitalize()
#         return f"{n[0:1]}.{self.name2[0:1]}"
#
#
# a1 = Name("john", "SMITH")
# print(a1.fname())
# print(a1.Iname())
# print(a1.fullname())
# print(a1.initials())
# 8-masala
# 9-masala
# class HP:
#     def __init__(self, name1, name2):
#         self.name1 = name1
#         self.name2 = name2
#     def title(self):
#         return self.name1
#     def author(self):
#         return self.name2
#     def get_title(self):
#         return f"Title: {self.name1}"
#     def get_author(self):
#         return f"Author: {self.name2}"
#
#
# hp1 = HP("Pride and Prejudice", "Jane Austen")
# hp2 = HP("Hamlet", "William Shakespeare")
# hp3 = HP("War and Peace", "Leo Tolstoy")
# print(hp1.title())
# print(hp1.author())
# print(hp1.get_title())
# print(hp1.get_author())
# 10-masala
# 11-masala
# class Person:
#     def __init__(self, name, n1, n2):
#         self.name = name
#         self.n1 = n1
#         self.n2 = n2
#
#     def taste1(self, n1):
#         return f"{self.name} eats the {n1} and loves it!"
#     def taste2(self, name2):
#         return f"{self.name} eats the {name2}!"
#     def taste3(self, n2):
#         return f"{self.name} eats the {n2} and hates it!"
#
#
# p1 = Person("Sam", ["ice cream"], ["carrots"])
# print(p1.taste1("ice cream"))
# print(p1.taste2("cheese"))
# print(p1.taste3("carrots"))
# 12-masala
# 13-masala
# class Programmer:
#     def __init__(self, num, num2):
#         self.num = num
#         self.num2 = num2
#
#     def salary(self):
#         return self.num
#     def work_hours(self):
#         return self.num2
#     def __del__(self):
#         print(f"oof, {self.num}, {self.num2}")
#
#
# prog = Programmer(25000, 5)
# print(prog.salary())
# print(prog.work_hours())
# del prog
# 14-masala