class Testclass:
    def __init__(self):
        self.a = 0

    def testmethod(self, x):
        x = x + 1
        self.a = self.a + 1
        if x <= 3:
            x = self.testmethod(x)
        else:
            return x
        print(x)


a = Testclass()
a.testmethod(1)
