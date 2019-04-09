import random
class warrior:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def attack(self, enemy):
        enemy.hp -= self.dmg

    def war(w1, w2):
        while (w1.hp>0 and w2.hp>0):
            n = random.random()
            if n >=0.5:
                w1.attack(w2)
                print(f'Воин {w1.name} нанес {w1.dmg} урона. У {w2.name} осталось {w2.hp} здоровья')
            else:
                w2.attack(w1)
                print(f'Воин {w2.name} нанес {w2.dmg} урона. У {w1.name} осталось {w1.hp} здоровья')
        else:
            if w1.hp<0:
                print(f'Воин {w1.name} одержал победу. У {w2.name} осталось {w2.hp} здоровья')
            if w2.hp<0:
                print(f'Воин {w2.name} одержал победу. У {w1.name} осталось {w1.hp} здоровья')

ork = warrior('Серега',100,5)
elf = warrior('Alesha', 200,7)
warrior.war(ork,elf)
