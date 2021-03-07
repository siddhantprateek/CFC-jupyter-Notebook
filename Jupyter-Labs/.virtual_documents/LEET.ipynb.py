first = [10, 11, 12] 


second = [4, 5]


third = first


third is first


big = [first, second]


first = [1, 5] 


big[0] is first


# reference of first will change but won't affect big
big[0]


first


s = "Siddhant"


for ch in s[1:]:
    print(ch)


# Can anybody explain me why range is inclusive in this case?
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        LR = 0
        right = 0
        left = 0
        # why range argument is inclusing in this case 
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                if s[i] == 'L':
                    left += 1
                else:
                    right += 1
            else:
                if s[i] == 'L':
                    left += 1
                else:
                    right += 1
            if left == right:
                LR += 1 
        LR += 1 
        return print(LR)
ret = Solution().balancedStringSplit("RLRRLLRLRL")
    
# but same thing done on c++ gives the right output
class Solution {
public:
    int balancedStringSplit(string s) {
        
        int LR = 0, left = 0, right = 0;
        
        for (int i = 0; i < s.length(); i++)
        {   if (s[i] == s[i + 1])
                if (s[i] == 'L')
                    left ++;
                else
                    right ++;
            else
                 if (s[i] == 'L')
                    left ++;
                else
                    right ++;
            if (left == right)
                LR ++;
        }
        return (LR);
    }
};





#    0123456879
s = "RLRRRLLRLL"


len(s)


# class Solution:
#     def balancedString(self, s: str) -> int:
#         count = 0
#         new = "" 
#         for char in s:
#             if char not in new:
#                 new += char
#             else:
#                 count += 1
#         return print(count)
    
# ret = Solution().balancedString("QQQW")


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        max_pro = 0
        for i in range(len(nums) - 1):
            for j in range(i, len(nums) - 1):
                current = (nums[i] - 1)*(nums[j + 1] - 1)
                if max_pro < current:
                    max_pro = current 
                
        return print(max_pro)
        

ret = Solution().maxProduct([1,5,4,5])





# 1450. Number of Students Doing Homework at a Given Time
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        working_students = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                working_students += 1
        return working_students    
