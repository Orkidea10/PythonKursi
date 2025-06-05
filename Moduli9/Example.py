class Dog:
    def __init__(self, name):
        self.name=name

    def sound(self):
        print(f"{self.name} makes the sound: ham")


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: miau")


class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: Ciu")


qeni= Dog("Reksi")
macja= Cat("Tom")
zogu= Bird("Tweetie")

for kafsha in (qeni, macja, zogu):
    kafsha.sound()