class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set('auieoAUIEO')
        words = sentence.split()
        words_latin = []

        cnt = 0
        for w in words:
            cnt += 1
            if w[0] in vowels:
                new_word = w + "ma"
            else:
                new_word = w[1:] + w[0] + "ma"

            new_word += "a" * cnt
            words_latin.append(new_word)

        return " ".join(words_latin)
