

def my_findMedianSortedArrays(nums1:list, nums2:list):

    nums = nums1 + nums2
    #nums = sorted(nums)

    n = len(nums)
    # n 是奇数还是偶数
    for i in range(n):

        if len(nums) == 2:
            return sum(nums)/2  # 退出循环

        if len(nums) == 1:
            return sum(nums)
        max_num = max(nums)
        min_num = min(nums)
        nums.remove(max_num)
        nums.remove(min_num)





if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,4]

    result = my_findMedianSortedArrays(nums1,nums2)
    print(result)