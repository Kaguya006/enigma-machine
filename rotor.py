from constants import ALPHABET
from plugboard import PlugBoard


class Rotor(PlugBoard):
    def __init__(self, map_alphabet, offset=0) -> None:
        super().__init__(map_alphabet)
        self.offset = offset
        self.rotations = 0

    def rotate(self, offset=None):
        if not offset:
            offset = self.offset
        self.alphabet = self.alphabet[offset:] + self.alphabet[:offset]
        self.rotations += offset
        #print(f'offset: {offset}, rotations: {self.rotations}')
        return self.rotations

    def reset(self):
        self.rotations = 0
        self.alphabet = ALPHABET
