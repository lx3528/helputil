'''
算法学习笔记(1) : 并查集
https://zhuanlan.zhihu.com/p/93647900

用于解决：神跟谁是亲戚（是否是同一个集合）

结果：每个人都有一个父亲，然后相互寻找

问题：如何合并
前者的父节点设为后者

路径压缩：
'''
class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1] *n
        self.n=n
        self.setCount = n

    def findset(self,x):
        if self.parent[x]==x:
            return x
        self.parent[x]=self.findset(self.parent[x])
        return self.parent[x]
    def unite(self,x,y):
        '''
        hebing
        :param x:
        :param y:
        :return:
        '''
        x,y=self.findset(x),self.findset(y)
        if x==y:
            return False
        if self.size[x]<self.size[y]:
            x,y=y,x
        self.parent[y]=x
        self.size[x]+=self.size[y]

        self.setCount-=1
        return True
    def connected(self,x,y):
        x,y=self.findset(x),self.findset(y)
        return x==y

    def isolate(self,x):
        if self.parent[x]!=x:
            self.parent[x]=x
            self.size[x]=1
            self.setCount+=1
import math
def factors(a):
    '''
    计算a的所有因子
    :param a:
    :return:
    '''
    ans=set()
    # 埃氏找因子！
    for i in range(1,int(math.sqrt(a))+1):
        if not a%i:
            ans.add(i)
            ans.add(a//i)
    return ans
from collections import defaultdict
class Solution:
    def largestComponentSize(self,nums):
        n=len(nums)
        factor = defaultdict
        for i,a in enumerate(nums):
            fac=factors(a)
            for f in fac:
                if f!=1:
                    factor[f].append(i)
        UF = UnionFind(n)#先创建这么多个数的
        for f in factor:
            for i in range(1,len(factor[f])):
                UF.unite(factor[f][i-1],factor[f][i])
        return max(UF.size)



