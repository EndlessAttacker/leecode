from typing import List
class Solution:
    def frontSums(self, list:List[int]):
        list1 = []
        sum = 0
        list1.append(sum)
        if list == []:
            return []
        for i in list:      
            sum += i
            list1.append(sum)
        # print(list1)
        return list1

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len( grid )
        n = len( grid[ 0 ] )
        # print("ceshi",self.frontSums( grid[2] )[3],self.frontSums( grid[2] )[0])
        rows = []
        for i in range(n):

            rows.append([rows[i] for rows in grid])  
        print(rows)
        for d in range( min( m, n) , -1, -1):
            for i in range(0,m - d + 1):
                for j in range(0,n - d + 1):

                    if self.frontSums( grid[i] )[j+d]- self.frontSums( grid[i] )[j] == d and\
                       self.frontSums( grid[i + d - 1] )[j+d]- self.frontSums( grid[i + d - 1] )[j] == d and\
                        self.frontSums( rows[j + d - 1] )[i+d]- self.frontSums( rows[j + d - 1] )[i] == d and\
                        self.frontSums( rows[j] )[i+d]- self.frontSums( rows[j] )[i] == d:
                        return d*d
    
        # while n > 0:
        #     for i in range(n):
        #         for j in range(i):

grid = [[0,0,0],[0,0,0]]
s = Solution()
# print(s.frontSums(grid[0]))
print(s.largest1BorderedSquare(grid))