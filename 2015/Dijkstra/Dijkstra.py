'''
The Dutch computer scientist Edsger Dijkstra made many important contributions to the field, 
including the shortest path finding algorithm that bears his name. 
This problem is not about that algorithm.
You were marked down one point on an algorithms exam for misspelling "Dijkstra" -- between D and stra, 
you wrote some number of characters, each of which was either i, j, or k. 
You are prepared to argue to get your point back using quaternions, 
an actual number system (extended from complex numbers) with the following multiplicative structure:
To multiply one quaternion by another, look at the row for the first quaternion 
and the column for the second quaternion. For example, to multiply i by j, 
look in the row for i and the column for j to find that the answer is k. To multiply j by i, 
look in the row for j and the column for i to find that the answer is -k.
As you can see from the above examples, the quaternions are not commutative
that is, there are some a and b for which a * b != b * a. However they are associative
for any a, b, and c, it's true that a * (b * c) = (a * b) * c.
Negative signs before quaternions work as they normally do -- for any quaternions a and b, 
it's true that -a * -b = a * b, and -a * b = a * -b = -(a * b).
You want to argue that your misspelling was equivalent to the correct spelling ijk 
by showing that you can split your string of is, js, and ks in two places, forming three substrings, 
such that the leftmost substring reduces (under quaternion multiplication) to i, 
the middle substring reduces to j, and the right substring reduces to k. 
(For example, jij would be interpreted as j * i * j; j * i is -k, and -k * j is i, so jij reduces to i.) 
If this is possible, you will get your point back. Can you find a way to do it?
'''

from collections import namedtuple


class TESTCASE():
    def __init__(self,unit_length, multiple_times, unit_string):
        self.L = int(unit_length)
        self.X = int(multiple_times)
        self.S = unit_string


    def __repr__(self):
        fmt_string=""
        return fmt_string.format()
    

    def solve(self):
        return "NO"


    def first_filter(self):
        

class COMPLEX_IJK():
    def __init__(self,ijk):
        self.imaginary = ijk
    

    def __mul__(self,):
        if 

def data_preprocessing():
    testcases=['index_start_from_1']
    with open(IN,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            unit_length, multiple_times = f.readline().rstrip('\n').split(" ")
            unit_string = f.readline().rstrip('\n')
            testcases.append(TESTCASE(unit_length,multiple_times,unit_string))
    return testcases


def model(testcase):
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
    #------------------------Test Conditions----------------------#
    suspect = "sample"
    difficulty = 'C'
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
        