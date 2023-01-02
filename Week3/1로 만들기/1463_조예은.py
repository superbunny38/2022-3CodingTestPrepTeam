import sys


class MakeOne:
    def __init__(self, n) -> None:
        self.record = {0: -1}
        self.op = [self.Divide(3), self.Divide(2)]
    
    class Divide:
        def __init__(self, n) -> None:
            self.num = n
        def __call__(self, n):
            return n // self.num, n % self.num
    
    def __call__(self, n):
        candidate = list()
        if n <= 1:
            r = 0
        else:
            for op in self.op:
                prev, rest = op(n)
                prev = self.record[prev] if prev in self.record else self.__call__(prev)
                candidate.append(prev + rest + 1)
            r = min(candidate)
        self.record[n] = r
        return r

                
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    one = MakeOne(n)
    print(one(n))