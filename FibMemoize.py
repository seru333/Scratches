class Memoize:
    def __init__(self, entry):
        self.entry = entry
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.entry(*args)
        return self.memo[args]
@Memoize
def fib(n):
    if type(n) != int:
        return print("please enter and integer")
    if n < 1:
        return print("not a positive integer")
    if n == 1 or n == 2:
        answer = 1
    else:
        answer = fib(n - 2) + fib(n - 1)
    return answer

if __name__ == '__main__':
    assert fib(7) == 13
    for i in range(1, 50):
        print(i, ":", fib(i))
    fib(-1)
    fib("one")