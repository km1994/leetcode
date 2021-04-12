class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        '''
            方法：双指针法
            解析：
                因为对于 n * m 的二维数组中：
                    每一行都按照从左到右递增的顺序排序；
                    每一列都按照从上到下递增的顺序排序；
                所以，从左下角看：
                    上面的元素比他小；
                    左边的元素比他大；
            方法：
                从左下角开始遍历数组，做一下三种判断：
                    当前值 比 target 大，那么往上移动；
                    当前值 比 target 小，那么往右移动；
                    当前值 比 target 一样，返回 True；
                越界？返回 False
            复杂度：
                时间：O(n*m)
                空间：O(1)
        '''
        row = len(matrix)
        if row==0:
            return False
        col = len(matrix[0])
        t = row-1
        r = 0
        while t>-1 and r<col:
            if target>matrix[t][r]:
                r = r+1
            elif target<matrix[t][r]:
                t = t-1
            else:
                return True 
        return False
        