import dfa

def __main__():
    A = dfa.DFA(
        Q={1, 2, 3, 4},
        Sigma={'a', 'b'},
        delta={
            (1, 'a'): 2,
            (1, 'b'): 4,
            (2, 'a'): 3,
            (2, 'b'): 4,
            (3, 'a'): 3,
            (3, 'b'): 3,
            (4, 'a'): 2,
            (4, 'b'): 3
        },
        q0=1,
        F={2, 4}
    )

    A0 = A.refuse()

    test_words = ["a", "b", "aa", "ab", "ba", "bb", "aba", "bab", "aaa"]
    print("Testing original A:")
    for w in test_words:
        print(f"{w}: {'True' if A.run(w) else 'False'}")

    print("\nTesting complement A0:")
    for w in test_words:
        print(f"{w}: {'True' if A0.run(w) else 'False'}")

__main__()
