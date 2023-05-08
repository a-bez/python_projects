import random
class Randomaser():
    def __init__(self, low, hight):
        self.low = low
        self.hight = hight

    def func(self):
        lst = []
        for i in range(1, 6):
            if i != 0:
                randNum = random.randint(self.low, self.hight)
                if randNum == 2:
                    continue
                lst.append(randNum)
        return lst


ran = Randomaser(1, 5)
print(ran.func())