class Node:
    def __init__(self,label=None,data=None):
        self.label=label
        self.data=data
        self.num=0
        self.children={}
    
    def addChild(self,key,data=None):
        if not isinstance(key,Node):
            self.children[key] = Node(key,data)
        else:
            self.children[key.label]=key
    
    def __getitem__(self,key):
        return self.children[key]

class Trie:
    def __init__(self):
        self.head=Node()
    def __getitem__(self,key):
        return self.head.children[key]
    # add word to the graph and make a trie
    def add(self,word):
        current_node=self.head
        word_finished = True
        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node.num+=1
                current_node = current_node.children[word[i]]
            else:
                word_finished=False
                break
        
        # For every new letter, create a new child node
        if not word_finished:
            while i < len(word):
                current_node.num+=1
                current_node.addChild(word[i])
                current_node=current_node.children[word[i]]
                i+=1
        # Let's store the full word at the end node so we don't need to
        # travel back up the tree to reconstruct the word
        current_node.num += 1
        current_node.data = word

    
    def start_with_prefix(self,prefix):
        """ Returns a list of all words in tree that start with prefix """
        top_node = self.head
        if len(prefix) == 0:
            return 0
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                return 0
        return top_node.num

if __name__ == '__main__':
    """ Example use """
    trie = Trie()
    n = int(input())
    for i in range(n):
        operation,word=input().strip().split()
        if operation == "add":
            trie.add(word)
            # print(trie.head.children['s'].num)
        else:
            print(trie.start_with_prefix(word))
