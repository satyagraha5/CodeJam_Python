'''
A jamcoin is a string of N ≥ 2 digits with the following properties:
Every digit is either 0 or 1.
The first digit is 1 and the last digit is 1.
If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.
Not every string of 0s and 1s is a jamcoin. 
For example, 101 is not a jamcoin; its interpretation in base 2 is 5, which is prime. 
But the string 1001 is a jamcoin: in bases 2 through 10, 
its interpretation is 9, 28, 65, 126, 217, 344, 513, 730, and 1001, respectively, and none of those is prime.
We hear that there may be communities that use jamcoins as a form of currency. 
When sending someone a jamcoin, it is polite to prove that 
the jamcoin is legitimate by including a nontrivial divisor of that jamcoin's interpretation 
in each base from 2 to 10. (A nontrivial divisor for a positive integer K is some positive integer 
other than 1 or K that evenly divides K.) For convenience, these divisors must be expressed in base 10.
For example, for the jamcoin 1001 mentioned above, 
a possible set of nontrivial divisors for the base 2 through 10 
interpretations of the jamcoin would be: 3, 7, 5, 6, 31, 8, 27, 5, and 77, respectively.
Can you produce J different jamcoins of length N, along with proof that they are legitimate?
'''

TEST = 'large-practice'
IN = 'C-{}.in'.format(TEST)
OUT = 'C-{}.out'.format(TEST)


from collections import namedtuple

class TESTCASE():
    def __init__(self,length,number):
        self.length_of_jamcoin = int(length)
        self.number_of_jamcoin = int(number)


    def __repr__(self):
        fmt_string=""
        return fmt_string.format()
    

    def solve(self):
        jamcoins = []
        cases = self.make_cases()
        for ith, case in enumerate(cases,start=1):
            if ith > self.number_of_jamcoin:
                break
            jamcoins.append(self.make_jamcoins(case))
        return self.add_trivial_divisor(jamcoins)
    

    def make_cases(self):
        cases = [""]
        for ith in range(int(self.length_of_jamcoin/2)-2):
            zero_case = ["0" + case for case in cases]
            one_case = ["1" + case for case in cases]
            cases = zero_case + one_case
        return cases


    def make_jamcoins(self,case):
        case = case.replace("1","11")
        case = case.replace("0","00")
        return "11" + case + "11"
    

    def add_trivial_divisor(self,jamcoins):
        answer = [jamcoin + " 3 4 5 6 7 8 9 10 11" for jamcoin in jamcoins]
        return answer



def data_preprocessing():
    testcases=['index_start_from_1']
    with open(IN,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            length, number = f.readline().rstrip('\n').split(" ")
            testcases.append(TESTCASE(length, number))
    return testcases


def data_postprocessing(data):
    processed_data = ""
    for datum in data:
        processed_data += datum + "\n"
    return processed_data


def model(*,testcase):
    total_string = data_postprocessing(testcase.solve())
    return total_string

    
def controller_view(*,testcases):
    fmt_string="Case #{0}:\n{1}"
    with open(OUT,'w') as f:
        for n_th, n_th_testcase in enumerate(testcases[1:],1):
            f.write(fmt_string.format(n_th,model(testcase=n_th_testcase)))    


def main():
        testcases=data_preprocessing()
        controller_view(testcases=testcases)


if __name__=="__main__":
    main()
        