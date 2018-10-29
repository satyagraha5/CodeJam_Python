'''
Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. 
First, she picks a number N. Then she starts naming N, 2 × N, 3 × N, and so on. 
Whenever she names a number, she thinks about all of the digits in that number. 
She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once 
so far as part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep.
Bleatrix must start with N and must always name (i + 1) × N directly after i × N. For example, 
suppose that Bleatrix picks N = 1692. She would count as follows:
N = 1692. Now she has seen the digits 1, 2, 6, and 9.
2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
3N = 5076. Now she has seen all ten digits, and falls asleep.
What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead.
'''


TEST = 'large-practice'
IN = 'A-{}.in'.format(TEST)
OUT = 'A-{}.out'.format(TEST)


from collections import namedtuple


class TESTCASE():
    def __init__(self,n):
        self.n = n
        self.current_n = n
        self.occured_digit_set = self.parsing(n)

    def __repr__(self):
        fmt_string="n :{0}\noccured_digit_set :{1}"
        return fmt_string.format(self.n, self.occured_digit_set)
    
    def parsing(self,n):
        digit_subset = {digit for digit in str(n)}
        return digit_subset
    def examine(self):
        if len(self.occured_digit_set) == 10:
            return True
        else:
            return False
    def first_level_filter(self):
        if self.n == 0:
            return False
    def iterate(self):
        if self.examine() is True:
            return self.current_n
        else:
            while(True):
                self.current_n += self.n
                self.occured_digit_set |= self.parsing(self.current_n)
                if self.examine() is True:
                    return self.current_n
            
    def solve(self):
        if self.first_level_filter() is False:
            return "INSOMNIA"
        else:
            return self.iterate()
def data_preprocessing():
    testcases=['index_start_from_1']
    with open(IN,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            n = int(f.readline())
            testcases.append(TESTCASE(n = n))
    return testcases


def model(*,testcase):
    answer = testcase.solve()
    return answer


    
def controller_view(*,testcases):
    fmt_string="Case #{0}: {1}\n"
    with open(OUT,'w') as f:
        for n_th, n_th_testcase in enumerate(testcases[1:],1):
            f.write(fmt_string.format(n_th,model(testcase=n_th_testcase)))    


def main():
        testcases=data_preprocessing()
        controller_view(testcases=testcases)


if __name__=="__main__":
    main()
        