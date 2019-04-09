class Psina:
    def __init__(self, name, color):
        self.name=name
        self.color=color

    def tell(self):
        print("Я собака {0}, я имею {1} окрас".format(self.name, self.color), end="" )

    def voice(self):
        print("\nГаф")

class Taksa(Psina):
    def __init__(self, name, color, nose_color):
        Psina.__init__(self, name, color)
        self.nose_color=nose_color

    def tell(self):
        Psina.tell(self)
        print(' и цвет носа {0}'.format(self.nose_color))

    def voice(self):
        print('Тяф')


a=Psina("Ебучка", 'синий')
a.tell()
a.voice()
b=Taksa('Вонючка', 'красный', 'белый')
b.tell()
b.voice()

