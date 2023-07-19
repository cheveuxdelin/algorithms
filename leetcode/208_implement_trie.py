class TrieNode:
    def __init__(self, value: str = "") -> None:
        self.value = value
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        current = self.head
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode(c)
            current = current.children[c]
        current.is_word = True

    def search(self, word: str) -> bool:
        current = self.head
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        current = self.head
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True


        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
