import suduku_functions 

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0], 
          [6, 0, 0, 1, 9, 5, 0, 0, 0], 
          [0, 9, 8, 0, 0, 0, 0, 6, 0], 
          [8, 0, 0, 0, 6, 0, 0, 0, 3], 
          [4, 0, 0, 8, 0, 3, 0, 0, 1], 
          [7, 0, 0, 0, 2, 0, 0, 0, 6], 
          [0, 6, 0, 0, 0, 0, 2, 8, 0], 
          [0, 0, 0, 4, 1, 9, 0, 0, 5], 
          [0, 0, 0, 0, 8, 0, 0, 0, 0] 
          ] 

variables = suduku_functions.find_variables()
domain = suduku_functions.find_domains(puzzle=puzzle)
constrains = suduku_functions.find_constrains()


class CSP:
    def __init__(self, variables, domains, constrains):
        self.variables = variables
        self.domains = domains
        self.constrains = constrains
        self.solution = None

    def solve(self):
        assignment = {}
        self.solution = self.backtrack(assignment)
        return self.solution
    
    def backtrack(self, assignment):
        if len(assignment) == len(variables):
            return assignment
        
        var = self.select_unassigned_variables(assignment)
        for value in self.order_domain_values(var):
            if self.is_consistant(var, value, assignment):
                assignment[var] = value
                result = self.backtrack(assignment)

                if result is not None:
                    return result
                
                del assignment[var]
        return None

        
    def select_unassigned_variables(self, assignment):
        unassigned_vars = [var for var in self.variables if var not in assignment] 
        print("unassigned var: ", unassigned_vars)
        print("min: ", min(unassigned_vars, key=lambda var: len(self.domains[var])) )
        return min(unassigned_vars, key=lambda var: len(self.domains[var])) #returns the lowest value
    
    def order_domain_values(self,variable):
        return self.domains[variable]
    
    def is_consistant(self, variable, value, assignment):
        for constrain in self.constrains[variable]:
            if constrain in assignment and assignment[variable] == value :
                return False
        return True



csp = CSP(variables,domain, constrains)
csp.solve()