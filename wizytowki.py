from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    def __repr__(self):
        return f"Contact({self.name}, {self.email}, {self.phone_number})"

    def contact(self):
        return f"Wybieram numer {self.phone_number} i dzwonie do {self.name}"

    def label_lenght(self):
        return len(self.name)
        
    def label_count(self):
        return count(self.name)


class BusinessContact(BaseContact):
   def __init__(self, max_load, role, company, company_phone,  *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load
       self.role = role
       self.company = company
       self.company_phone = company_phone

def create_contact(kind, quantity):
    if kind == "business":
        return BusinessContact(name=fake.name(), email=fake.email(), phone_number=fake.phone_number())
    else:
        return BaseContact(name=fake.name(), email=fake.email(), phone_number=fake.phone_number())


base_contacts=[]
for person in range(5):
    person= BaseContact(name=fake.name(), email=fake.email(), phone_number=fake.phone_number())
    print(person.contact(),person.label_lenght())
    base_contacts.append(person)



sort_name = sorted(base_contacts, key=lambda BaseContact: BaseContact.name)
print(*sort_name, sep = "\n") 

business_contacts=[]
for person in range(5):
    person= BusinessContact(name=fake.name(), email=fake.email(), phone_number=fake.phone_number())
    business_contacts.append(person)

sort_name = sorted(business_contacts, key=lambda BusinessContact: BusinessContact.name)
print(*sort_name, sep = "\n") 

sort_name = sorted(base_contacts, key=lambda Contact: Contact.name)
print(*sort_name, sep = "\n") 

