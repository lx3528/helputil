'''

不要想为什么做，就去做，
想怎么做！！！！


因为标准答案给的是存val：
private HashMap<Integer, Node> map;
    // Node(k1, v1) <-> Node(k2, v2)...
    private DoubleList cache;

我需要改造一下！让他存key，但还要封装函数
'''


'''
doublelist 有哪些任务呢？
--通过链表的形式进行添加
1、定义一个head和tail
2、在尾部添加节点x，addlast（o1）
3、删除节点x，remove(x)
4、removeFirst 删除第一个节点
5、size 返回大小

'''
class Node:
    """
    定义基础数据结构，链点，包含数据域和指针域
    指针域默认初始化为空
    """
    def __init__(self, data):
        self.data = data   # 表示对应的元素值
        self.left = None
        self.right = None

class doublelist:
    def __init__(self,cap):
        self.head = Node(0)
        self.tail = self.head
        self.cap = cap

    #head 是last
    def addlast(self,t):

        x=Node(t)
        #x.right = self.head.right
        #right 是空的，所以没用
        if self.head.right:
            self.head.right.left = x
            self.head.right = x
        self.head.right = x
        x.left = self.head

        # 重置
        self.head = x

    def remove(self,t):
        #x=Node(t)
        tem = self.tail
        while tem.right:
            if tem.right.data == t:
                #删除
                tem.right.right.left = tem
                tem.right = tem.right.right
                break
            tem = tem.right

    def removeTail(self):
        if self.head != self.tail:
            self.head = self.head.left
            self.head.right = None
    def removeFirst(self):
        if self.head != self.tail:
            del_node = self.tail.right
            if self.tail.right.right:
                self.tail.right.right.left = self.tail
            self.tail.right = self.tail.right.right
            if del_node == self.head:
                self.head = self.tail

    def print(self):
        sstr=""
        tem = self.tail.right
        while tem != None and tem != self.tail:
            sstr += str(tem.data) + " "
            tem = tem.right
        print("sstr:"+sstr)


if __name__ == "__main__":
    m1 = doublelist(11)


    # 添加
    print(m1.addlast(1))
    m1.addlast(2)

    m1.addlast(3)

    m1.addlast(4)

    m1.addlast(5)

    m1.addlast(6)
    m1.print()

    # 删除
    m1.remove(5)
    m1.print()
    m1.removeFirst()
    m1.print()#sstr:2 3 4 6

    m1.removeFirst()
    m1.print()#sstr:3 4 6

    m1.removeFirst()
    m1.print()#sstr:4 6

    m1.removeFirst()
    m1.print()#sstr:6

    m1.removeFirst()
    m1.print()
    # map = linkedhashmap(6)
    # map.entrySet()
    # map.put("apple", "苹果");
    # map.put("watermelon", "西瓜");
    # map.put("banana", "香蕉");
    # map.put("peach", "桃子");
    # map.entrySet()
    # map.get("banana");
    # map.get("apple");
    # map.entrySet()

    #分析上面的操作过程，要让 put 和 get 方法的时间复杂度为 O(1)，我们可以总结出 cache 这个数据结构必要的条件

    #到这里就能回答刚才「为什么必须要用双向链表」的问题了，因为我们需要删除操作。删除一个节点不光要得到该节点本身的指针，也需要操作其前驱节点的指针，而双向链表才能支持直接查找前驱，保证操作的时间复杂度 O(1)




