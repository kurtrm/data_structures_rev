"""Implement a trie in Python."""


class Trie:
    """Define a trie and its methods."""

    def __init__(self):
        """Initialize a trie."""
        self._base = {}
        self._size = 0

    def insert(self, word: str) -> None:
        """Insert an input string into the trie."""
        if not isinstance(word, str):
            raise TypeError('Insert takes in one param which must be a string')

        if word not in self:
            current = self._base
            for idx, character in enumerate(word, start=1):
                try:
                    current = current[character]
                    if idx == len(word):
                        current['$'] = {}
                except KeyError:
                    current[character] = {}
                    if idx == len(word):
                        current[character]['$'] = {}
                    else:
                        current = current[character]
            self._size += 1

    def contains(self, word: str) -> bool:
        """Check to see if a given word is contained in the trie."""
        if not isinstance(word, str):
            raise TypeError('word argument must be str')

        current = self._base
        for character in word + '$':
            try:
                current = current[character]
            except KeyError:
                return False
        else:
            return True

    @property
    def size(self):
        """Return the total number of words in the trie."""
        return self._size

    def remove(self, word: str) -> None:
        """Remove the specified word from the trie."""
        if not isinstance(word, str):
            raise TypeError('Parameter must be of type str')
        if word not in self:
            raise ValueError('Word not in trie')

        current = self._base
        last_word = self._base
        next_letter = word[0]
        for idx, letter in enumerate(word, start=1):
            if '$' in current[letter] and idx != len(word):
                last_word = current[letter]
                next_letter = word[idx]
                current = current[letter]
            elif idx == len(word):
                if len(current[letter]) > 1:
                    del current[letter]['$']
                else:
                    del last_word[next_letter]
                self._size -= 1
            else:
                current = current[letter]

    def traversal(self, start: str, end: str=None) -> None:
        """Perform a DFT of the trie from a specified start."""
        if not isinstance(start, str):
            raise TypeError('Traversal takes in one param which must be a string')
        if not start:
            raise ValueError('Please enter a string')
        if end is None:
            curr = self._base
            for idx, char in enumerate(start, start=1):
                if idx == len(start) and char in curr:
                    yield start
                    curr = curr[char]
                    for char in curr:
                        if not char == '$':
                            yield char
                            for each_char in self.traversal(start, curr[char]):
                                yield each_char
                elif char in curr:
                    curr = curr[char]
                else:
                    raise ValueError('String not in trie')
        else:
            for char in end:
                if not char == '$':
                    yield char
                    for each_char in self.traversal(start, end[char]):
                        yield each_char

    def autocomplete(self, start: str, end: str=None) -> str:
        """Autocomplete a string with all possible words."""
        if not isinstance(start, str):
            raise TypeError('Traversal takes in one param which must be a string')

        words = []
        if not end:
            curr = self._base
            for idx, char in enumerate(start, start=1):
                if idx == len(start) and char in curr:
                    curr = curr[char]
                    for char in curr:
                        if char == '$':
                            words.append(start)
                        if not char == '$':
                            next_char = start + char
                            words.extend(self.autocomplete(next_char, curr[char]))
                elif char in curr:
                    curr = curr[char]
                else:
                    raise ValueError('String not in trie')
        else:
            for char in end:
                if char == '$':
                    words.append(start)
                if not char == '$':
                    next_char = start + char
                    words.extend(self.autocomplete(next_char, end[char]))

        return words

    def __contains__(self, item):
        """
        Permit the use of the 'in' keyword to check
        membership of a word in the trie.
        """
        return self.contains(item)
