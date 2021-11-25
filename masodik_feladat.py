class Counter:
    def __init__(self, value):
        self.value = value
        self.step = 1

    def increment(self):
        self.value += self.step

    def decrement(self):
        self.value -= self.step

    def set_value(self, value):
        self.value = value

    def set_step(self, step):
        self.step = step

    def get_value(self):
        print(self.value)


myCounter = Counter(10)
myCounter.increment()
myCounter.increment()
myCounter.get_value()  #12
myCounter.set_step(5)
myCounter.decrement()
myCounter.get_value()  #7
myCounter.set_value(100)
myCounter.increment()
myCounter.get_value()  #105


class ScoreCounter(Counter):
    def __init__(self, value, name, age):
        super().__init__(value)  # öröklődés a Counterből
        self.name = name
        self.age = age
        self.winner = False

    def get_value(self):
        if self.value() >= 12:
            self.winner = True
        else:
            self.winner = False
        return super().get_value()


myScoreCounter = ScoreCounter(10, 'Zsolt', 34)
myScoreCounter.increment()
myScoreCounter.get_value()
myScoreCounter.increment()
myScoreCounter.get_value()
print(myScoreCounter.winner)