class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)-1
        ct=0
        mid = (low+high)//2
        print(high,mid)
        k = True
        cnt = 0
        while(low<=high):
            print(mid)
            
            if(int(matrix[mid][0])==int(target)):
                
                return(True)
            elif(matrix[mid][0]<target):
                if(mid+1>=len(matrix)):
                    k=False
                    break
                else:
                    if(matrix[mid+1][0]>target):
                        k=False
                        break

                low = mid+1
                
                mid = (low+high)//2
            else:
                if(mid-1<0):
                    k=False
                    break
                else:
                    if(matrix[mid-1][0]<target):
                        mid-=1
                        k=False
                        break
                high=mid-1
                mid = (low+high)//2
        l = 0
        print(mid)
        h= len(matrix[0])-1
        m = (l+h)//2
        while(l<=h):
            if(matrix[mid][m]==target):
                return(True)
            elif(matrix[mid][m]>target):
                h=m-1
                m = (l+h)//2
            else:
                l=m+1
                m = (l+h)//2
        return(False)
        