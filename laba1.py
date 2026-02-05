class Human:
    def __init__(self, name):
        self.name = name
        self.__money = 0  # Інкапсуляція (приватна змінна)

    # Метод для зміни приватних даних
    def set_money(self, amount):
        if amount >= 0:
            self.__money = amount

    # Поліморфізм (базовий метод)
    def work(self):
        print(f"{self.name} просто працює.")

class Programmer(Human):
    # Поліморфізм (той самий метод, але інша дія)
    def work(self):
        print(f"{self.name} пише код і п'є каву.")

# --- Перевірка ---
person = Human("Вася")
dev = Programmer("Іван")

# Перевіряємо поліморфізм
person.work()  # Вася просто працює
dev.work()     # Іван пише код (інша дія)

# Перевіряємо інкапсуляцію
dev.set_money(1000)
# print(dev.__money) # Це видасть помилку, бо змінна схована