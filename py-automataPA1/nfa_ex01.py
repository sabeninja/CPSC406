from nfa import NFA

def generate_words():
    words = []
    alphabet = ['0', '1']
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                words.append(a + b + c)
    return words

def __main__():
    A1 = NFA(
        Q={'q0', 'q1'},
        Sigma={'0', '1'},
        delta={
            ('q0', '0'): {'q0'},
            ('q0', '0'): {'q1'},
            ('q1', '1'): {'q0'}
        },
        q0='q0',
        F={'q1'}
    )

    A2 = NFA(
        Q={'q0', 'q1', 'q2'},
        Sigma={'0', '1'},
        delta={
            ('q0', '0'): {'q1'},
            ('q0', '1'): {'q0'},
            ('q1', '1'): {'q2'},
            ('q2', '0'): {'q2'},
            ('q2', '1'): {'q2'}
        },
        q0='q0',
        F={'q2'}
    )

    A3 = NFA(
        Q={'q0', 'q1', 'q2'},
        Sigma={'0', '1'},
        delta={
            ('q0', '0'): {'q1'},
            ('q0', '1'): {'q0'},
            ('q1', '1'): {'q2'},
            ('q2', '0'): {'q2'},
            ('q2', '1'): {'q2'}
        },
        q0='q0',
        F={'q0', 'q1'}
    )

    A4 = NFA(
        Q={'q0', 'q1', 'q2', 'q3', 'q4'},
        Sigma={'0', '1'},
        delta={
            ('q0', '0'): {'q0'},
            ('q0', '1'): {'q0', 'q1'},
            ('q1', '0'): {'q2'},
            ('q1', '1'): {'q2'},
            ('q2', '0'): {'q3'},
            ('q2', '1'): {'q3'},
            ('q3', '0'): {'q4'},
            ('q3', '1'): {'q4'},
            ('q4', '0'): {'q4'},
            ('q4', '1'): {'q4'}
        },
        q0='q0',
        F={'q4'}
    )

    words = generate_words()
    automata = [A1, A2, A3, A4]

    for i, A in enumerate(automata, start=1):
        print(f"--- A{i} ---")
        for w in words:
            print(f"{w}: {A.run(w)}")
        print("\n")

__main__()
