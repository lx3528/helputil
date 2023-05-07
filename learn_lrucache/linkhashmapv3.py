



class Node:
    """
    定义基础数据结构，链点，包含数据域和指针域
    指针域默认初始化为空
    """
    def __init__(self, k,v):
        self.k = k   # 表示对应的元素值
        self.v = v
        self.prev = None
        self.next = None



class doublelist:
    def __init__(self):
        self.size =0
        self.head=Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def addLast(self,x):
        '''
        这里是tail为添加的头部
        先把x分配好，
        然后分配tail的前一个（不用管tail，tail是单独的！）
        :param x:
        :return:
        '''
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size+=1

    def remove(self,x):
        '''

        :param x:
        :return:
        '''
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -=1

    def removeFirst(self):
        if self.head.next == self.tail:
            return None

        first = self.head.next
        self.remove(first)
        return first

    def size(self):
        return self.size


'''

https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247486428&idx=1&sn=3611a14535669ba3372c73e24121247c&chksm=9bd7f5d4aca07cc28c02c3411d0633fc12c94c2555c08cbfaa2ccd50cc2d25160fb23bccce7f&scene=21#wechat_redirect



map存k v
cache存放的是v？---你看仔细了！
'''
class LRUCache:
    def __init__(self,cap):
        self.cap = cap
        self.map={}
        self.cache = doublelist()

    #makeRecently 存在的内容，更新
    def makeRecently(self,):


    #不存在的内容，加进去，并更新
    def addRecently(self,):

    #在两个结构体中删除
    #deleteKey

    #
    #removeLeastRecently


    #
    def put(self,k,v):

