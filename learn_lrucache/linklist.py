
'''
插入一个，再删一个！


Java LinkedList（链表） 类似于 ArrayList，是一种常用的数据容器。

与 ArrayList 相比，LinkedList 的增加和删除对操作效率更高，而查找和修改的操作效率较低

以下情况使用 ArrayList :

频繁访问列表中的某一个元素。
只需要在列表末尾进行添加和删除元素操作。
以下情况使用 LinkedList :

你需要通过循环迭代来访问列表中的某些元素。
需要频繁的在列表开头、中间、末尾等位置进行添加和删除元素操作

https://blog.csdn.net/weixin_43314519/article/details/107473351
'''
class Node:
    """
    定义基础数据结构，链点，包含数据域和指针域
    指针域默认初始化为空
    """
    def __init__(self, data):
        self._data = data   # 表示对应的元素值
        self._next = None   # 表示下一个链接的链点​

class Linked_List:
    """
    创建一个Linked_List类，初始化对应的内参
    """
    def __init__(self, head=None):  # 链表初始化函数
        self._head = head   # 初始化的链表有一个头结点，为None# self._head 是Node() 类型​
    def append(self, new_element):
        """
        append函数
        功能是向链表添加新的结点
        这个新结点应该是 Node 数据类型（上面定义的链点类）
        """
        # 将头部结点指向临时变量，current
        current = self._head
        # 当头部结点存在的时候
        if self._head:
            # 循环遍历到列表的最后一个元素
            while current._next:
                current = current._next
            current._next = new_element
        # 当头部结点不存在时，即为空的时候，即由一个空链表向后面append链点
        else:
            self._head = new_element

    def is_empty(self):
        """
        判断链表是否为空
        """
        # bool 函数只返回True和False
        return not self._head
    def get_length(self):
        """
        获取链表的长度
        """
        # 将头部结点赋值给temp变量
        temp = self._head
        # 计算链表长度
        length = 0
        while temp != None:
            length = length + 1
            temp = temp._next
        # 返回链表的长度
        return length

    def insert(self, position, new_element):
        """
        在链表指定索引出添加一个new_element元素
        流程如下：
            1.先判断要插入的位置是否在链表的索引范围内
            2.当插入的位置是头结点时，（即索引为0）时，做特殊情况处理
            3.当插入的结点位置不是在0时，找到要插入的位置，插入新结点
        """
        global pre
        if position < 0 or position > self.get_length():
            raise IndexError("insert插入时，key的值超出了范围")
        temp = self._head
        # 如果在头结点插入
        if position == 0:
            new_element._next = temp
            self._head = new_element
            return
        # 如果不是i=0 或者 超出范围，则需要遍历到指定位置
        i = 0
        while i < position:
            pre = temp
            temp = temp._next
            i += 1
            # 等待循环结束时，已经找到i这个元素，即为temp.并且temp的前一个元素pre也已找到
        pre._next = new_element
        new_element._next = temp

    # 找对应元素值的索引！
    # silu：1\ 遍历找data值的索引是那个，如果不存在返回-1
    def find(self,data):
        temp = self._head  # 将头结点保存在temp中去
        pos = 0
        # 当存在链表元素才能执行删除操作
        while temp != None:
            if temp._data == data:
                return pos
            temp = temp._next
            pos+=1
        return -1
    def get(self,newpos):
        temp = self._head
        pos = 0
        while temp != None:
            if pos == newpos:
                return temp._data
            temp = temp._next
            pos+=1
        return None

    def remove(self, position):
        """
        从链表中任意位置删除一个元素
        流程如下：
            1.先判断要删除的元素索引是否存在，如果不存在抛出错误
            2.接着判断当存在链表元素时才能执行删除操作。
            3.当要删除的是头结点时（即索引为 0），做特殊情况处理。
            4.他情况时，通过循环找到要删除的结点。
            5.最后把这个结点删除掉。
        """
        #所以多加了个等于号！
        if position < 0 or position >= self.get_length():
            raise IndexError("删除元素的索引超出范围")
        i = 0   # 遍历链表时使用
        temp = self._head   # 将头结点保存在temp中去
        # 当存在链表元素才能执行删除操作
        while temp != None:
            # 若要删除头结点
            if position == 0:
                # 将头结点的后一个结点（即temp._next）
                # 赋值给新的头结点，再将之前的头结点指向None
                self._head = temp._next
                temp._next = None
                return
            # 若要删掉的不是头结点，也不超出范围
            # 需要遍历链表找到位置
            pre = temp
            temp = temp._next
            i += 1
            # i 为1的时候，删除的就是第一个索引的节点
            #i 为2 时候， 会报错，因为temp为空，测试一下！
            if i == position:
                # 将pre的next属性指向temp的下一个结点
                pre._next = temp._next
                temp._next = None
                return
    def get_list(self):
        temp = self._head
        new_list = []
        while temp is not None:
            new_list.append(temp._data)
            temp = temp._next
        return new_list
    def print_list(self):
        """
        遍历链表，将元素依次打印出来
        """
        print("Linked_list:")
        new_list = self.get_list()
        print(new_list)
    def reverse(self):
        """
        将链表反转
        """
        prev = None
        current = self._head
        while current:
            # 将本来由链点1指向链点2的连接， 反转为由链点2指向链点1
            next_node = current._next   # 将下一个链点保存在next_node中
            current._next = prev    # 将头结点变为尾结点，所以尾结点指向 None
            prev = current  # 更新prev：当前的这个链点变为下一个链点的前一个链点
            current = next_node     # 向后移动链点
        self._head = prev   # 最终将原本的链尾结点指定为链表的头结点
    def initlist(self, data_list):
        """
        将列表转化为链表
        """
        # 创建头结点
        self._head = Node(data_list[0])
        temp = self._head
        # 逐个为data内的数据创建结点，建立链表
        for i in data_list[1:]:
            node = Node(i)
            temp._next = node
            temp = temp._next


if __name__ == "__main__":
    list = Linked_List()
    list.append(Node(1))
    list.append(Node(2))
    list.append(Node(3))
    list.append(Node(5))
    list.print_list()
    print(list.get(list.find(2)))
    print(list.find(6))
    print(list.get_length())
    print(list.remove(3))
    list.print_list()
    list.reverse()
    list.print_list()
