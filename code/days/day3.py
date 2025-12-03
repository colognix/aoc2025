from days.base import Basesolver

class Solver(Basesolver):

    def solve_1(self):
        sum_j = 0
        for bank in self.input:
            j1 = max(bank)
            if bank.index(j1) == len(bank)-1:
                sum_j += max(bank[:-1])*10 + j1
            else:
                sum_j += max(bank[bank.index(j1)+1:]) + 10*j1
        return sum_j
    
    def solve_2(self):
        joltage_total = 0
        for bank in self.input:
            joltage_bank = 0
            n = 11
            while n > 0:
                s_tmp = max(bank[:-n])
                joltage_bank = 10*joltage_bank + s_tmp
                bank = bank[bank.index(s_tmp)+1:]
                n -= 1
            joltage_total += 10*joltage_bank+max(bank)
        return joltage_total
