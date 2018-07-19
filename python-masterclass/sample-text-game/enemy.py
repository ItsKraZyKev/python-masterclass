import random


class Enemy:

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self._name = name
        self._hit_point = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_point - damage
        if remaining_points >= 0:
            self._hit_point = remaining_points
            print(f'{self._name} took {damage} points damage and has {self._hit_point} left.')
        else:
            self._lives -= 1
            if self._lives > 0:
                print(f'{self._name} took too much damage and lost a life, he has {self._lives} remaining.')
            else:
                print(f'{self._name} is dead')
                self._alive = False

    def __str__(self):
        return f'Name: {self._name}, Lives: {self._lives}, Hit Points: {self._hit_point}'


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=23, lives=1)

    def grunt(self):
        print(f'Me {self._name}! {self._name} stomp you!!')


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print(f'***** {self._name} dodges *****')
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name)
        self._hit_point = 140

    def take_damage(self, damage):
        super().take_damage(damage//4)















