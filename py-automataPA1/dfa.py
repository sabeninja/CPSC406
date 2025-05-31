
class DFA :

    # init the DFA
    def __init__(self, Q, Sigma, delta, q0, F) : 
        self.Q = Q 
        self.Sigma = Sigma 
        self.delta = delta 
        self.q0 = q0 # initial state
        self.F = F # final states
   
    # print 
    def __repr__(self) :
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # run the DFA on the word w

    def run(self, w):
        current_state = self.q0
        for symbol in w:
            if symbol not in self.Sigma:
                return False
            if (current_state, symbol) not in self.delta:
                return False
            current_state = self.delta[(current_state, symbol)]
        return current_state in self.F
    
    def refuse(self):
        new_F = self.Q - self.F
        return DFA(self.Q, self.Sigma, self.delta, self.q0, new_F)
    
    def to_NFA(self):
        from nfa import NFA
        nfa_delta = {}
        for (state, symbol), dest in self.delta.items():
            nfa_delta[(state, symbol)] = {dest}
        return NFA(self.Q, self.Sigma, nfa_delta, self.q0, self.F)



        
