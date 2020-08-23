


class Trie:

    def __init__(self):
        self.root = {}
        self.root['#'] = False


    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.setdefault(w,{})
        node['#'] = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node:
                return False
            node = node[w]
        return node['#'] == True if '#' in node else False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node:
                return False
            node = node[w]
        return True