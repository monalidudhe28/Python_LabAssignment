class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0
        self.address = ""

    def get_input(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def display(self):
        print(self.name, self.age, self.salary, self.address)


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = ""

    def get_input(self):
        super().get_input()
        self.department = input("Enter department: ")

    def display(self):
        super().display()
        print(self.department)


managers = []

for i in range(10):
    print(f"\nManager {i+1}")
    m = Manager()
    m.get_input()
    managers.append(m)

print("\nDetails:")
for m in managers:
    m.display()
