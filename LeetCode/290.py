class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_word = s.split()

        if len(pattern) != len(list_word):
            return False

        p2w = {}
        w2p = {}

        for p, w in zip(pattern, list_word):
            if p not in p2w:
                p2w[p] = w
            else:
                if p2w[p] != w:
                    return False
            
            if w not in w2p:
                w2p[w] = p
            else:
                if w2p[w] != p:
                    return False

        return True
