# name: shuntaro abe
# student id: 2377370

class NFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta  # map from (state, symbol) -> set of next states
        self.q0 = q0
        self.F = F

    # for easy printing
    def __repr__(self):
        return f"NFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # run nfa on input word w
    def run(self, w):
        current_states = {self.q0}
        for symbol in w:
            next_states = set()
            for state in current_states:
                next_states |= self.delta.get((state, symbol), set())
            current_states = next_states
        return bool(current_states & self.F)  # true if any final state reached

    # powerset construction to convert nfa -> dfa
    def to_DFA(self):
        from dfa import DFA
        from collections import deque

        initial_state = frozenset({self.q0})  # start with singleton set
        dfa_states = set()
        dfa_delta = {}
        dfa_final = set()
        queue = deque([initial_state])

        while queue:
            state = queue.popleft()
            if state in dfa_states:
                continue
            dfa_states.add(state)

            for symbol in self.Sigma:
                # union over all transitions from states in current subset
                next_state = frozenset().union(*(self.delta.get((q, symbol), set()) for q in state))
                if next_state:
                    dfa_delta[(state, symbol)] = next_state
                    queue.append(next_state)

        # any subset with a final state is accepting
        for state in dfa_states:
            if self.F & state:
                dfa_final.add(state)

        return DFA(dfa_states, self.Sigma, dfa_delta, initial_state, dfa_final)
