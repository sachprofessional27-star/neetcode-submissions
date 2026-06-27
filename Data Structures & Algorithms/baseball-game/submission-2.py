class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        # for j in range(0,len(operations)):
        #     if(operations[j]!='C' and operations[j]!='D' and operations[j]!='+'):
        #         operations[j]=int(operations[j])
        for i in range(0,len(operations)):
            if(operations[i]=='+'):
                arr.append(arr[len(arr)-1]+arr[len(arr)-2])
            elif(operations[i]=='C'):
                arr.pop(-1)
            elif(operations[i]=='D'):
            
                arr.append(2*arr[len(arr)-1])
            else:
                arr.append(int(operations[i]))
        
        return sum(arr)