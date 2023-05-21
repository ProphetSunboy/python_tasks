class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        '''
        Given an integer n, return a string array answer (1-indexed) where:

            answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
            answer[i] == "Fizz" if i is divisible by 3.
            answer[i] == "Buzz" if i is divisible by 5.
            answer[i] == i (as a string) if none of the above conditions are true.
            
        '''
        answer = [''] * n
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                answer[i] = 'FizzBuzz'
            elif (i+1) % 3 == 0:
                answer[i] = 'Fizz'
            elif (i+1) % 5 == 0:
                answer[i] = 'Buzz'
            else:
                answer[i] = str(i+1)
        return answer