"""
    该案例演示了栈应用的leetcode题
    （1）题目描述
    给定一个只包括“(”，“)”，“[”，“]”，“{”，“}”的字符串s，判断字符串是否有效。
    有效字符串需满足：
    	左括号必须用相同类型的右括号闭合。
    	左括号必须以正确的顺序闭合。
    	每个右括号都有一个对应的相同类型的左括号。
    （2）示例
    示例 1：
    输入：s = "()"
    输出：true
    示例 2：
    输入：s = "()[]{}"
    输出：true
    示例 3：
    输入：s = "(]"
    输出：false
    示例 4：
    输入：s = "([])"
    输出：true
    （3）思路分析
    遇到左括号则入栈，遇到右括号则出栈一个左括号与之匹配，如果能够匹配则继续，如果匹配失败或者栈为空则返回False。

"""
class Solution:
    def isValid(self, s):
        # 定义一个栈（用list模拟）
        stack = []
        # 遍历字符串  获取当前字符串中的一个个字符
        for char in s:
            match char:
                case "("|"["|"{":
                    # 如果是左括号，将字符放到栈中
                    stack.append(char)
                case ")":
                    if (not stack) or (stack.pop() != "("):
                        return False
                case "]":
                    if (not stack) or (stack.pop() != "["):
                        return False
                case "}":
                    if (not stack) or (stack.pop() != "{"):
                        return False
        return True if not stack else False
