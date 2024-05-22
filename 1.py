def r1():
    class Restauran():
        def __init__(self, restauran_name, kuhni_type):
            self.restauran_name = restauran_name
            self.kuxni_type = kuhni_type

        def describe_restauran(self):
            print('Имя ресторана: ', self.restauran_name)
            print('Тип кухни: ', self.kuxni_type)

        def open_restauran(self):
            print('Ресторан открыт')

    newRestauran = Restauran('Мама Рома', 'Итальянская')
    newRestauran.describe_restauran()
    newRestauran.open_restauran()

def r2():
    class Restauran():
        def __init__(self, restauran_name, kuhni_type):
            self.restauran_name = restauran_name
            self.kuhni_type = kuhni_type

        def describe_restauran(self):
            print('Имя ресторана: ', self.restauran_name)
            print('Тип кухни: ', self.kuhni_type)

        def open_restauran(self):
            print('Ресторан открыт')

    restauran1 = Restauran('Рыбка', "Рыбный ресторан")
    restauran2 = Restauran("Круассан", "Французская")
    restauran3 = Restauran('Мама Рома', "Итальянская")

    restauran1.describe_restauran()
    print('\n')
    restauran2.describe_restauran()
    print('\n')
    (restauran3.describe_restauran())

def r3():
    class Restauran():
        def __init__(self, restauran_name, kuhni_type, rating):
            self.restauran_name = restauran_name
            self.kuhni_type = kuhni_type
            self.rating = rating

        def describe_restauran(self):
            print('Имя ресторана: ', self.restauran_name)
            print('Тип кухни: ', self.kuhni_type)
            print('Рейтинг ', self.rating)

        def open_restauran(self):
            print('Ресторан открыт')

        def rating(self,new_rating):
            self.rating = new_rating

    restauran1 = Restauran('Папакарня', "Выпечка", 3.9)
    restauran2 = Restauran("Куассо", "Французская", 4.5)
    restauran3 = Restauran('Мак утка', "ФастФуд", 3.1)

    restauran1.describe_restauran()
    print('\n')
    restauran2.describe_restauran()
    print('\n')

r3()
