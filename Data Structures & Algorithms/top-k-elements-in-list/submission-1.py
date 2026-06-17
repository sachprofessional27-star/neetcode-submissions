from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p = Counter(nums)
        t=sorted(p.values())
        t=t[::-1]
        ans=set()
        last=-1
        for i in range(0,k):
            target = t[i]
            
            for key,val in p.items():
                if(val==target):  
                    prior = len(ans)               
                    ans.add(key)
                    post=len(ans)
                    if(prior==post):
                        continue
                    else:
                        break
                    
                    
                
        return(list(ans))

        