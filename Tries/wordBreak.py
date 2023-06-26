class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
  
class Trie:
    def __init__(self):
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
        if cur.isEnd:
            return True
        return False
            
def checkWordBreak(trie, word):
    if len(word) == 0:  # Base case: empty string
        return True

    n = len(word)
    for i in range(1, n + 1):
        if trie.search(word[:i]) and checkWordBreak(trie, word[i:]):
            return True
    return False
    
if __name__ == '__main__':
    wrd = "thequickbrownfox",
    keys = ["the", "quick", "fox", "brown"]
    trie = Trie()
    for key in keys:
        trie.insert(key)
        
    print(checkWordBreak(trie, wrd))
    