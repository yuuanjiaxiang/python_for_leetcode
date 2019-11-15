# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution:
    @classmethod
    def twoSum(self,nums, target):
        dic={}
        for i,item in enumerate(nums):
            if target-item in dic:
                return [dic[target-item],i]
            dic[item] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution.twoSum(nums,target)
    print(result)

# 29 / 29 个通过测试用例
# 状态：通过
# 执行用时：56 ms
# 我的提交执行用时
# 已经战胜 98.99 % 的 python3 提交记录

# 主要通过