class Voin():
    def __init__(self, name, sila, vinoslyvost, svet_volos):
        self.name = name
        self.sila = sila
        self.vinoslyvost = int(vinoslyvost)
        self.svet_volos = svet_volos

    def sleep(self):
        self.vinoslyvost += 2
        print(f'{self.name} уснул и восстановил винослывость. ')


    def eat(self):
        print(f"{self.name} ест")
        self.sila += 1

    def ydar(self):
        print(f"{self.name} бьёт")
        self.vinoslyvost -= 1

    def xodit(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.svet_volos}")
        print(f"cила воина - {self.sila}")
        print(f"выносливость воина - {self.vinoslyvost}")

voin1 = Voin("Олег", "56", "69", "чёрный")
voin2 = Voin("Виктор", "78", "56", "рыжий")

print(voin2.vinoslyvost)
