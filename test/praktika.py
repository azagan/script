class Person:
    def __init__(self, imya, familiya, specialnos = 1):
        self.im = imya
        self.fam = familiya
        self.spec = specialnos

    def tell(self):
        print("Сотрудник {0} {1} имеющий {2} квалификацию".format(self.im, self.fam, self.spec) )

    def __del__(self):
        print("До свидания мистер {0} {1}".format(self.im,self.fam))

p1=Person('Семен', 'Семенович')
p2=Person('Иван', 'Иваныч', 2)
p3=Person('Игорь', 'Игорич')
p1.tell()
p2.tell()
p3.tell()
n=input()