import queue

q=queue.Queue(5)    #如果不设置长度,默认为无限长
print(q.maxsize)    #注意没有括号
q.put(123)
q.put(456)
q.put(789)
q.put(233)
print(q.get())
print(q.get())

#后进先出
q = queue.LifoQueue()
q.put(12)
q.put(34)
print(q.get())

#优先级队列  取优先级低的组合
q = queue.PriorityQueue()
q.put((3,'aaaaa'))
q.put((3,'bbbbb'))
q.put((1,'ccccc'))
q.put((3,'ddddd'))
print(q.get())
print(q.get())

#双线队列
q = queue.deque()
q.append(123)
q.append(456)
q.appendleft(780)
print(q)
print(q.pop())
print(q.popleft())



