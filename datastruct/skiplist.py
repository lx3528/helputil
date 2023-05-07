from typing import Optional
import random
'''
跳表（Skip List）是对链表改造后的动态数据结构，利用空间换时间的思想，建立多级索引来提高查找、插入、删除操作的效率。

一层一层索引有点类似二分查找这种分而治之的思想。

在跳表中查询一个数据的时间复杂度是O( log n )，空间复杂度是O( n )。

跳表通过随机函数来维护平衡性，即索引大小与原始链表大小之间的平衡，不至于性能过度退化，有效平衡执行效率和内存消耗。通过随机函数，来决定将这个结点插入到哪几级索引中，比如随机函数生成了值K，那就将结点添加到第一级到第K级这K级索引中。

-------原理：
发现节点--》见find
插入节点--》

————————————————
版权声明：本文为CSDN博主「-TOXNO-」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_36911138/article/details/104233251
'''

class ListNode:
    def __init__(self, data: Optional[int] = None):
        self._data = data
        self._forwards = []


class SkipList:
    _MAX_LEVEL = 16

    def __init__(self):
        self._level_count = 1
        self._head = ListNode()
        self._head._forwards = [None] * type(self)._MAX_LEVEL

    def find(self, value: int) -> Optional[ListNode]:  # 查找
        ''''
        层_level_count越大，是最快的索引
        发现的方式`，也是从最大的索引开始查找！
        首先同层遍历，只要值小于你查找的这个值

        然后是不满足就这个节点的下一个层找
        循环上面的流程

        之后，就是这个节点了
        '''
        p = self._head
        for i in range(self._level_count - 1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
        return p._forwards[0] if p._forwards[0] and p._forwards[0]._data == value else None

    def insert(self, value: int):  # 插入
        '''
        就跟节点插入一样，只是现在有level个层，每个层都执行一次
        _forwards 其实就是next！
        :param value:
        :return:
        '''
        level = self._random_level()
        if self._level_count < level:
            self._level_count = level
        new_node = ListNode(value)
        new_node._forwards = [None] * level
        update = [self._head] * level
        p = self._head
        for i in range(level - 1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
            update[i] = p
        for i in range(level):
            new_node._forwards[i] = update[i]._forwards[i]
            update[i]._forwards[i] = new_node

    def delete(self, value: int):
        '''
        因为 p._forwards >= value
        所以对每个等于的都要删除
        :param value:
        :return:
        '''
        update = [None] * self._level_count
        p = self._head
        for i in range(self._level_count - 1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
            update[i] = p
        if p._forwards[0] and p._forwards[0]._data == value:
            for i in range(self._level_count - 1, -1, -1):
                if update[i]._forwards[i] and update[i]._forwards[i]._data == value:
                    update[i]._forwards[i] = update[i]._forwards[i]._forwards[i]


    def _random_level(self, p: float = 0.5) -> int:  # 随机函数
        level = 1
        while random.random() < p and level < type(self)._MAX_LEVEL:
            level += 1
        return level


    def __repr__(self) -> str:
        values = []
        p = self._head
        while p._forwards[0]:
            values.append(str(p._forwards[0]._data))
            p = p._forwards[0]
        p = self._head
        values1 = []
        while p._forwards[1]:
            values1.append(str(p._forwards[1]._data))
            p = p._forwards[1]
        # return "->".join(values)
        return "->".join(values) + "|"+"->".join(values1)


if __name__ == "__main__":
    l = SkipList()
    for i in range(10):
        l.insert(i)
    print(l)
    p = l.find(8)
    print(p._data)
    l.delete(4)
    print(l)