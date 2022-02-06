from constants import ALPHABET


class Reflector(object):
    def __init__(self, map_alphabet) -> None:
        self.map = dict(zip(ALPHABET, map_alphabet))
        for x, y in self.map.items():
            if x != self.map[y]:
                raise ValueError(x, y)

    def reflect(self, idx):
        reflected_ch = self.map[ALPHABET[idx]]
        return ALPHABET.index(reflected_ch)
