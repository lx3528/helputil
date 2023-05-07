from typing import List

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word, index):
        node = self.root
        for w in word + "#":
            if w == "#":
                node[w] = index
                break
            if w not in node:
                node[w] = {}
            node = node[w]

    def getcnt(self, node):
        # stack
        stack = [node]
        tem_node = []
        # final_pivot=-1
        cnt_list = []
        while len(stack) > 0:
            node1 = stack.pop()
            for key in node1:
                if "#" == key:
                    val = node1['#']
                    cnt_list.append(val)
                else:
                    #print("key",key,node1)
                    #for node2 in node1[key]:
                    tem_node.append(node1[key])

            if len(stack) == 0:
                stack = tem_node
                tem_node = []

        return cnt_list

    def find_index(self, word):
        node = self.root
        finish = True
        for i in range(len(word)):
            # if '#' in node:
            if word[i] in node:
                node = node[word[i]]
            else:
                finish = False
                break
        cntlist = []
        if finish:
            cntlist = self.getcnt(node)
        return cntlist


class WordFilter:
    '''
    08:26 用字典树试试：

    '''

    def __init__(self, words: List[str]):
        self.ptree = Trie()
        self.stree = Trie()
        for ind, i in enumerate(words):
            self.ptree.insert(i, ind)
            self.stree.insert(i[::-1], ind)

    def f(self, pref: str, suff: str) -> int:
        cnt_list1 = self.ptree.find_index(pref)

        cnt_list2 = self.stree.find_index(suff[::-1])
        #print("cnt_list1,cnt_list2",cnt_list1,cnt_list2)
        cn1 = set(cnt_list1)
        cn2 = set(cnt_list2)
        val = -1
        for i in cn1 & cn2:
            if i > val:
                val = i

        return val

# Your WordFilter object will be instantiated and called as such:

words,[pref,suff]= ["apple"], ["a", "e"]
words,[pref,suff]= ["abbba","abba"],["ab","ba"]
obj = WordFilter(words)
param_1 = obj.f(pref,suff)

print("param_1",param_1)