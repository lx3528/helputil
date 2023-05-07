#
# #skiptable
#
# '''
# 主旨：可运行，易看懂的代码
#
#
# 类似分块查找，二级索引
# 跳表
#
# 快速查找、插入、删除的数据结构
#
# 空间复杂度： n
# 查找时间复杂度：o（logn）
# 插入删除：o（logn)
#
# 十分钟弄懂什么是跳表，不懂可以来打我_愤怒的可乐的博客-CSDN博客_跳表%20(2022_4_29%2012_39_31).html
#
# 分块查找又称索引顺序查找，它是顺序查找的一种改进方法
#
# '''
# import random
# maxLevel = 4
# PROBABILITY = 0.5
#
# class Node:
#     def __init__(self,data):
#         self.data=data;
#         self.forwards=[]#保存每层节点上的索引信息
#         for i in range(maxLevel):
#             self.forwards.append(None)
#
#     def isnull(self):
#         if self.data == None:
#             return " "
#
#         return ""  + self.data
#
#     def next(self,level):
#         if level>=maxLevel:
#             print("maxLevel",level)
#             return None
#         return self.forwards[level]
#
#
#
#
# class SkipList:
#     def __init__(self):
#         self.size = 0
#         self.curLevel = 0
#         self.head = Node(None)
#
#     '''
#     生成随机层数[0,maxLevel)
#          * 生成的值越大，概率越小
#     '''
#     def randomLevel(self):
#         level = 0
#         for i in range(maxLevel-1):
#         # while random.randint(0,101)/100 < PROBABILITY \
#         #     and level < maxLevel - 1:
#             if random.randint(0,101)/100 < PROBABILITY:
#                 level+=1
#         return level
#
#     #返回给定层数中小于e的最大者
#     def findNext(self,e,cur,level):
#         next_node = cur.next(level)
#         while next_node != None:
#             if e < next_node.data:
#                 break
#             cur = next_node
#             next_node = cur.next(level)
#         return cur
#     # def find(self,e):
#     #     if self.size == 0:
#     #         return None
#     #     return self.find(e,self.head,self.curLevel)
#     def find(self,e,cur= 0,level = 0):
#         if self.size == 0:
#             return None
#         if cur == 0:
#             cur = self.head
#             level = self.curLevel
#         while level >= 0:
#             cur = self.findNext(e,cur,level)
#             level-=1
#         return cur
#     def contains(self,e):
#         node = self.find(e)
#         if node is not None and node.data is not None and node.data == e:
#             return True
#         return False
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.head.next(0) is not None:
#             return self.head.data
#         else:
#             raise StopIteration
#
#     def print(self):
#         index_map = {}
#         cur = self.head.next(0)
#         index =1
#         maxwidth=1
#         while cur is not None:
#             curwidth = len(str(cur.data))
#             if curwidth > maxwidth:
#                 maxwidth = curwidth
#             index+=1
#             index_map[cur.data]= index
#             cur= cur.next(0)
#
#         self.print2(index_map,maxwidth)
#     def print2(self,index_map,width):
#         level = self.curLevel
#
#         while level>=0:
#             print("level: %s hd_nt:%s index_map:%s width:%s"%(level,str(self.head.next(level)),index_map,width))
#             level-=1
#
#
#
#     def add(self,e):
#         if self.contains(e):
#             return False
#
#         level = self.randomLevel()
#
#         if (level > self.curLevel):
#             self.curLevel = level
#         newnode = Node(e)
#         cur = self.head
#         print("level",level)
#         while level>=0:
#             cur = self.findNext(e,cur,level)
#
#             newnode.forwards.insert(0,cur.next(level))
#             #newnode.forwards[level] = cur.next(level)
#
#             cur.forwards[level] = newnode
#
#             level-=1
#         self.size+=1
#         return True
#
#
# # 写一点看一点！
#
# if __name__=="__main__":
#     val = [1,6,9,3,5,7,4,8]
#     sk = SkipList()
#     for i in val:
#         #temp_node = Node(i)
#         sk.add(i)
#
#     print("before remove")
#     sk.print()