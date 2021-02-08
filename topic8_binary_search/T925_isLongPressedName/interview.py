'''
    925. 长按键入

    你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

    你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

    示例 1：

    输入：name = "alex", typed = "aaleex"
    输出：true
    解释：'alex' 中的 'a' 和 'e' 被长按。
    示例 2：

    输入：name = "saeed", typed = "ssaaedd"
    输出：false
    解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
    示例 3：

    输入：name = "leelee", typed = "lleeelee"
    输出：true
    示例 4：

    输入：name = "laiden", typed = "laiden"
    输出：true
    解释：长按名字中的字符并不是必要的。
'''
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # 定义指针，分别指向 name 和 typed 的首字符
        p = 0
        q = 0

        m = len(name)
        n = len(typed)
        # 遍历 typed 与 name 中的字符比较
        while q < n:
            # 比较，相同移动指针
            if p < m and name[p] == typed[q]:
                p += 1
                q += 1
            # 不相同时，要注意 p 指针指向的元素
            # 如果是首元素，那么表示 name 和 typed 首字符都不同，可以直接返回 False
            # 如果不在首元素，看是否键入重复，键入重复，继续移动 q 指针，继续判断；如果不重复，也就是不相等的情况，直接返回 False，表示输入错误
            elif p > 0 and name[p-1] == typed[q]:
                q += 1
            else:
                return False
        
        # typed 遍历完成后要检查 name 是否遍历完成
        return p == m

if __name__ == "__main__":
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            res = solution.isLongPressedName(str1,str2)
            print(res)
        else:
            break

