# ÖRNEK 1
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype1(Prototype):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"ConcretePrototype1 with value: {self.value}"

class ConcretePrototype2(Prototype):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"ConcretePrototype2 with value: {self.value}"

# Kullanım
prototype1 = ConcretePrototype1(10)
prototype2 = ConcretePrototype2(20)

clone1 = prototype1.clone()
clone2 = prototype2.clone()

print(clone1)  # ConcretePrototype1 with value: 10
print(clone2)  # ConcretePrototype2 with value: 20

# Klonlanan nesnelerin bağımsız olduğunu kanıtlama
clone1.value = 30
print(prototype1)  # ConcretePrototype1 with value: 10
print(clone1)      # ConcretePrototype1 with value: 30


# ÖRNEK 2
import copy

class Document:
    def clone(self):
        return copy.deepcopy(self)

class Report(Document):
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Report(title={self.title}, content={self.content}, author={self.author})"

class Letter(Document):
    def __init__(self, recipient, body, sender):
        self.recipient = recipient
        self.body = body
        self.sender = sender

    def __str__(self):
        return f"Letter(recipient={self.recipient}, body={self.body}, sender={self.sender})"

# Prototip Belgeler Oluşturma
report_prototype = Report("Annual Report", "This is the annual report content.", "Alice")
letter_prototype = Letter("Bob", "Dear Bob, ...", "Alice")

# Prototiplerden Klonlanmış Belgeler Oluşturma
report_clone = report_prototype.clone()
letter_clone = letter_prototype.clone()

# Klonlanmış Belgeleri Özelleştirme
report_clone.title = "Monthly Report"
report_clone.content = "This is the monthly report content."

letter_clone.recipient = "Charlie"
letter_clone.body = "Dear Charlie, ..."

# Sonuçları Yazdırma
print(report_prototype)  # Report(title=Annual Report, content=This is the annual report content., author=Alice)
print(report_clone)      # Report(title=Monthly Report, content=This is the monthly report content., author=Alice)

print(letter_prototype)  # Letter(recipient=Bob, body=Dear Bob, ..., sender=Alice)
print(letter_clone)      # Letter(recipient=Charlie, body=Dear Charlie, ..., sender=Alice)

print("#"*100)

# ÖRNEK 3
import copy

class Department:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager

    def __str__(self):
        return f"{self.name} Department (Manager: {self.manager})"

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __str__(self):
        return f"{self.name} works in {self.department} department"

class EmployeeFactory:
    departments = {}

    @staticmethod
    def register_department(name, manager, prototype):
        EmployeeFactory.departments[name] = (manager, prototype)

    @staticmethod
    def create_employee(department_name, name):
        manager, prototype = EmployeeFactory.departments.get(department_name, (None, None))
        if manager and prototype:
            new_employee = copy.deepcopy(prototype)
            new_employee.name = name
            new_employee.department = department_name
            return new_employee
        else:
            raise ValueError(f"Department '{department_name}' not found.")

# Departmanları kaydetme
EmployeeFactory.register_department("Engineering", "Alice", Employee("John", None))
EmployeeFactory.register_department("Marketing", "Bob", Employee("Mike", None))

# Yeni çalışanlar oluşturma
engineer1 = EmployeeFactory.create_employee("Engineering", "John")
engineer2 = EmployeeFactory.create_employee("Engineering", "Jane")
marketer1 = EmployeeFactory.create_employee("Marketing", "Mike")
marketer2 = EmployeeFactory.create_employee("Marketing", "Emily")

# Sonuçları yazdırma
print(engineer1)
print(engineer2)
print(marketer1)
print(marketer2)
