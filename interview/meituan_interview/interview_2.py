'''
   题目描述：
有一款叫做空间回廊的游戏，游戏中有着n个房间依次相连，如图，1号房间可以走到2号房间，以此类推，n号房间可以走到1号房间。



这个游戏的最终目的是为了在这些房间中留下尽可能多的烙印，在每个房间里留下烙印所花费的法力值是不相同的，已知他共有m点法力值，这些法力是不可恢复的。

小明刚接触这款游戏，所以只会耿直的玩，所以他的每一个行动都是可以预料的：

1. 一开始小明位于1号房间。

2. 如果他剩余的法力能在当前的房间中留下一个烙印，那么他就会毫不犹豫的花费法力值。

3. 无论是否留下了烙印，下一个时刻他都会进入下一个房间，如果当前位于i房间，则会进入i+1房间，如果在n号房间则会进入1号房间。

4. 当重复经过某一个房间时，可以再次留下烙印。

很显然，这个游戏是会终止的，即剩余的法力值不能在任何房间留下烙印的时候，游戏终止。请问他共能留下多少个烙印。

输入
输入第一行有两个正整数n和m，分别代表房间数量和小明拥有的法力值。(1<=n<=100000,1<=m<=10^18)

输入第二行有n个正整数，分别代表1~n号房间留下烙印的法力值花费。(1<=a_i<=10^9)

输出
输出仅包含一个整数，即最多能留下的烙印。


样例输入
4 21
2 1 4 3
样例输出
9

'''

class Solution:
    def remove_num(self,n,x,nums):
        count = 0
        num = 0
        min_val = min(nums)
        while x >= min_val:
            print(f"nums[num%n]:{nums[num%n]}")
            print(f"x:{x}")
            print(f"num%n:{num%n}")
            if nums[num%n] <= x:
                x = x - nums[num%n]
                count = count + 1
            num = num + 1
        return count
        

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1!="" and str2!="":
            n,x = str1.split(" ")
            n = int(n)
            x = int(x)
            nums = [int(num) for num in str2.split(" ")]

            res = solution.remove_num(n,x,nums)
            print(f"res:{res}")
        else:
            break

