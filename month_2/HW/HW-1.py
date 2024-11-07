class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def is_adult(self):
        return self.age >= "18"

    def intoduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age}, я живу в {self.city}")

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Город: {self.city}"


person1 = Person("Султан", "18", "Бишкек")
person2 = Person("Саша", "12", "Москва")
person3 = Person("Улукбек", "35", "Талас")

person1.intoduce()
person2.intoduce()
person3.intoduce()

print(person1.is_adult())
print(person2.is_adult())
print(person3.is_adult())

person4 = Person("Алия", "10", "Каракол")
print(person4)