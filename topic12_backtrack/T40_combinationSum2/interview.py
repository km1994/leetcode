class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates_len = len(candidates)
        if candidates_len==0:
            return []
        candidates = sorted(candidates)
        res = []
        self.dfs(candidates,0,[],target,candidates_len,res)
        return res


    def dfs(self,candidates,begin,path,target,candidates_len,res):
        if target==0:
            res.append(path[:])
        
        for index in range(begin,candidates_len):
            # 第一轮剪枝，后面的值超过 target
            if target<candidates[index]:
                break 
            
            # 第二轮剪枝,遇到重复值
            if index>begin and candidates[index-1]==candidates[index]:
                continue
            
            self.dfs(candidates,index+1,path+[candidates[index]],target-candidates[index],candidates_len,res)


    def combinationSum21(self, candidates, target):
        # step 1：判空
        candidates_len = len(candidates)
        if candidates_len == 0:
            return []
        # step 2：排序
        candidates.sort()
        res = []
        # step 3：回溯
        self.dfs(candidates,0, [], target,candidates_len,res)
        return res

    def dfs1(self,candidates, begin, path, residue,candidates_len, res):
        '''
            方法：回溯法
            input：
                candidates          List          候选列表
                begin               int            开始位置
                path                List           当前路径
                residue             int            当前目标值
                candidates_len      int            候选列表长度            
                res                  List[]        结果列表 
            return:

        '''
        # step 1：当前目标值为零，即找到一组解
        if residue == 0:
            res.append(path[:])
            return

        for index in range(begin, candidates_len):
            # step 2：剪枝 1 当前值 超过目标值，即后面无可行解
            if candidates[index] > residue:
                break
            # step 3：剪枝 2 遇到重复值
            if index > begin and candidates[index - 1] == candidates[index]:
                continue

            path.append(candidates[index])
            self.dfs(candidates, index + 1, path, residue - candidates[index],candidates_len,res)
            path.pop()

