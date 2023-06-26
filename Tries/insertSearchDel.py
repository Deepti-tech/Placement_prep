class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
  
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self,word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        if cur.isEnd == True:
            return True
        
    def startsWith(self):
        cur = self.root
        for c in self.word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
if __name__ == '__main__':
    words = Trie()
    words.insert('apple')
    print(words.search('apple'))
    