class trie:
    def __init__(self):
        self.root = dict()
        self.root['_end_'] = '_end_'
    def add_string(self,s,priority):
        current_dict = self.root
        for letter in s:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                current_dict[letter] = {}
                current_dict['_max_weight_'] = -1
                current_dict = current_dict[letter]
        current_dict['_end_'] = priority
        current_dict['_max_weight_'] = -1
    def find_string(self,s):
        current_dict = self.root
        for letter in s:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return False
        if '_end_' in current_dict:
            return True
        else:
            return False
    def find_weight(self,current_dict,max_weight):
        if current_dict['_max_weight_'] > -1:
            return current_dict['_max_weight_']
        else:
            for key in current_dict:
                if key == '_end_':
                    if max_weight < current_dict['_end_']:
                        max_weight = current_dict['_end_']
                elif key!='_max_weight_':
                    max_weight = self.find_weight(current_dict[key],max_weight)
        current_dict['_max_weight_'] = max_weight
        return max_weight

    def find_complete_strings(self,s):
        current_dict = self.root
        for letter in s:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return -1
        return self.find_weight(current_dict,-1)

t = trie()
n,q = input().split()
n = int(n)
q = int(q)
for i in range(n):
    word,weight = input().split()
    weight = int(weight)
    t.add_string(word,weight)


for i in range(q):
    word = input()
    print(t.find_complete_strings(word))
