from nfa import NFA

def generate_words():
    return ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']

def __main__():
    # A1 NFA
    A1 = NFA(
        Q={1, 2, 3, 4},
        Sigma={'a', 'b'},
        delta={
            (1, 'a'): {2},
            (1, 'b'): {4},
            (2, 'a'): {2},
            (2, 'b'): {3},
            (3, 'a'): {3},
            (3, 'b'): {3},
            (4, 'a'): {4},
            (4, 'b'): {4}
        },
        q0=1,
        F={3}
    )

    # A2 NFA
    A2 = NFA(
        Q={1, 2, 3},
        Sigma={'a', 'b'},
        delta={
            (1, 'a'): {2},
            (1, 'b'): {1},
            (2, 'a'): {3},
            (2, 'b'): {1},
            (3, 'a'): {3},
            (3, 'b'): {1}
        },
        q0=1,
        F={3}
    )

    # A3 NFA (non-deterministic)
    A3 = NFA(
        Q={1, 2, 3},
        Sigma={'a', 'b'},
        delta={
            (1, 'a'): {1, 2},
            (2, 'b'): {3}
        },
        q0=1,
        F={3}
    )

    # A4 NFA (no accepting states)
    A4 = NFA(
        Q={1, 2},
        Sigma={'a', 'b'},
        delta={
            (1, 'a'): {2},
            (2, 'b'): {1}
        },
        q0=1,
        F=set()
    )

    nfas = [A1, A2, A3, A4]
    words = generate_words()

    for i, nfa in enumerate(nfas, start=1):
        print(f"\n--- NFA A{i} converted to DFA ---")
        dfa = nfa.to_DFA()
        print(f"{dfa}")
        for w in words:
            print(f"{w}: {dfa.run(w)}")

__main__()
