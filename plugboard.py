from constants import ALPHABET


class PlugBoard(object):

    def __init__(self, map_alphabet) -> None:
        self.alphabet = ALPHABET
        self.forward_map = {}
        self.backward_map = {}
        self.mapping(map_alphabet)

    def mapping(self, map_alphabet) -> None:
        # mapping 'ABCD' to 'BADC'
        # {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C'}
        self.forward_map = dict(zip(self.alphabet, map_alphabet))
        self.backward_map = {v: k for k, v in self.forward_map.items()}

    def forward(self, idx) -> int:
        ch = self.forward_map[self.alphabet[idx]]
        return self.alphabet.index(ch)

    def backward(self, idx) -> int:
        ch = self.backward_map[self.alphabet[idx]]
        return self.alphabet.index(ch)
