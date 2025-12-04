from days.base import Basesolver
import numpy as np

class Solver(Basesolver):

    # process input, override if neccessary
    def process_input(self,input):

        self.input = input
        n = len(self.input)
        self.pr_dict = {}
        # preprocess a dictionary for each paper roll with adjacent nodes
        for i in range(n):
            for j in range(n):
                if input[i][j] == '@':
                    # encode index
                    self.pr_dict[1000*i+j] = set([])
                    for k,l in [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]:
                        
                        if k < n and k >= 0 and l < n and l >= 0:
                            if input[k][l] == '@':
                                try:
                                    self.pr_dict[1000*i+j].add(1000*k+l)
                                except KeyError:
                                    self.pr_dict[1000*i+j] = {1000*k+l}

        
        




    def set_constants(self):
        return super().set_constants()


    def solve_1(self):
        return len([p for p in self.pr_dict.keys() if len(self.pr_dict[p]) <  4])
    
    def solve_2(self):
        c = 0
        while True:
            removals = [p for p in self.pr_dict.keys() if len(self.pr_dict[p]) <  4]
            c += len(removals)
            for roll in removals:
                self.clean_neighbours(roll, self.pr_dict.pop(roll))
            if len(removals) == 0:
                return c
            
    def clean_neighbours(self,p,neighbours):
        for n in neighbours:
            try:
                self.pr_dict[n].remove(p)
            except ValueError:
                continue



            

        