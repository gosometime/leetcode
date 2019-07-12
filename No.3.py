
'''
存在的问题：
1、逻辑不完整，条理不清晰
2、没有考虑，字符串没有重复的情况
3、没有考虑，最后一个子字符串就是最长字符串的情况（一直到末尾）
4、对结束的条件没有充分考虑

'''

s = 'abc'

a = ord(s[0])
#print(a)

n = [1 ,2,3,2]
n = n[1+1:]
#print(n)

def my_lengthOfLongestSubstring(s):
    cnt = 0
    L = []
    num = []
    for i in range(len(s)):
        j = ord(s[i])   # 转换为整数
        if j not in L:
            L.append(j) # 位置放错，最初放在if前面，逻辑不清晰
            #print(L)
            cnt += 1
        else:
            num.append(cnt)
            #print(num)
            L.append(j)         # 缺少，逻辑不清晰
            index = L.index(j)  # 获取第一个匹配元素的索引值
            L = L[index+1:]     # 舍弃前面重复字符以及它之前的字符
            cnt = len(L)
            #print(L)
    # 针对问题2/3，这类问题，可以通过调整思路来避免
    #2、没有考虑，字符串没有重复的情况
    #3、没有考虑，最后一个子字符串就是最长字符串的情况（一直到末尾）
    if len(num) != 0:
        if len(L) > max(num):
            MAX = len(L)
        else:
            MAX = max(num)
    else:
        MAX = len(L)

    return MAX

# 滑动窗口法
# 思路：
# 采用set集合，从字符串第0个元素开始，while循环判断是否在集合中，如果在，则移除集合中最左边的元素。
# 同时增减集合中元素个数。每次跳出while循环，判断当前集合元素个数是否为比max_len大，如果大，则更新max_len为当前元素个数。
# 将当前元素添加到集合中。
def lengthOfLongestSubstring_1(s):
    if len(s) == 0:
        return 0
    max_len = 0
    cur_len = 0

    q = set()
    n = len(s)
    left = 0
    for i in range(n):
        while s[i] in q:       # 很关键
            q.remove(s[left])  # 按照进入的顺序进行移除，跟存储没关系(set存储元素的顺序不是按进入先后来的)
            left += 1          #
            cur_len -= 1
        #print(q)
        q.add(s[i])
        cur_len += 1           # 放在更新max_len之前
        if cur_len > max_len:
            max_len = cur_len

    return max_len








if __name__ =='__main__':
    s = 'abcabcbb'

    l = my_lengthOfLongestSubstring(s)
    ll = lengthOfLongestSubstring_1(s)
    print(l)
    print(ll)