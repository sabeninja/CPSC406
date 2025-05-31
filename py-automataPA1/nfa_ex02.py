from dfa import DFA
from nfa import NFA

def generate_words():
    words = []
    alphabet = ['a', 'b']
    for first in alphabet:
        for second in alphabet:
            for third in alphabet:
                words.append(first + second + third)
    return words

def __main__():
    A1 = DFA(
        Q={1, 2, 3, 4},
        Sigma={'a', 'b'},
        delta={
            (1, 'a'): 2,
            (1, 'b'): 4,
            (2, 'a'): 2,
            (2, 'b'): 3,
            (3, 'a'): 3,
            (3, 'b'): 3,
            (4, 'a'): 4,
            (4, 'b'): 4
        },
        q0=1,
        F={3}
    )

    A2 = DFA(
        Q={1, 2, 3},
        Sigma={'a', 'b'},
        delta={
            (1, 'a'): 2,
            (1, 'b'): 1,
            (2, 'a'): 3,
            (2, 'b'): 1,
            (3, 'a'): 3,
            (3, 'b'): 1
        },
        q0=1,
        F={3}
    )

    dfas = [A1, A2]
    words = generate_words()

    for i, dfa in enumerate(dfas, start=1):
        print(f"\n--- DFA A{i} converted to NFA ---")
        nfa = dfa.to_NFA()
        for w in words:
            print(f"{w}: {nfa.run(w)}")

__main__()
