class Node:
    def __init__(self, chr = None):
        self.chr = None
        self.isLeaf = False
        self.children = {}
    
    def getChildren(self):
        return self.children.keys()
    
    def getChild(self, s: str):
        return self.children.get(s)
    
    def addChild(self, s: str):
        self.children[s] = Node(s)
        return self.children[s] # Return the node to continue. 


        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            checkChildren = curr.getChildren()
            if c not in checkChildren:
                curr = curr.addChild(c)
            else:
                curr = curr.getChild(c)
        curr.isLeaf = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            if not curr.getChild(c):
                return False
            curr = curr.getChild(c)
        if curr.isLeaf == True:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            if not curr.getChild(c):
                return False
            curr = curr.getChild(c)
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
