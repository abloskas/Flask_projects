# class MathDojo(object):
#     result = 0

#     def add(self, *nums):
#         self.result += sum(nums)
#         return self

#     def subtract(self, *nums):
#         self.result -= sum(nums)
#         return self

# md = MathDojo()
# print md.add(2).add(2,5).subtract(3,2).result        

class MathDojo(object):
    result = 0

    def add(self, *nums):
        for i in nums:
            if isinstance(i, int) or isinstance(i, float):
                self.result += i
            elif isinstance(i, tuple) or isinstance(i, list):
                self.result += sum(i)
        return self

    def subtract(self, *nums):
        for i in nums:
            if isinstance(i, int) or isinstance(i, float):
                self.result -= i
            elif isinstance(i, tuple) or isinstance(i, list):
                self.result -= sum(i) 
        return self

md = MathDojo()
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result


