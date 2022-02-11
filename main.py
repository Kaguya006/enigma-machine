import random
from constants import ALPHABET
from enigma import EnigmaMachine
from plugboard import PlugBoard
from rotor import Rotor
from reflector import Reflector

if __name__ == '__main__':
    def get_random_alphabet(): return ''.join(
        random.sample(ALPHABET, len(ALPHABET))
    )
    p = PlugBoard(get_random_alphabet())
    r1 = Rotor(get_random_alphabet(), 2)
    r2 = Rotor(get_random_alphabet(), 3)
    r3 = Rotor(get_random_alphabet(), 5)

    reflect_mapping = list(ALPHABET)
    indexes = [i for i in range(len(ALPHABET))]
    for _ in range(int(len(indexes) / 2)):
        x = indexes.pop(random.randint(0, len(indexes) - 1))
        y = indexes.pop(random.randint(0, len(indexes) - 1))
        reflect_mapping[x], reflect_mapping[y] = reflect_mapping[y], reflect_mapping[x]
    r = Reflector(''.join(reflect_mapping))

    enigma_machine = EnigmaMachine(
        p, [r1, r2, r3], r
    )

    print('INPUT TEXT >>', end='')
    s1 = input().strip()
    encrypted = enigma_machine.encrypt(s1)
    print('-----ENCRYPTED-----')
    print(encrypted)
    print('-----ENCRYPTED-----\n')

    print('INPUT THE ENCRYPTED TEXT >>', end='')
    s2 = input().strip()

    print('\n-----DECRYPTED-----')
    print(enigma_machine.decrypt(s2))
    print('-----DECRYPTED-----')
