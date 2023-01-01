import sys


class Fibonacci:
    def __init__(self, n) -> None:
        self.curr = 0
        self.next = 1
        self.current = 0
        self.stop = n + 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            r = self.curr
            self.curr = self.next
            self.next += r
            self.current += 1 
            return r
        else:
            raise StopIteration

                
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    fibo = Fibonacci(n)
    for i in fibo:
        pass
    print(i)