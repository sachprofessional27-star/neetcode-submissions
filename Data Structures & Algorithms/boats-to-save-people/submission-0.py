class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left = 0
        right = len(people)-1
        while(left<right):
            if(people[left]+people[right]<=limit):
                boats+=1
                people[left]=-1
                people[right]=-1
                left+=1
                right-=1
            else:
                right-=1
        for i in range(0,len(people)):
            if(people[i]!=-1):
                boats+=1
        return(boats)

        