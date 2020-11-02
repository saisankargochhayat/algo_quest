MAX_CHARS = 26
letterDic = {}
letterDic['A'] = 2
letterDic['B'] = 2
letterDic['C'] = 2
letterDic['D'] = 3
letterDic['E'] = 3
letterDic['F'] = 3
letterDic['G'] = 4
letterDic['H'] = 4
letterDic['I'] = 4
letterDic['J'] = 5
letterDic['K'] = 5
letterDic['L'] = 5
letterDic['M'] = 6
letterDic['N'] = 6
letterDic['O'] = 6
letterDic['P'] = 7
letterDic['Q'] = 7
letterDic['R'] = 7
letterDic['S'] = 7
letterDic['T'] = 8
letterDic['U'] = 8
letterDic['V'] = 8
letterDic['W'] = 9
letterDic['X'] = 9
letterDic['Y'] = 9
letterDic['Z'] = 9


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.child = [None] * 10


class Trie:
    def __init__(self, words):
        self.words = words
        self.root = TrieNode()
        self.words_to_trie()

    def words_to_trie(self):
        for word in self.words:
            conv_word = [letterDic[x] for x in word[::-1]]
            self.create_entry(conv_word)

    def create_entry(self, conv_word):
        node = self.root
        for num in conv_word:
            if not node.child[num]:
                node.child[num] = TrieNode()
            node = node.child[num]
        node.is_word = True


def vanity(codes, numbers):
    # Write your code here
    def has_word(number: str):
        nonlocal global_trie
        node = global_trie.root
        for num_char in number[::-1]:
            if node.is_word == True:
                return True
            if not node.child[int(num_char)]:
                return False
            node = node.child[int(num_char)]
        else:
            return False

    out_list = []
    global_trie = Trie(codes)
    for number in numbers:
        if has_word(number):
            out_list.append(number)
    print(out_list)
    return []


words_in = ['TWLO']
numbers_in = [
    '+14157088956',
    '+15109926333',
    '+17474824380',
    '+1415123456',
    '+919810155555'
]
vanity(words_in, numbers_in)