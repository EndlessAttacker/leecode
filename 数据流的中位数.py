class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = list()


    def addNum(self, num: int) -> None:
        self.list.append(num)
        self.list.sort()


    def findMedian(self) -> float:
        n = len(self.list)
        print(n//2,self.list)
        while n>0:
            if n%2 == 0:
                return (self.list[n//2] + self.list[(n//2)-1])/2
            else:
                return self.list[n//2]


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
param_2 = obj.findMedian()
print(param_2)