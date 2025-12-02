from days.base import Basesolver

class Solver(Basesolver):

    # process input, override if neccessary
    def process_input(self,input):
        self.input = [l.split("-") for l in input[0].split(',')]

    def solve_1(self):
        s = 0
        
        for r0,r1 in self.input:
            
            len0, len1 = len(r0), len(r1)
            flen = len0
            if len0 == len1:
                # cleanup, only even number of numchars are possible targets
                if len0 % 2 != 0:
                    continue
            if len0 != len1:
                if len0 % 2 == 0:
                    r1 = "9"*len0
                else:
                    # only consider values which 
                    r0 = "1" + "0"*(len1-1)
                    flen += 1
            hlen = int(flen/2)

            s += sum([get_dup(i) for i in range(int(r0[:hlen]), int(r1[:hlen])+1) if get_dup(i) >= int(r0) and get_dup(i) <= int(r1)])
        
        return s
    
    def solve_2(self):

        s = 0

        for r0,r1 in self.input:
            dupes = []
            len0, len1 = len(r0), len(r1)
            if len0 == len1:
                # for each size of repeated numchars      
                for l in range(1,len0):
                    # only check if multiple possible
                    if len0 % l == 0:
                        # check if the possible multiples are in the given range (for this see check_mul)
                        dupes += [check_mul(i, int(len0/l), r0, r1) for i in range(int(r0[:l]), int(r1[:l])+1)]
                
            if len0 != len1:
                # split in two groups
                r0_0, r0_1, r1_0, r1_1 = r0, "1" + "0"*(len1-1), "9"*len0, r1
                # same as before
                for l in range(1,len0):
                    if len0 % l == 0:
                        dupes += [check_mul(i, int(len0/l), r0_0, r1_0) for i in range(int(r0_0[:l]), int(r1_0[:l])+1)]
                for l in range(1,len1):
                    if len1 % l == 0:
                        dupes += [check_mul(i, int(len1/l), r0_1, r1_1) for i in range(int(r0_1[:l]), int(r1_1[:l])+1)]
            
            # remove duplicate finds
            s += sum(set(dupes))
        
        return s


def get_dup(i):
    return int(str(i)+str(i))

def get_mul(i,n):
    return int(n*str(i))

def check_mul(i,n,r0,r1):
    val = get_mul(i,n)
    if val >= int(r0) and val <= int(r1):
        return val
    else:
        return 0

        
