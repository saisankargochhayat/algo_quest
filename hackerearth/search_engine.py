class trie:
    def __init__(self):
        self.root = dict()
        self.root['_end_'] = -1
        self.root['_max_'] = -1
    def add_string(self,s,priority):
        current_dict = self.root
        for letter in s:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                current_dict[letter] = {'_max_':-1}
                current_dict = current_dict[letter]
        if '_end_' in current_dict:
            if current_dict['_end_'] < priority:
                current_dict['_end_'] = priority
        else:
            current_dict['_end_'] = priority
        if current_dict['_max_'] < priority:
            current_dict['_max_'] = priority

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

    def get_max(self,current_dict):
        curr_max = current_dict['_max_']
        for key in current_dict:
            if key == '_end_':
                if curr_max < current_dict['_end_']:
                    curr_max = current_dict['_end_']
            elif key == '_max_':
                if curr_max < current_dict['_max_']:
                    curr_max = current_dict['_max_']
            else:
                k = self.get_max(current_dict[key])
                if curr_max < k:
                    curr_max = k
        current_dict['_max_'] = curr_max
        return curr_max

    def find_max_weight(self,s):
        current_dict = self.root
        for letter in s:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return -1
        if current_dict['_max_'] == -1:
            return self.get_max(current_dict)
        else:
            return current_dict['_max_']

t = trie()
n,q = input().split(' ')
n = int(n)
q = int(q)
for i in range(n):
    word,priority = input().split(' ')
    priority = int(priority)
    t.add_string(word,priority)

for i in range(q):
    word = input()
    print(t.find_max_weight(word))
