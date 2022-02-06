from constants import ALPHABET


class EnigmaMachine(object):
    def __init__(self, plugboard, rotors, reflector) -> None:
        self.plugboard = plugboard
        self.rotors = rotors
        self.reflector = reflector

    def encrypt(self, text):
        return ''.join([self.go_through(c.upper()) for c in list(text)])

    def decrypt(self, text):
        for rotor in self.rotors:
            rotor.reset()
        return ''.join([self.go_through(c.upper()) for c in list(text)])

    def go_through(self, ch):
        if ch not in ALPHABET:
            return ch

        idx = self.plugboard.forward(ALPHABET.index(ch))
        for rotor in self.rotors:
            idx = rotor.forward(idx)

        idx = self.reflector.reflect(idx)

        for rotor in reversed(self.rotors):
            idx = rotor.backward(idx)
        idx = self.plugboard.backward(idx)
        encrypted_charactor = ALPHABET[idx]

        # １つのローターが回り切った時は、となりのローターを１つ回す
        for rotor in reversed(self.rotors):
            if rotor.rotate() % len(ALPHABET) != 0:
                break

        return encrypted_charactor
