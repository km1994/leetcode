'''
    79. 单词搜索
    给定一个二维网格和一个单词，找出该单词是否存在于网格中。

    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

     

    示例:

    board =
    [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]

    给定 word = "ABCCED", 返回 true
    给定 word = "SEE", 返回 true
    给定 word = "ABCB", 返回 false
     

    提示：

    board 和 word 中只包含大写和小写英文字母。
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3

'''
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 回溯法
    def exist1(self, board, word):
        '''
            功能： 判断函数
            @param board List(n*m) 字符二维网络
            @param word  String    单词
            return
                res bool 是否存在
        '''
        if word == 0:
            return True
        board_row = len(board)
        board_col = len(board[0])
        board_flag = [[False for _ in range(board_col)] for _ in range(board_row)]
        res = False

        def backtrack(board,word,board_flag,board_row,board_col,i,j,res):
            '''
                功能： 回溯函数
                @param board        List(n*m)   字符二维网络
                @param word         String      单词
                @param board_flag   List(n*m)   bool 二维网络
                @param board_row    int         行数
                @param board_col    int         列数
                @param i            int         当前行
                @param j            int         当前列
                @param res          bool         是否存在
                return
                    res bool 是否存在
            '''
            if len(word) == 0:
                return True
            if res:
                return res
            res = process(board,word,board_flag,board_row,board_col,i-1,j,res) # 向左
            res = process(board,word,board_flag,board_row,board_col,i,j+1,res) # 向下
            res = process(board,word,board_flag,board_row,board_col,i+1,j,res) # 向右
            res = process(board,word,board_flag,board_row,board_col,i,j-1,res) # 向上
            return res

        def process(board,word,board_flag,board_row,board_col,i,j,res):
            '''
                功能：处理函数
                @param board        List(n*m)   字符二维网络
                @param word         String      单词
                @param board_flag   List(n*m)   bool 二维网络
                @param board_row    int         行数
                @param board_col    int         列数
                @param i            int         当前行
                @param j            int         当前列
                @param res          bool         是否存在
                return
                    res bool 是否存在
            '''
            if i>=0 and i<board_row and j>=0 and j<board_col and board[i][j]==word[0] and not board_flag[i][j]:
                board_flag[i][j] = True
                res = backtrack(board,word[1:],board_flag,board_row,board_col,i,j,res)
                board_flag[i][j] = False
            return False


        for i in range(0,board_row):
            for j in range(0,board_col):
                res = process(board,word,board_flag,board_row,board_col,i,j,res)
                if res:
                    return True
        return res

    def exist(self, board, word):
        if len(word) == 0:
            return True

        def backtrack(board,word,i,j,index):
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
                res = backtrack(board,word,i-1,j,index+1)
                if res:
                    return True

            if j-1>=0 and board[i][j-1]==word[index+1]:
                res = backtrack(board,word,i,j-1,index+1)
                if res:
                    return True

            if i<board_row-1 and board[i+1][j]==word[index+1]:
                res = backtrack(board,word,i+1,j,index+1)
                if res:
                    return True

            if j<board_col-1 and board[i][j+1]==word[index+1]:
                res = backtrack(board,word,i,j+1,index+1)
                if res:
                    return True
            
            board[i][j] = word[index]
            return False
        
        board_row = len(board)
        board_col = len(board[0])
        res = False
        for i in range(0,board_row):
            for j in range(0,board_col):
                if board[i][j]==word[0]:
                    res = backtrack(board,word,i,j,0)
                    if res:
                        return True
        return res

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        str2 = input()
        if str1 != "" and str2 != "":
            board = [[c for c in s.split(",")] for s in str1.split(";")]
            word = str(str2)
            print(f"board:{board}")
            print(f"word:{word}")

            res = solution.exist(board, word)
            print(res)
        else:
            break

