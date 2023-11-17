

class Packet:
    def __init__(self, version_ID, type_ID, contents):
        self.version_ID = version_ID
        self.type_ID = type_ID
        self.contents = contents

    def compute(self):
        if self.type_ID == 0:
            return self.summation()
        elif self.type_ID == 1:
            return self.product()
        elif self.type_ID == 2:
            return self.minimum()
        elif self.type_ID == 3:
            return self.maximum()
        elif self.type_ID == 4:
            return self.contents
        elif self.type_ID == 5:
            return self.greater_than()
        elif self.type_ID == 6:
            return self.less_than()
        elif  self.type_ID == 7:
            return self.equal_to()

    def summation(self):
        ans = 0
        for val in self.contents:
            ans += val.compute()
        return ans

    def product(self):
        ans = 1
        for val in self.contents:
            ans *= val.compute()
        return ans

    def minimum(self):
        ans = self.contents[0].compute()
        for val in self.contents[1:]:
            ans = min(ans, val.compute())
        return ans

    def maximum(self):
        ans = self.contents[0].compute()
        for val in self.contents[1:]:
            ans = max(ans, val.compute())
        return ans
    
    def greater_than(self):
        return self.contents[0].compute() > self.contents[1].compute()
    
    def less_than(self):
        return self.contents[0].compute() < self.contents[1].compute()

    def equal_to(self):
        return self.contents[0].compute() == self.contents[1].compute()