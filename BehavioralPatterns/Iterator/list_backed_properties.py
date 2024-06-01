# ÖRNEK 1
class ListBackedProperty:
    def __init__(self):
        self._values = []

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, new_values):
        if not isinstance(new_values, list):
            raise ValueError("Values must be a list.")
        self._values = new_values

    def add_value(self, value):
        self._values.append(value)

# Kullanım
obj = ListBackedProperty()
obj.values = [1, 2, 3]
print(obj.values)  # [1, 2, 3]

obj.add_value(4)
print(obj.values)  # [1, 2, 3, 4]

try:
    obj.values = "not a list"  # ValueError fırlatır
except ValueError as e:
    print(e)

print("#"*70)

# ÖRNEK 2
class Student:
    def __init__(self, name):
        self.name = name
        self._grades = []

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, new_grades):
        if not isinstance(new_grades, list):
            raise ValueError("Grades must be a list.")
        if not all(isinstance(grade, (int, float)) for grade in new_grades):
            raise ValueError("All grades must be numbers.")
        self._grades = new_grades

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a number.")
        self._grades.append(grade)

    def average_grade(self):
        return sum(self._grades) / len(self._grades) if self._grades else 0.0

# Kullanım
student = Student("John Doe")
student.grades = [90, 85, 88]
print(f"{student.name}'s grades: {student.grades}")
print(f"Average grade: {student.average_grade():.2f}")

student.add_grade(92)
print(f"Updated grades: {student.grades}")
print(f"Updated average grade: {student.average_grade():.2f}")

try:
    student.grades = "not a list"  # ValueError fırlatır
except ValueError as e:
    print(e)

try:
    student.add_grade("not a number")  # ValueError fırlatır
except ValueError as e:
    print(e)
