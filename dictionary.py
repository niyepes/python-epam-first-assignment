class Dictionary:
    def __init__(self):
        self._entries = {}
 
    def newentry(self, word, definition):
        self._entries[word] = definition
 
    def look(self, word):
        if word in self._entries:
            return self._entries[word]
        return f"Can't find entry for {word}"
 
 
d = Dictionary()
d.newentry('Apple', 'A fruit that grows on trees')
print(d.look('Apple'))
print(d.look('Banana'))
 
