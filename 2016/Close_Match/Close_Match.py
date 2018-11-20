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
from collections import namedtuple,defaultdict

class CODER_JAMMER_PAIR():
    def __init__(self,coder,jammer):
        self.C = coder
        self.J = jammer

    def __getattr__(self, name):
        if name == 'C':
            return self.C
        elif name == 'J':
            return self.J
        else:
            raise IndexError

    def __str__(self):
        return "Coder: {} Jammer: {}".format(self.C.decode('utf-8'),self.J.decode('utf-8'))

    


class TESTCASE():
    def __init__(self,coder,jammer):
        self.C = bytearray(coder,'utf-8')
        self.J = bytearray(jammer,'utf-8')


    def solve(self):
        '''
            initial setting
        '''
        max_depth = len(self.C)
        possible_case_tree = defaultdict(list)
        initial_pair = CODER_JAMMER_PAIR(self.C, self.J)
        possible_case_tree[0].append(initial_pair)
        #possible_case_tree[0].append(self.current_decisions(initial_pair,0))
        for current_decision in self.current_decisions(initial_pair,0):
            possible_case_tree[0].append(current_decision)
        current_depth = 1

        '''
            making decision tree
        '''
        while current_depth < max_depth:
            #print(current_depth)
            past_depth = current_depth - 1
            for current_pair in possible_case_tree[past_depth]:
                for current_decision in self.current_decisions(current_pair,current_depth):
                    possible_case_tree[current_depth].append(current_decision)
            current_depth += 1
        #print("possible_case_tree: {}".format(possible_case_tree))
        self.pretty_print_defaultdict(possible_case_tree)


    def current_decisions(self,current_pair,depth):
        '''
            return list of CODER_JAMMER_PAIR
        '''
        C = current_pair.C
        J = current_pair.J
        c = chr(C[depth])
        j = chr(J[depth])
        if is_integer(c) is True and is_integer(j) is True:
            print("{} is integer and {} is integer".format(c,j))
            if are_same(c,j) is True:
                return [CODER_JAMMER_PAIR(C,J)]
            elif are_same(c,j) is False:
                return [self.fill_question_mark(C,J,depth)]
        elif is_integer(c) is True and is_integer(j) is False:
            print("{} is integer and {} is not integer".format(c,j))
            bigger = J
            bigger[depth] = (c + 1)%10
            same = J
            smaller = J
            smaller[depth] = (c - 1)%10
            return [CODER_JAMMER_PAIR(C,bigger), CODER_JAMMER_PAIR(C,same), CODER_JAMMER_PAIR(C,smaller)]
        elif is_integer(c) is False and is_integer(j) is True:
            print("{} is not integer and {} is integer".format(c,j))
            bigger = C
            bigger[depth] = (j + 1)%10
            same = C
            smaller = C
            smaller[depth] = (j - 1)%10
            return [CODER_JAMMER_PAIR(bigger,J), CODER_JAMMER_PAIR(same,J), CODER_JAMMER_PAIR(smaller,J)]
        elif is_integer(c) is False and is_integer(j) is False:
            print("{} is not integer and {} is not integer".format(c,j))
            one_C = C
            one_C[depth] = 1
            zero_C = C
            zero_C[depth] = 0
            one_J = J
            one_J[depth] = 1
            zero_J = J
            zero_J[depth] = 0
            return [CODER_JAMMER_PAIR(one_C,zero_J), CODER_JAMMER_PAIR(zero_C,zero_J), CODER_JAMMER_PAIR(zero_C,one_C)]
    

    def fill_question_mark(self,string_a,string_b,depth):
        '''
            return list
        '''
        if string_a[depth] > string_b[depth]:
            return CODER_JAMMER_PAIR(self.fill_smallest(string_a), self.fill_biggest(string_b))
        elif string_a[depth] < string_b[depth]:
            return CODER_JAMMER_PAIR(self.fill_biggest(string_a),self.fill_smallest(string_b))


    def fill_smallest(self,bigger):
        '''
            return str
        '''
        return bigger.replace(b'?',b'0')


    def fill_biggest(self,smaller):
        '''
            return str
        '''
        return smaller.replace(b'?',b'9')


    def pretty_print_defaultdict(self,possible_case_tree):
        for depth, decisions in possible_case_tree.items():
            print("depth: {}".format(depth))
            for decision in decisions:
                print(decision)



def is_integer(suspect):
    try:
        int(suspect)
    except ValueError:
        return False
    else:
        return True 


def are_same(a,b):
    if a == b:
        return True
    else:
        return False



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
        