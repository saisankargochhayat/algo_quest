class Node:
    def __init__(self,label=None,data=None):
        self.label=label
        self.data=data
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
                current_node = current_node.children[word[i]]
            else:
                word_finished=False
                break
        
        # For every new letter, create a new child node
        if not word_finished:
            while i < len(word):
                current_node.addChild(word[i])
                current_node=current_node.children[word[i]]
                i+=1
        # Let's store the full word at the end node so we don't need to
        # travel back up the tree to reconstruct the word
        current_node.data = word

    #checks if trie has that word
    def has_word(self,word):
        if word == '':
            return False
        if word == None:
            raise ValueError('Trie.has_word requires a not-Null string')
         # Start at the top
        current_node=self.head
        exists = True
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                exists = False
                break
        return exists
    

    def start_with_prefix(self,prefix):
        """ Returns a list of all words in tree that start with prefix """
        words=list()
        if prefix == None:
            raise ValueError('Requires not-Null prefix')
                
        # Determine end-of-prefix node
        top_node=self.head
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                # Prefix not in tree, go no further
                return words
        # Get words under prefix
        # Prints all words of dict
        if top_node == self.head:
            #prints value of dictionary
            queue = [node for key,node in top_node.children.items()]
        else:
            queue = [top_node]
        # This queue as a list of branches to be traversed. 
        # Perform a breadth first search under the prefix
        # A cool effect of using BFS as opposed to DFS is that BFS will return
        # a list of words ordered by increasing length
        while queue:
            current_node = queue.pop()
            if current_node.data != None:
                # Isn't it nice to not have to go back up the tree?
                words.append(current_node.data)
            queue = [node for key,node in current_node.children.items()] + queue
        return words       

    
    def getData(self, word):
        """ This returns the 'data' of the node identified by the given word """
        if not self.has_word(word):
            raise ValueError('{} not found in trie'.format(word))
        # Race to the bottom, get data
        current_node = self.head
        for letter in word:
            current_node = current_node[letter]  
        return current_node.data

if __name__ == '__main__':
    """ Example use """
    trie = Trie()
    words = 'hello goodbye help gerald gold tea ted team to too tom stan standard money'
    for word in words.split():
        trie.add(word)
    print(trie.start_with_prefix('te'))
    # print(trie.head.children['h'].children['e'].children['l'].children['l'].children.items())