## twoSum
× iterate the whole list for every num
√ hash
```py
class Solution:
    def twoSum(self, nums, target):
        ht = {}     # initiallize!!!
        for i, num in enumerate(nums): 
            if num in ht:
                return [i, ht[num]]
            ht[target - num] = i 
```

## addTwoNumbers
LinkList -> dummy head!!!
```py
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        co = 0
        res = ListNode()
        cur = res
        while l1 != None or l2 != None:
            cur.next = ListNode()
            cur = cur.next
            s = co
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            if s >= 10:
                co = 1
                cur.val = s - 10
            else:
                co = 0
                cur.val = s

        if co == 1:
            cur.next = ListNode(1, None)
        return res.next 
```

## lengthOfLongestIndex
| cases  | expected  |remark|
|---|---|---|
|  "abac" | 3  |当出现重复字符时，应当从上一出现位置的下一个开始重新计算，而不是第二次出现的位置|
| " "|1|不能等出现重复了才统计字符|


```py
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        max_len = 0
        left = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
    
        return max_len
```
substring:
- left & right + char_index √
    ```py
    if char in char_index and char_index[char] >= left: 
        left = char_index[char] + 1     # O(N)
        ...
    ```
- substr[] ×
    ```py
    if cur_char in substr:  
        pos = substr.index()    # O(N^2)
        substr = substr[pos + 1:] + [letter]    
    ...
    ```
  
max_len:
- max_len √
- max(possible_max_lens) ×

## longestPalindrome
2 simplest cases:
- even length: "aa"
- odd length: "a"

then try to extend them 
```py
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        max_str = []
        for cur in range(len(s)):
            right = cur
            left = right - 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if left >= -1 and right - left - 1 > max_len:
                max_len = right - left - 1
                max_str = s[left + 1 : right]

            right = cur
            left = right 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if left >= -1 and right - left - 1 > max_len:
                max_len = right - left - 1
                max_str = s[left + 1 : right]

        return "".join(max_str)
```
⚠️loop variable cannot be reassigned within the loop 
```py
for right in range(len(s)):
    ...
    right += 1
    ...
```

## convert (zigzag)
### compressed matrix
```py
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        lists = [[] for _ in range(numRows)]

        row = 0     # 一组是2*numRow-2, 0~numRow-1 往下，numRow-1~2*numRow-2 往上
        for char in s:
            if row < numRows:
                lists[row].append(char)
            else:
                lists[2 * numRows - row - 2].append(char)

            row = (row + 1) % (2 * numRows - 2)
            
        res = []
        for row in lists:
            for elem in row:
                res.append(elem)
        return "".join(res)
```
black box!
API!
只需要返回按行输出的结果
中间过程不需要真的存储
```
P   A   H   N
A P L S I I G
Y   I   R
```
### direct construction
```py
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        ans = []
        for i in range(r):  # 枚举矩阵的行
            for j in range(0, n - i, t):  # 枚举每个周期的起始下标
                ans.append(s[j + i])  # 当前周期的第一个字符
                if 0 < i < r - 1 and j + t - i < n:
                    ans.append(s[j + t - i])  # 当前周期的第二个字符
        return ''.join(ans)
```

## isPalindrome
```py
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        rev = 0
        while x > rev:
            x, rev = x // 10, rev * 10 + x % 10

        return x == rev or x == rev // 10
```

## longestConsecutive
`set`, `map` are implemented as hash tables
time complexity for searching and inserting are $O(1)$ 
```py
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1 
                target = num + 1
                while target in num_set:
                    length, target = length + 1, target + 1
                max_len = max(max_len, length)
        return max_len
```

## moveZeros
找到 0 ，删掉，末尾加一个 0 ×
```py
if nums[i] == 0:
nums.pop(i)
nums.append(0)
```
修改正在遍历的数组很危险
--> 找到所有 0 的位置后删除
```py
nums.pop(zeros[zero - i])
```
bad space complexity 


移动窗口和双指针：
交换 0 block 的第一个 0 和 0 block 之后的第一个非 0 数
time complexity of swap: $O(1)$，不会影响总体时间复杂度

```py
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        while right < len(nums):
            if nums[right] == 0 and nums[left] != 0:
                left = right
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
```

## maxArea
Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.

利用一些性质筛选出所有可能 ($O(N^2)$) 中的一部分
```py
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            water = (right - left) * min(height[left], height[right])
            if water > max_water:
                max_water = water
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_water
```