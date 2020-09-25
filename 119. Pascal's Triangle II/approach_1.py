class Solution:
    def getRow(self, rowIndex: int):
        tri=[]
        row=col=0
        while row<=rowIndex:
            col=0
            while col<=row:
                #print(row,col)
                if col==0:
                    tri.append([1])
                elif col==row:
                    tri[row].append(1)
                else:
                    #print(tri)
                    tri[row].append(tri[row-1][col-1]+tri[row-1][col])
                col+=1
            row+=1
        return tri[rowIndex]

def main():
    s=Solution()
    print(s.getRow(40))

if __name__ == '__main__':
    main()
