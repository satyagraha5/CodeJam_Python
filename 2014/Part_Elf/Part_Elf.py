'''
Vida says she's part Elf: that at least one of her ancestors was an Elf. 
But she doesn't know if it was a parent (1 generation ago), a grandparent (2 generations ago), 
or someone from even more generations ago. Help her out!
Being part Elf works the way you probably expect. People who are Elves, 
Humans and part-Elves are all created in the same way: two parents get together and have a baby. 
If one parent is A/B Elf, and the other parent is C/D Elf, then their baby will be (A/B + C/D) / 2 Elf. 
For example, if someone who is 0/1 Elf and someone who is 1/2 Elf have a baby, that baby will be 1/4 Elf.
Vida is certain about one thing: 40 generations ago, she had 240 different ancestors, and each one of them was 1/1 Elf or 0/1 Elf.
Vida says she's P/Q Elf. Tell her what is the minimum number of generations ago 
that there could have been a 1/1 Elf in her family. If it is not possible for her to be P/Q Elf, 
tell her that she must be wrong!
'''

from collections import namedtuple


class TESTCASE():
    def __init__(self,numerator,denominator):
        self.P = int(numerator)
        self.Q = int(denominator)


    def solve(self):
        P, Q = self.fraction_shape(self.P,self.Q)
        if self.first_filter(Q) is False:
            return "impossible"
        generation = 0
        current = self.P/self.Q
        while current < 1/2:
            current *= 2
            generation += 1
        generation += 1
        return generation

    def fraction_shape(self,numerator,denominator):
        gcd = self.gcd(numerator,denominator)
        numerator /= gcd
        denominator /= gcd
        return int(numerator), int(denominator)

    
    def first_filter(self,Q):
        if self.judge_power_of_n(Q,2) is False:
            return False
        return True

    
    def judge_power_of_n(self,suspect,n):
        k = 0
        while pow(n,k) <= suspect:
            if pow(n,k) == suspect:
                return True
            k += 1
        return False
        
    
    def gcd(self,n,m):
        if m > n:
            n, m = m, n
        dividend = n
        divisor = m
        remainder = n%m
        while remainder != 0:
            dividend = divisor
            divisor = remainder
            remainder = dividend%divisor
        return divisor

def data_preprocessing(input_file):
    testcases=['index_start_from_1']
    with open(input_file,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            #----------------------Parsing Logic----------------------#
            numerator, denominator = f.readline().rstrip('\n').split("/")
            testcases.append(TESTCASE(numerator,denominator))
            #--------------------------End----------------------------#
    return testcases


def model(testcases):
    answers = ['index_start_from_1']
    for testcase in testcases[1:]:
        answer = testcase.solve()
        answers.append(answer)
    return answers


def view(output_file,answers):    
    fmt_string="Case #{0}: {1}\n"
    with open(output_file,'w') as f:
        for n_th, answer in enumerate(answers[1:],1):
            f.write(fmt_string.format(n_th,answer))  


def controller():
    #Test Conditions
    suspect = "large-practice"
    difficulty = 'A'
    input_file = '{}-{}.in'.format(difficulty,suspect)
    output_file = '{}-{}.out'.format(difficulty,suspect)
    #----------------------Data Preprocessing----------------------#
    testcases = data_preprocessing(input_file)
    #----------------------------Model-----------------------------#
    answers = model(testcases = testcases)
    #-----------------------------View-----------------------------#
    view(output_file = output_file,answers = answers)   


if __name__=="__main__":
    controller()
        