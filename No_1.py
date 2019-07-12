'''
No.1
两数之和

'''

class two_Sum():
    #我的答案
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            print(i)
            a = target - nums[i]
            # 没有考虑两个数相同的情况，比如3+3=6
            # 没有考虑a不在nums中的情况，比如6-2=4
            p = []
            if a in nums:
                p.append(nums.index(a))
                print(p)
                if p[-1] != i:
                    return [i, p[-1]]
                else:
                    continue

    def twoSum1(self,nums, target):
        dict1 = {}
        for i, m in enumerate(nums):    # 模拟哈希？
            dict1[m] = i
            print(m, i)
        print('dict1',dict1)    # dict1 {3: 2, 2: 1}    ??
        print(dict1[3])
        for i, m in enumerate(nums):
                j = dict1.get(target - m)
                if j !=None and j != i:
                    return [i, j]

    def twoSum2(self,nums, target):
        dict2 = {}
        for i, m in enumerate(nums):

            if dict2.get(target - m) is not None:
                return [i, dict2.get(target - m)]
            dict2[m] = i    # 不能放if前面，保证不会返回的两个索引值相同



if __name__ == "__main__":
    list = [3, 2, 3]

    fun = two_Sum()
    print('result:',fun.twoSum(list, 6))
    fun.twoSum1(list, 6)

    print('result1:', fun.twoSum1(list, 6))

