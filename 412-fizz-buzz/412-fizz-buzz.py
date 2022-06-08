class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i+1) for i in range(n)]
        for i in range(2,n,3):
            print(i)
            res[i] = "Fizz"
        for i in range(4,n,5):
            res[i] = "Buzz"
        for i in range(14,n,15):
            res[i] = "FizzBuzz"
        
        return res