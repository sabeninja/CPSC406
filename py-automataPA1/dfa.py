# name: Shuntaro Abe
# student id: 2377370

class DFA:

    # init dfa with states, alphabet, transition function, start state, and final states
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0  # initial state
        self.F = F    # set of accepting states

    # show it nicely when printed
    def __repr__(self):
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # simulate the dfa on input word w
    def run(self, w):
        current_state = self.q0
        for symbol in w:
            if symbol not in self.Sigma:
                return False
            if (current_state, symbol) not in self.delta:
                return False
            current_state = self.delta[(current_state, symbol)]
        return current_state in self.F

    # flips accepting and rejecting states
    def refuse(self):
        new_F = self.Q - self.F
        return DFA(self.Q, self.Sigma, self.delta, self.q0, new_F)

    # convert dfa to nfa (each dfa transition becomes a singleton nfa transition)
    def to_NFA(self):
        from nfa import NFA
        nfa_delta = {}
        for (state, symbol), dest in self.delta.items():
            nfa_delta[(state, symbol)] = {dest}
        return NFA(self.Q, self.Sigma, nfa_delta, self.q0, self.F)
