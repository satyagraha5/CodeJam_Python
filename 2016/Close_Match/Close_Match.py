'''
You are attending the most important game in sports history. 
The Oceania Coders are playing the Eurasia Jammers in the Centrifugal Bumble-Puppy world finals. 
Unfortunately, you were sleep deprived from all the anticipation, so you fell asleep during the game!
The scoreboard is currently displaying both scores, perhaps with one or more leading zeroes 
(because the scoreboard displays a fixed number of digits). 
While you were asleep, some of the lights on the scoreboard were damaged by strong ball hits, 
so one or more of the digits in one or both scores are not being displayed.
You think close games are more exciting, and you would like to imagine 
that the scores are as close as possible. Can you fill in all of the missing digits 
in a way that minimizes the absolute difference between the scores? 
If there is more than one way to attain the minimum absolute difference, 
choose the way that minimizes the Coders' score. 
If there is more than one way to attain the minimum absolute difference 
while also minimizing the Coders' score, choose the way that minimizes the Jammers' score.
'''
from collections import namedtuple


class TESTCASE():
    def __init__(self,coder,jammer):
        self.C = coder
        self.J = jammer


    def solve(self):


class NUMBER_STRING_WITH_Q_MARK():
    def __init__(self,original_string):
        self.S = original_string
        self.G = [] #Guesses
    

    def 


def data_preprocessing(input_file):
    testcases=['index_start_from_1']
    with open(input_file,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            #----------------------Parsing Logic----------------------#
            coder, jammer =  f.readline().rstrip('\n').split(" ")
            testcases.append(TESTCASE(coder,jammer))
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
    suspect = "sample"
    difficulty = 'B'
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
        