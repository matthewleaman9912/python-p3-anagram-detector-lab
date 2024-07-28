class Anagram:
    def __init__(self, word="team"):
        self.word=word
    
    def match(self, list):
        new_list = []
        for words in list:
            if sorted(words) == sorted(self.word):
                new_list.append(words)
        return new_list
