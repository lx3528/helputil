'''

hashmap 是什么
HashMap的get/put
https://zhuanlan.zhihu.com/p/127147909

HashMap 是一个散列表，它存储的内容是键值对(key-value)映射。

增
查
删
改



我们期待一个有序的Map.这就是我们的LinkedHashMap,



# 不是双向链表：查询慢了一步：
https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247486428&idx=1&sn=3611a14535669ba3372c73e24121247c&chksm=9bd7f5d4aca07cc28c02c3411d0633fc12c94c2555c08cbfaa2ccd50cc2d25160fb23bccce7f&scene=21#wechat_redirect



'''


class hashmap:
    def __init__(self):
        self.dic={}

    def get(self,key):
        if key not in self.dic:
            return None
        return self.dic[key]


    def put(self,k,v):
        self.dic[k]=v

    #
    def remove(self,k):
        self.dic.pop(k)


class LinkedList:
    def __init__(self):
        self.list=[]
    def addfirst(self,x):
        self.add(0,x)

    def add(self,x):
        self.list.append(x)

from linklist import Node
from linklist import Linked_List
class linkedhashmap:
    '''
    先是hashmap存 kv
    然后k是通过链表链接的

    实现put：
    put放入结构中(find +remove + insert(0)
    更新索引为队列头部( dierzhong find+remove/kexuan + insert(0)
    如果队列长度大于8，删除最后一个(length-check---remove最后一个

    实现get：
    更新索引为队列头部（find +remove + insert(0)

    实现entrySet：
    按照索引顺序，输出索引（get_list)

    '''
    def __init__(self,cap):
        self.keylist = Linked_List()#存的是k
        self.map = {}# 维护kv
        self.cap = cap

    #
    def put(self,k,v):
        find_pos = self.keylist.find(k)
        if find_pos != -1:
            self.keylist.remove(find_pos)
        # else:
        self.keylist.insert(0,Node(k))

        ##--check
        if self.keylist.get_length()>=self.cap:
            del_k = self.keylist.get(self.keylist.get_length() - 1)
            #dict.pop(key)和del dict[key].
            # 值节点删除
            self.map.pop(del_k)
            self.keylist.remove(self.keylist.get_length() - 1)

        self.map[k]=v
    def get(self,k):
        find_pos = self.keylist.find(k)
        if find_pos != -1:
            self.keylist.remove(find_pos)

            self.keylist.insert(0, Node(k))

    def entrySet(self):
        print(self.keylist.get_list())


if __name__ == "__main__":
    map = linkedhashmap(6)
    map.entrySet()
    map.put("apple", "苹果");
    map.put("watermelon", "西瓜");
    map.put("banana", "香蕉");
    map.put("peach", "桃子");
    map.entrySet()
    map.get("banana");
    map.get("apple");
    map.entrySet()

    #分析上面的操作过程，要让 put 和 get 方法的时间复杂度为 O(1)，我们可以总结出 cache 这个数据结构必要的条件

    #到这里就能回答刚才「为什么必须要用双向链表」的问题了，因为我们需要删除操作。删除一个节点不光要得到该节点本身的指针，也需要操作其前驱节点的指针，而双向链表才能支持直接查找前驱，保证操作的时间复杂度 O(1)




