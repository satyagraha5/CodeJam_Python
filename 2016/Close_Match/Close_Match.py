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
from copy import deepcopy

class CODER_JAMMER_PAIR():
    def __init__(self,coder,jammer):
        """
            Args:
                coder (list)
                jammer (list)
            Returns:
        """
        self.C = coder
        self.J = jammer

    def __getattr__(self, name):
        """
            Args:
                name (str)
            Returns:
                self.C (list)
                self.J (list)
        """
        if name == 'C':
            return self.C
        elif name == 'J':
            return self.J
        else:
            raise IndexError

    def __str__(self):
        coder = ''.join(self.C)
        jammer = ''.join(self.J)
        return "Coder: {} Jammer: {}".format(coder,jammer)

    def __repr__(self):
        coder = ''.join(self.C)
        jammer = ''.join(self.J)
        return "Coder: {} Jammer: {}".format(coder,jammer)

    


class TESTCASE():
    def __init__(self,coder,jammer):
        """
            Args:
                coder (str)
                jammer (str)
        """
        self.C = list(coder)
        self.J = list(jammer)
        self.max_depth = len(self.C)


    def solve(self):
        """
            Variables:
                self.C (list)
                self.J (list)
                max_depth (int)
                possible_case_tree (defaultdict)
                initial_pair (CODER_JAMMER_PAIR)
        """
        possible_case_tree = defaultdict(list)
        initial_pair = CODER_JAMMER_PAIR(self.C, self.J)
        print("original - {}".format(initial_pair))
        #possible_case_tree[0].append(self.current_decisions(initial_pair,0))
        end, decisions = self.current_decisions(initial_pair,depth= 0)
        if end is True:
            for decision in decisions:
                possible_case_tree[self.max_depth].append(decision)
        else:
            for decision in decisions:
                possible_case_tree[current_depth].append(decision)
        current_depth = 1
        while current_depth < self.max_depth:
            #print(current_depth)
            past_depth = current_depth - 1
            for current_pair in possible_case_tree[past_depth]:
                if current_pair == []:
                    break
                end, decisions = self.current_decisions(current_pair,depth= current_depth)
                if end is True:
                    for decision in decisions:
                        possible_case_tree[self.max_depth].append(decision)
                else:
                    for decision in decisions:
                        possible_case_tree[current_depth].append(decision)
            current_depth += 1
        #print("possible_case_tree: {}".format(possible_case_tree))
        #self.pretty_print_defaultdict(possible_case_tree)


    def current_decisions(self,current_pair,depth):
        """
            Make possilbe decisions in current CODER_JAMMER_PAIR and depth
            Args:
                current_pair (CODER_JAMMER_PAIR)
                depth (int)
            Variables:
                C (list): coder string list
                J (list): jammer string list
                c (str): current focused char in C
                j (str): current focused char in J
            Returns :
                list of CODE_JAMMER_PAIR
        """
        print("current- {}".format(current_pair))
        C = current_pair.C
        J = current_pair.J
        c = C[depth]
        j = J[depth]
        if is_integer(c) is True and is_integer(j) is True:
            #print("{} is integer and {} is integer".format(c,j))
            if are_same(c,j) is True:
                current_decision = [CODER_JAMMER_PAIR(C,J)]
                end = False
                return (end, current_decision)
            elif are_same(c,j) is False:
                all_filled_coder, all_filled_jammer = self.fill_question_mark(C,J,depth)
                current_decision = [CODER_JAMMER_PAIR(all_filled_coder,all_filled_jammer)]
                end = True
                print("current decision: {}".format(current_decision))
                return (end, current_decision)
        elif is_integer(c) is True and is_integer(j) is False:
            #print("{} is integer and {} is not integer".format(c,j))
            bigger = self.next_num(J,depth)
            smaller = self.past_num(J,depth)
            current_decision = [CODER_JAMMER_PAIR(C,bigger), CODER_JAMMER_PAIR(C,J), CODER_JAMMER_PAIR(C,smaller)]
            end = True
            print("current decision: {}".format(current_decision))
            return (end, current_decision)
        elif is_integer(c) is False and is_integer(j) is True:
            #print("{} is not integer and {} is integer".format(c,j))
            bigger = self.next_num(C,depth)
            smaller = self.past_num(C,depth)
            decision_bigger = self.fill_question_mark(bigger,J,depth= depth)
            decision_smaller = self.fill_question_mark(smaller,J,depth= depth)
            current_decision = [CODER_JAMMER_PAIR(bigger,J), CODER_JAMMER_PAIR(C,J), CODER_JAMMER_PAIR(smaller,J)]
            end = True
            print("current decision: {}".format(current_decision))
            return (end, current_decision)
        elif is_integer(c) is False and is_integer(j) is False:
            #print("{} is not integer and {} is not integer".format(c,j))
            one_C = self.one_num(C,depth)
            zero_C = self.zero_num(C,depth)
            one_J = self.one_num(J,depth)
            zero_J = self.zero_num(J,depth)
            current_decision = [CODER_JAMMER_PAIR(one_C,zero_J), CODER_JAMMER_PAIR(zero_C,zero_J), CODER_JAMMER_PAIR(zero_C,one_J)]
            end = True
            print("current decision: {}".format(current_decision))
            return (end, current_decision)
    

    def next_num(self,old_list,depth):
        """
            Return one more than num_list
            Args:
                old_list (list)
                depth (int)
            Returns:
                new_list (list)
        """
        new_list = deepcopy(old_list)
        if new_list[depth] == '9':
            new_list[depth] = '0'
            return new_list
        else:
            new_list[depth] = str(int(new_list[depth]) + 1)
            return new_list

    
    def past_num(self,old_list,depth):
        """
            Return one less than num_list
            Args:
                old_list (list)
                depth (int)
            Returns:
                new_list (list)
        """
        new_list = deepcopy(old_list)
        if new_list[depth] == '0':
            new_list[depth] = '9'
            return new_list
        else:
            new_list[depth] = str(int(new_list[depth]) - 1)
            return new_list

    
    def zero_num(self,old_list,depth):
        """
            Return filled zero list
            Args:
                old_list (list)
                depth (int)
            Returns:
                new_list (list)
        """
        new_list = deepcopy(old_list)
        new_list[depth] = '0'
        return new_list
    

    def one_num(self,old_list,depth):
        """
            Return filled one list
            Args:
                old_list (list)
                depth (int)
            Returns:
                new_list (list)
        """
        new_list = deepcopy(old_list)
        new_list[depth] = '1'
        return new_list


    def fill_question_mark(self,list_a,list_b,depth):
        """
            Fill as big as possible smaller one, and vice versa
            Args:
                list_a (list)
                list_b (list)
                depth (int)
            Returns:
                (tuple)
        """
        if list_a[depth] > list_b[depth]:
            return (self.fill_smallest(list_a), self.fill_biggest(list_b))
        elif list_a[depth] < list_b[depth]:
            return (self.fill_biggest(list_a),self.fill_smallest(list_b))


    def fill_smallest(self,bigger):
        """
            Fill question mark with 0
            Args:
                bigger (list)
            Returns:
                (list)
        """
        return replace_list(bigger,old_char= '?',new_char= '0')


    def fill_biggest(self,smaller):
        """
            Fill question mark with 9
            Args:
                bigger (list)
            Returns:
                (list)
        """
        return replace_list(smaller,old_char= '?',new_char= '9')


    def pretty_print_defaultdict(self,possible_case_tree):
        """
            Print defaultdict wrapper
            Args:
                possible_case_tree (defaultdict)
        """
        for depth, decisions in possible_case_tree.items():
            print("depth: {}".format(depth))
            for decision in decisions:
                print(decision)


def replace_list(old_list,old_char,new_char):
    new_list = deepcopy(old_list)
    for index, char in enumerate(old_list):
        if char == old_char:
            new_list[index] = new_char
    return new_list


def is_integer(suspect):
    """
        Judge suspect is integer or not
        Args:
            suspect (any)
        Returns:
            (bool)
    """
    try:
        int(suspect)
    except ValueError:
        return False
    else:
        return True 


def are_same(a,b):
    """
        Judge two object are same
        Args:
            a (any)
            b (any)
        Returns:
            (bool)
    """
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
        