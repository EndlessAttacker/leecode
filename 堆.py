import heapq 

#1 heappush生成堆+ heappop把堆从小到大pop出来 
heap = []
data = [1,3,5,7,9,2,4,6,8,0]
# ##############data
#                 1
#             3       5
#         7      9  2   4
#      6    8  0
# ###################
for i in data:
    heapq.heappush(heap,i)
print(heap,type(heap))
# ##############heap
#                 0
#             1       2
#         6      3  5   4
#      7    8  9
# ###################

lis = []
while heap:
    lis.append(heapq.heappop(heap))
    print(heap)
print(lis)

# #2 heapify生成堆+ heappop把堆从小到大pop出来 
# data2 = [1,5,3,2,9,5]
# heapq.heapify(data2)
# print(data2)

# lis2 = []
# while data2:
#     lis2.append(heapq.heappop(data2))
#     print(data2)
# print(lis2)