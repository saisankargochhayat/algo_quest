
class trie:
    def __init__(self):
        self.root = dict()
        self.root['_end_'] = '_end_'
        self.root['_min_'] = -1
    def add_string(self,s):
        current_dict = self.root
        word = ''
        for letter in s:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                current_dict[letter] = {}
                current_dict = current_dict[letter]
            word = word+letter
        checkpoint = current_dict
        if '_end_' not in current_dict:
            current_dict['_end_'] = '_end_'
            current_dict['_min_'] = -1
            return word
        else:
            k = checkpoint['_min_'] + 1
            while not self.check_availability(str(k),checkpoint):
                k = k+1
            checkpoint['_min_'] = k
            return word + str(k)
    def check_availability(self,s,current_dict):
        for letter in s:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                current_dict[letter] = {}
                current_dict = current_dict[letter]
        if '_end_' in current_dict:
            return False
        else:
            current_dict['_end_'] = '_end_'
            current_dict['_min_'] = -1
            return True
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
t = trie()
n = int(input())
for i in range(n):
    word = input()
    print(t.add_string(word))
