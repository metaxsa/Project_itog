 print('Задание 1')

def card_num(t):
    print('**** **** ****', t[::-4])


     print(card_num)
 t=(input('введите номер карты'))
 card_num(t)

 print('_______')
 print("задание 2")

 a=(input("ввести слово"))
 def polindrom():


     b = a.split()
     b = ''.join(b)

     if b[::1] == b[::-1]:
         print("палиндром")
     else:
         print("не палиндром")


 polindrom()
 print('____________')
 print('задание 3')


class Tomato:
    states= {1:'small',2:"middle", 3:'high'}
    def __init__(self,_index,):
        self._index= _index
        self._state=0
    def grow(self):
        self._state+=1
    def is_ripe(self):
        if self._state==3:
            print('томат созрел')
class TomatoBush:

    def __init__(self,num):
        self.tomatoes=[Tomato(index) for index in range(1,num)]
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
            print(i._state)
    def all_are_ripe(self):
        for i in self.tomatoes:
            i.is_ripe()
        return True

    def give_avay_all(self):
        self.tomatoes=[]
        print(self.tomatoes)

class Gardener:
    def __init__(self,name,plant):
        self.name=name
        self._plant=plant

    def work(self):
        self._plant.grow_all()
    def harvest(self):
        if self._plant.all_are_ripe:
            self._plant.give_avay_all()

        else:
            print("урожай не созрел")




    @staticmethod
    def knowledge_base():
        print('информация по саду')

if __name__ == '__main__':
    Gardener.knowledge_base()
    a = TomatoBush(4)
    b = Gardener('Artur',a)
    b.work()
    b.harvest()






