class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for i in range(0,len(nums)):
            num_set.add(nums[i])
        maxi = 0
        counter = 0
        for j in num_set:
            counter=0
            ele = j
            if(ele-1 in num_set):
                pass
            else:
                counter+=1
                while(True):
                    if(ele+1 in num_set):
                        counter+=1
                        ele = ele+1
                    else:
                        break
                if(counter>maxi):
                    maxi=counter
        return(maxi)
