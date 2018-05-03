class trie_binary:
    def __init__(self,size):
        #size is the max size of a binary number.
        self.nodes = {}
        self.binarysize = size
        self.insert(0)
        self.swap = {'0':'1','1':'0'}
    def insert(self,n):
        arr = ('{0:0'+str(self.binarysize)+'b}').format(n)
        pointer = self.nodes
        for element in arr:
            if element not in pointer:
                pointer[element] = {}
            pointer = pointer[element]
        pointer['_end_'] = n

    def get_max_xor(self,n):
        #Given a number n, finds out the number already inserted in the trie with the
        #maximum n xor a[i]
        max = ''
        pointer = self.nodes
        arr = ('{0:0'+str(self.binarysize)+'b}').format(n)
        for element in arr:
            wewant = self.swap[element]
            if wewant in pointer:
                pointer = pointer[wewant]
                max += '1'
            else:
                pointer = pointer[element]
                max += '0'
        return pointer['_end_'],int(max,2)


trie = trie_binary(15)
