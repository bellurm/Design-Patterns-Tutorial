# ÖRNEK 1
class Person:
    def __init__(self):
        # ad-soyad bilgileri
        self.name = None
        self.surname = None
        
        # okuduğu fakülte ve bölüm bilgisi
        self.faculty = None
        self.department = None
        
        # çalıştığı şirket ve pozisyonu
        self.company = None
        self.position = None
        
        # yıllık olarak kazandığı para
        self.earn = None
    
    def __str__(self):
        return (f"{self.name} {self.surname} studied {self.department} at the {self.faculty}"
                f"He works as a {self.position} at {self.company} and earns {self.earn} per year :D.")
    
class EmployeeBuilder:
    def __init__(self):
        self.employee = Person()
    
    def info(self):
        return PersonInfoBuilder(self.employee, self)
    
    def whereStudied(self):
        return PersonStudied(self.employee, self)
    
    def whereWorking(self):
        return PersonWorking(self.employee, self)
    
    def howMuchEarning(self):
        return PersonEarning(self.employee, self)
    
    def build(self):
        return self.employee

class PersonInfoBuilder:
    def __init__(self, employee, parent_builder):
        self.employee = employee
        self.parent_builder = parent_builder
    
    def name(self, name):
        self.employee.name = name
        return self

    def surname(self, surname):
        self.employee.surname = surname
        return self

    def done(self):
        return self.parent_builder

class PersonStudied:
    def __init__(self, employee, parent_builder):
        self.employee = employee
        self.parent_builder = parent_builder
    
    def faculty(self, faculty):
        self.employee.faculty = faculty
        return self
    
    def department(self, department):
        self.employee.department = department
        return self
    
    def done(self):
        return self.parent_builder

class PersonWorking:
    def __init__(self, employee, parent_builder):
        self.employee = employee
        self.parent_builder = parent_builder
    
    def company(self, company):
        self.employee.company = company
        return self
    
    def done(self):
        return self.parent_builder
    
class PersonEarning:
    def __init__(self, employee, parent_builder):
        self.employee = employee
        self.parent_builder = parent_builder
    
    def earning(self, earning):
        self.employee.earning = earning
        return self

    def done(self):
        return self.parent_builder
    
builder = EmployeeBuilder()

person = (builder
          .info().name("Cyber").surname("Worm").done()
          .whereStudied().faculty("Business Administration").department("Management Information Systems").done()
          .whereWorking().company("xxx").done()
          .howMuchEarning().earning("nothing :D").done()
          .build())

print(person)


# ÖRNEK 2
class Person:
    def __init__(self):
        # Temel Bilgiler
        self.name = None
        self.surname = None
        
        # Adres Bilgileri
        self.street_address = None
        self.city = None
        self.postcode = None
        
        # İş Bilgileri
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return (f"{self.name} {self.surname} lives at {self.street_address}, {self.city}, {self.postcode}. "
                f"Works at {self.company_name} as a {self.position}, earning {self.annual_income} annually.")

class PersonBuilder:
    def __init__(self):
        self.person = Person()
    
    def info(self):
        return PersonInfoBuilder(self.person, self)
    
    def lives(self):
        return PersonAddressBuilder(self.person, self)
    
    def works(self):
        return PersonJobBuilder(self.person, self)
    
    def build(self):
        return self.person

class PersonInfoBuilder:
    def __init__(self, person, parent_builder):
        self.person = person
        self.parent_builder = parent_builder

    def name(self, name):
        self.person.name = name
        return self

    def surname(self, surname):
        self.person.surname = surname
        return self

    def done(self):
        return self.parent_builder

class PersonAddressBuilder:
    def __init__(self, person, parent_builder):
        self.person = person
        self.parent_builder = parent_builder

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def in_city(self, city):
        self.person.city = city
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def done(self):
        return self.parent_builder

class PersonJobBuilder:
    def __init__(self, person, parent_builder):
        self.person = person
        self.parent_builder = parent_builder

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self

    def done(self):
        return self.parent_builder

builder = PersonBuilder()

person = (builder
          .info().name("Cyber").surname("Worm").done()
          .lives().at("1234 Elm Street").in_city("Springfield").with_postcode("12345").done()
          .works().at("Initech").as_a("Network Sec. Specialist").earning("nothing :D").done()
          .build())

print(person)
