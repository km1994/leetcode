'''
    212. 单词搜索 II
    给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

    示例:

    输入: 
    words = ["oath","pea","eat","rain"] and board =
    [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
    ]

    输出: ["eat","oath"]

'''
import copy
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 回溯法
    def findWords(self, board, words):
        res =[]
        for word in words:
            temp_board = copy.deepcopy(board)
            if self.exist(temp_board, word):
                res.append(word)
        return res

    # 回溯法 
    def exist(self, board, word):
        if len(word) == 0:
            return True

        board_row = len(board)
        board_col = len(board[0])
        res = False
        for i in range(0,board_row):
            for j in range(0,board_col):
                if board[i][j]==word[0]:
                    res = self.dfs(board,word,i,j,0)
                    if res:
                        return True
        return res

    def dfs(self,board,word,i,j,index):
        '''
            功能： 回溯函数
            @param board        List(n*m)   字符二维网络
            @param word         String      单词
            @param board_row    int         行数
            @param board_col    int         列数
            @param i            int         当前行
            @param j            int         当前列
            return
                res bool 是否存在
        '''
        res = False
        board_row = len(board)
        board_col = len(board[0])
        if len(word) == index+1:
            return True
        board[i][j] = '\n'
        if i-1>=0 and board[i-1][j]==word[index+1]:
            res = self.dfs(board,word,i-1,j,index+1)
            if res:
                return True

        if j-1>=0 and board[i][j-1]==word[index+1]:
            res = self.dfs(board,word,i,j-1,index+1)
            if res:
                return True

        if i<board_row-1 and board[i+1][j]==word[index+1]:
            res = self.dfs(board,word,i+1,j,index+1)
            if res:
                return True

        if j<board_col-1 and board[i][j+1]==word[index+1]:
            res = self.dfs(board,word,i,j+1,index+1)
            if res:
                return True
        
        board[i][j] = word[index]
        return False


if __name__ == "__main__":
    
    solution = Solution()
    input_type = 0
    if input_type:
        while 1:
            str1 = input()
            str2 = input()
            if str1 != "" and str2 != "":
                board = [[c for c in s.split(",")] for s in str1.split(";")]
                words = str2.split(",")
                print(f"board:{board}")
                print(f"words:{words}")

                res = solution.findWords(board, words)
                print(res)
            else:
                break
    else:
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        res = solution.findWords(board, words)
        print(res)



