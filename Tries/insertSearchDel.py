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
        
    def startsWith(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
if __name__ == '__main__':
    words = Trie()
    keys = ["the", "quick", "fox", "brown"]
    trie = Trie()
    for key in keys:
        words.insert(key)
    print(words.search('apple'))
    print(words.search('application'))
    