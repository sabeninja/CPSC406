class NFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta  # {(state, symbol): {next_states}}
        self.q0 = q0
        self.F = F

    def __repr__(self):
        return f"NFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    def run(self, w):
        current_states = {self.q0}
        for symbol in w:
            next_states = set()
            for state in current_states:
                next_states |= self.delta.get((state, symbol), set())
            current_states = next_states
        return bool(current_states & self.F)

    def to_DFA(self):
        from dfa import DFA
        from collections import deque

        initial_state = frozenset({self.q0})
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
                next_state = frozenset().union(*(self.delta.get((q, symbol), set()) for q in state))
                if next_state:
                    dfa_delta[(state, symbol)] = next_state
                    queue.append(next_state)

        for state in dfa_states:
            if self.F & state:
                dfa_final.add(state)

        return DFA(dfa_states, self.Sigma, dfa_delta, initial_state, dfa_final)
