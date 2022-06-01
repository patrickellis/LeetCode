import threading

class FizzBuzz(threading.Thread):
    def __init__(self, printer, gap, bound, result):
        threading.Thread.__init__(self)
        self.printer = printer
        self.gap = gap
        self.bound = bound
        self.result = result
        self.current = gap-1

    def run(self):
        while self.current < self.bound:
            self.result[self.current] = self.printer(self.current+1)
            self.current += self.gap

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = list(map(str, range(1, n+1)))
        threads = [
            FizzBuzz(lambda i: 'FizzBuzz' if i % 5 == 0 else 'Fizz', 3, n, result),
            FizzBuzz(lambda i: 'FizzBuzz' if i % 3 == 0 else 'Buzz', 5, n, result),
        ]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        return result