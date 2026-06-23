class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()
        if(len(nums)==0):
            return 0
        elif(len(nums)==1):
            return 1
        for i in range(0,len(nums)):
            hash_set.add(nums[i])
        
        starting_points = []
        for j in hash_set:
            if(j-1 in hash_set):
                continue
            else:
                starting_points.append(j)
        
        longest = 1
        for k in starting_points:
            temp = k+1
            temp_longest = 1
            while(True):
                if(temp in hash_set):
                    temp+=1
                    temp_longest +=1
                    if(temp_longest>longest):
                        longest = temp_longest
                else:
                    break
        return longest
