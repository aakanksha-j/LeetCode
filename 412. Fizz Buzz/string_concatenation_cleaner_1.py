class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # if in future alongwith 3, 5 .. 7, etc. are added
        
        # time O(N)
        # space O(1)
        
        output = []
        for i in range(1, n + 1):
            num_ans_str = ''
            
            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)
            
            if divisible_by_3:
                num_ans_str += 'Fizz'
            if divisible_by_5:
                num_ans_str += 'Buzz'
            if not num_ans_str:
                num_ans_str = str(i)
                
            output.append(num_ans_str)
            
        return output