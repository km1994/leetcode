class Solution:
    def subSort1(self, array: List[int]) -> List[int]:
        '''
            方法：左右指针 【两遍遍历】
        '''
        # step 1：判空
        array_len = len(array)
        if array_len==0:
            return [-1,-1]
        # step 2：定义值和指针
        max_val = -9999
        min_val = 9999
        first_pos = -1
        last_pos = -1
        # step 3: 从前向后扫描数组，判断当前array[i]是否比max小，是则将last置为当前array下标i，否则更新max;
        for i in range(array_len):
            if max_val<=array[i]:
                max_val = max(array[i],max_val)
            else:
                last_pos = i 
        # step 4: 从后向前扫描数组，判断当前array[len - 1 - i]是否比min大，是则将first置位当前下标len - 1 - i，否则更新min;
        for i in range(array_len-1,-1,-1):
            if min_val>=array[i]:
                min_val = min( array[i],min_val)
            else:
                first_pos = i 
        return [first_pos,last_pos]

    
    def subSort(self, array: List[int]) -> List[int]:
        '''
            方法：左右指针 【一遍遍历】
        '''
        # step 1：判空
        array_len = len(array)
        if array_len==0:
            return [-1,-1]
        # step 2：定义值和指针
        max_val = -9999
        min_val = 9999
        first_pos = -1
        last_pos = -1
        for i in range(array_len):
            if max_val<=array[i]:
                max_val = max(array[i],max_val)
            else:
                last_pos = i 
            if min_val>=array[array_len-i-1]:
                min_val = min( array[array_len-i-1],min_val)
            else:
                first_pos = array_len-i-1 
        return [first_pos,last_pos]

            


