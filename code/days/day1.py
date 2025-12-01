from days.base import Basesolver

class Solver(Basesolver):

    # process input, override if neccessary
    def process_input(self,input):
        rotation_dict = {'R':1,'L':-1}
        self.input = [[rotation_dict[l[0]]*(l[1] % 100), max(0, int(l[1]/100))] for l in input]

    def set_constants(self):
        self.position = 50
        return super().set_constants()

    # set part for checks and also load part dependent stuff, override if neccessary
    def set_part(self,part):
        self.set_constants()
        return super().set_part(part)

    def solve_1(self):
        c = 0
        for r in self.input:
            c += self.rotate_and_count(r)
        return c
    
    def solve_2(self):
        c = 0
        for r in self.input:
            c += self.rotate_and_count(r)
        return c

    def rotate_and_count(self,r):
        # rotate, save relative position
        relative_position = self.position + r[0]
        counter_clockwise_pass = self.position != 0 and (relative_position < 0)
        clockwise_pass = relative_position > 100
        self.position = (relative_position) % 100
        # check if 0 is hit
        hit = self.position == 0
        # return if 0 % 100 hit
        if self.part == 1:
            return int(hit)
        # check if 0 % 100 got passed or hit and add number of roundtrips
        if self.part == 2:
            return int(hit or counter_clockwise_pass or clockwise_pass) + r[1]
        
