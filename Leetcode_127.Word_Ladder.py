import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:        
        wordList = set(wordList)
        queue = []
        queue.append([beginWord, 1])
        
        while queue:
            word, cnt = queue.pop(0)
            
            if word == endWord:
                return cnt
            
            for i in range(len(word)):
                for c in string.ascii_lowercase[:26]:
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        queue.append([next_word, cnt + 1])
                        wordList.remove(next_word)
                        
        return 0
    
    """
        T = O(N * 26* L)
        S = O(N)
    """
        
