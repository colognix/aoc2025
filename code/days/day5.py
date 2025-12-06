from days.base import Basesolver

class Solver(Basesolver):

    # process input, override if neccessary
    def process_input(self,input):
        self.id_ranges = []
        self.id_list = []
        for l in input:
            if l != '':
                if '-' in l:
                    r_min,r_max = [int(r) for r in l.split('-')]
                    self.id_ranges += [[r_min,r_max]]
                else:
                    self.id_list += [int(l)]


    def solve_1(self):
        c = 0
        for i in self.id_list:
            for r in self.id_ranges:
                if i >= r[0] and i <= r[1]:
                    c += 1
                    break
        return c
    def solve_2(self):
        while True:    
            ranges = []
            n = len(self.id_ranges)
            
            for r in self.id_ranges:
                new_range = True
                for r1 in ranges:
                    if r[0] <= r1[0] and r[1] >= r1[1]:
                        ranges.remove(r1)
                        ranges += [r]
                        new_range = False
                        break
                    elif r[0] <= r1[0] and r[1] >= r1[0]:
                        ranges.remove(r1)
                        ranges += [[r[0],r1[1]]]
                        new_range = False
                        break
                    elif r[1] >= r1[1] and r[0] <= r1[1]:
                        ranges.remove(r1)
                        ranges += [[r1[0],r[1]]]
                        new_range = False
                        break
                    elif r[0] >= r1[0] and r[1] <= r1[1]:
                        new_range = False
                        break
                if new_range:
                    ranges += [r]
            if len(self.id_ranges) == len(ranges):
                break
            self.id_ranges = ranges

        return(sum([r[1]-r[0]+1 for r in ranges]))

        