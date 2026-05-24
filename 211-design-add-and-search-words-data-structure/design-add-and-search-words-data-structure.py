class Node:
    def __init__(self):
        self.ch = {}
        self.end = False
        
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.ch:
                cur.ch[w] = Node()
            cur = cur.ch[w]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                if word[i] == '.':
                    for child in cur.ch.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in cur.ch:
                        return False
                    cur = cur.ch[word[i]]
            return cur.end
        return dfs(0,self.root)
                

        
        




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)