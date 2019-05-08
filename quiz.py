class CSNLP:
    def __init__(self,x):
        self.x = x

    def common(self,y):
        # l = []
        # for char in self.x:
        #     if char in y:
        #         l.append(char)
        # return l
        return [char for char in self.x  if char in y]

obj =CSNLP("Muhammad Elgendi")
print (obj.common("Elgendi"))
