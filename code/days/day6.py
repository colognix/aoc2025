from days.base import Basesolver
import math

class Solver(Basesolver):

    # process input, override if neccessary
    def process_input(self,input):
        self.input = input


    def solve_1(self):
        # prepare computation commands
        computations = []
        for l in self.input:
            computations += [l.replace('\n','').split()]
        # get computations by column-wise reordering
        computations = [list(x) for x in zip(*computations)]
        c = 0
        for p in computations:
            if p[-1] == '+':
                c += sum([int(v) for v in p[:-1]])
            if p[-1] == '*':
                c += math.prod([int(v) for v in p[:-1]])

        return c
    
    def solve_2(self):
        computations = []
        for line in self.input:
            computations += [[c for c in line[::-1].replace('\n','')]]
        computations = [list(x) for x in zip(*computations)]    

        c = 0
        current_val = None
        mul = None

        for p in computations[::-1]:
            try:
                # initialize new computation
                if p[-1] == '*':
                    current_val = get_number(p[:-1])
                    mul = True
                elif p[-1] == '+':
                    current_val = get_number(p[:-1])
                    mul = False
                # perform computation on other values
                else:
                    if mul:
                        current_val *= get_number(p)
                    else:
                        current_val += get_number(p)
            # ValueError is thrown on empty line aka current computation finished
            except ValueError:
                c += current_val
        # add up last computation
        return c + current_val

def get_number(s):
    return int(''.join(s).replace(' ', ''))      