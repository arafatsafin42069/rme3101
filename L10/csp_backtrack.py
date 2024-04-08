import sys
import time

#variables is where we will put values (State1, State2, State3, etc.)
#domains is where we will put the possible values (Red, Blue, Green, etc.)
#constrains is where we will put the rules (State1 != State2, State2 != State3, etc.)
class CSP:
    def __inti__(self, variables, domains, constrains):
        self.variables = variables
        self.domains = domains
        self.constrains = constrains   
        self.soluton = None

    def solve(self):
        self.assignment = {}
        self.soluton = self.backtrack(self.assignment)
        return self.soluton
    
    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            #we have asssigned values to all the variables, now the assignment is the solution
            return assignment
        #else it will execute the following code
        var = self.select_unassigned_variables(assignment)
    
    def select_unassigned_variables(self, assignment):
        unassigned_variables = []
        for variable in self.variables:
            if variable not in assignment:
                unassigned_variables.append(variable)
        return unassigned_variables
    




