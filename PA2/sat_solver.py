def solve_sat(clauses, assignment):
    clauses = [set(clause) for clause in clauses]

    while True:
        unit_clauses = [c for c in clauses if len(c) == 1]
        if not unit_clauses:
            break
        for clause in unit_clauses:
            lit = next(iter(clause))
            var = abs(lit)
            val = lit > 0
            if var in assignment and assignment[var] != val:
                return None
            assignment[var] = val
            new_clauses = []
            for c in clauses:
                if lit in c:
                    continue
                if -lit in c:
                    c = c.copy()
                    c.remove(-lit)
                new_clauses.append(c)
            clauses = new_clauses

    if not clauses:
        return assignment
    if any(c == set() for c in clauses):
        return None

    for clause in clauses:
        for lit in clause:
            var = abs(lit)
            if var not in assignment:
                for val in [True, False]:
                    new_assignment = assignment.copy()
                    new_assignment[var] = val
                    result = solve_sat(clauses + [{var if val else -var}], new_assignment)
                    if result is not None:
                        return result
                return None
    return assignment
