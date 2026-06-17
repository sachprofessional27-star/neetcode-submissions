class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(0,len(position)):
            arr.append([position[i],speed[i]])
        
        arr = sorted(arr,key = lambda x:x[0])
        x = []
        y = []
        for i in range(0,len(arr)):
            x.append(arr[i][0])
            y.append(arr[i][1])
        x=x[::-1]

        y=y[::-1]
        fleet = 1
        last = x[0]
        s1 = y[0]
        stk = []
        for i in range(1,len(x)):
            if(y[i]>s1):
                rem1 = target-last
                tr1 = rem1/s1
                cover = last-x[i]
                timecover = cover/(y[i]-s1)
                #print(x[i],y[i],tr1,timecover)
                if(timecover<=tr1):
                    pass
                else:
                    fleet+=1
                    last = x[i]
                    s1 = y[i]
            else:
                fleet+=1
                last = x[i]
                s1 = y[i]
        return(fleet)


