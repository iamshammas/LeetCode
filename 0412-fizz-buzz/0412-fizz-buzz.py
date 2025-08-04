class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        for i in range(1,n+1):
            answer.append(i)
        k = len(answer)
        for j in range(k):
            if answer[j] % 3 == 0 and answer[j] % 5 == 0:
                answer[j] = "FizzBuzz"
            elif answer[j] % 3 == 0:
                answer[j] = "Fizz"
            elif answer[j] % 5 == 0:
                answer[j] = "Buzz"
            else:
                answer[j] = str(answer[j])
        return answer
        """
        :type n: int
        :rtype: List[str]
        """
        