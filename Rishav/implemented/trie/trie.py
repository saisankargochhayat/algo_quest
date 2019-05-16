import pdb
class trie:
    def __init__(self):
        self.root = dict()
        self.root['_end_'] = '_end_'
    def add_string(self,s):
        current_dict = self.root
        for letter in s:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                current_dict[letter] = {}
                current_dict = current_dict[letter]
        current_dict['_end_'] = '_end_'
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
