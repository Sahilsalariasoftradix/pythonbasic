from OopsDemo import Calculator  # this is how the


class ChildImp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 3)

    def getcomleteData(self):
        return self.num2 + self.num + self.Summation()


Obj = ChildImp()
print(Obj.getcomleteData())
