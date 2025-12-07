from days.base import Basesolver
import numpy as np

class Solver(Basesolver):

    # process input, override if neccessary
    def process_input(self,input):
        self.input = input


    def solve_1(self):
        beams = [self.input[0].index('S')]
        n_beams = len(beams)
        splits = 0
        for step in self.input[1:]:
            beams = [b for b in beams if step[b] == '.'] + [b+1 for b in beams if step[b] == '^'] + [b-1 for b in beams if step[b] == '^']
            splits += len(beams) - n_beams
            beams = list(set(beams))
            n_beams = len(beams)
        return splits
    
    def solve_2(self):
        # for each position, keeps track of how many timelines there are
        timeline_tracker = {}
        positions = [self.input[0].index('S')]
        timeline_tracker[self.input[0].index('S')] = 1
        for step in self.input[1:]:
            # for each position
            for p in positions:
                # if the particle splits on this position
                if step[p] == '^':
                    # keep track of the new beams with multitude of the dimensions
                    try:
                        timeline_tracker[p-1] += timeline_tracker[p]
                    except KeyError:
                        timeline_tracker[p-1] = timeline_tracker[p]
                    try:
                        timeline_tracker[p+1] += timeline_tracker[p]
                    except KeyError:
                        timeline_tracker[p+1] = timeline_tracker[p]
                    # the splitting position currently does not hold a beam
                    timeline_tracker[p] = 0
            # get positions for the next iterations
            positions = list(timeline_tracker.keys())
        # each position holds the number of dimensions that lead to it
        return sum(timeline_tracker.values())