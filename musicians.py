class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoing, sproing, splang")

class Drummer(Musician):
    _alive = []
    def __init__(self):
        super().__init__(["Bam", "Bang", "Blop"])
        Drummer._alive.append(self)

    def countfour(self):
        for i in range(1, 5):
            print(i)

    def spontaneous_combust(self):
        self.__alive.remove(self)

class Band(Musician):
    def __init__(self, musicians):
        Drummer.countfour()
        for i in musicians:
            i.solo(6)

    def fire_musician(self, musicians, choice):
        for i in musicians:
            if i == choice:
                musicians.remove(choice)
                print("Band drama got the best of {}.".format(choice))

    def hire_musician(self, musicians, new_musician):
        musicians.append(new_musician)




nigel = Guitarist()
nigel.solo(6)
print(nigel.sounds)
