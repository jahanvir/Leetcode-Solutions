class TrieNode:
    def __init__(self):
        self.children:Dict[str, TrieNode]={}
        self.isWord=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()        

    def addWord(self, word: str) -> None:
        node: TrieNode=self.root
        for c in word:
            node=node.children.setdefault(c,TrieNode())
        node.isWord=True
        

    def search(self, word: str) -> bool:
        return self.dfs(word,0,self.root)
    
    def dfs(self,word,s,node):
        if s==len(word):
            return node.isWord
        if word[s]!='.':
            child=node.children.get(word[s],None)
            return self.dfs(word,s+1,child) if child else False
        return any(self.dfs(word, s+1,child) for child in node.children.values())


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)