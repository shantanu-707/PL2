# Base class
class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def introduce(self):
        print(self._name)
        print(self._age)

class Employee(Person):
    def __init__(self, empl_id, salary, name, age):
        super().__init__(name, age)
        self._empl_id = empl_id
        self._salary = salary

    def get_employee_info(self):
        print(self._name)
        print(self._age)
        print(self._empl_id)
        print(self._salary)

class Manager(Employee):
    def __init__(self, dept, empl_id, salary, name, age):
        super().__init__(empl_id, salary, name, age)
        self._dept = dept


    def get_manager_info(self):
        print(self._dept)
        print(self._name)
        print(self._age)
        print(self._empl_id)
        print(self._salary)


x = Employee("123","20000","Mike","Olsen")
y = Person("Ty","18")
y.introduce()
x.get_employee_info()