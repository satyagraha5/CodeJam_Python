

'''
An N-omino is a two-dimensional shape formed by joining N unit cells fully along their edges in some way. 
More formally, a 1-omino is a 1x1 unit square, and an N-omino is an (N-1)omino 
with one or more of its edges joined to an adjacent 1x1 unit square. For the purpose of this problem, 
we consider two N-ominoes to be the same if one can be transformed into the other via reflection 
and/or rotation. For example, these are the five possible 4-ominoes
Richard and Gabriel are going to play a game with the following rules, 
for some predetermined values of X, R, and C:
1. Richard will choose any one of the possible X-ominoes.
2. Gabriel must use at least one copy of that X-omino, along with arbitrarily 
many copies of any X-ominoes (which can include the one Richard chose), 
to completely fill in an R-by-C grid, with no overlaps and no spillover. 
That is, every cell must be covered by exactly one of the X cells making up an X-omino, 
and no X-omino can extend outside the grid. Gabriel is allowed to rotate or reflect 
as many of the X-ominoes as he wants, including the one Richard chose. 
If Gabriel can completely fill in the grid, he wins; otherwise, Richard wins.
Given particular values X, R, and C, can Richard choose an X-omino that will ensure that he wins, 
or is Gabriel guaranteed to win no matter what Richard chooses?
'''


class TESTCASE():
    def __init__(self,X,R,C):
        self.X = int(X)
        self.R = int(R)
        self.C = int(C)

    def __repr__(self):
        fmt_string=""
        return fmt_string.format()
    
    def solve(self):
        return self.Richard_versus_Gabriel()
    

    def Richard_versus_Gabriel(self):
        if self.first_filter() is False: # (R*C)%X != 0
            return "RICHARD"
        elif self.second_filter() is False: # X >= 7
            return "RICHARD"
        if self.fill_X_omino(self.X) is False:
            return "RICHARD"
        else:
            return "GABRIEL"

    def first_filter(self):
        if (self.R * self.C)%self.X is not 0:
            return False
        return True


    def second_filter(self):
        if self.X >= 7:
            return False
        return True
    

    def fill_X_omino(self,X):
        long_side = max(self.R, self.C)
        short_side = min(self.R, self.C)
        if X <= 2:
            return True #GABRIEL
        elif X == 3:
            if short_side == 1:
                return False #RICHARD
            else:
                return True #GABRIEL
        elif X == 4:
            if short_side <= 2:
                return False #RICHARD
            else:
                return True #GABRIEL
        elif X == 5:
            if short_side <= 2:
                return False #RICHARD
            elif short_side == 3:
                if long_side > 5:
                    return True #GABRIEL
                else: #long_side == 5
                    return False #RICHARD
            else:
                return True #GABRIEL
        else: # X == 6
            if short_side <= 3:
                return False #RICHARD
            else: 
                return True #GABRIEL




def data_preprocessing(input_file):
    testcases=['index_start_from_1']
    with open(input_file,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            X, R, C = f.readline().rstrip('\n').split(" ")
            testcases.append(TESTCASE(X,R,C))
    return testcases


def model(testcase):
    answer = testcase.solve()
    return answer


def view(output_file,answers):    
    fmt_string="Case #{0}: {1}\n"
    with open(output_file,'w') as f:
        for n_th, answer in enumerate(answers[1:],1):
            f.write(fmt_string.format(n_th,answer))  


def controller():
    #Conditions
    suspect = "large-practice"
    difficulty = 'D'
    input_file = '{}-{}.in'.format(difficulty,suspect)
    output_file = '{}-{}.out'.format(difficulty,suspect)
    #Answer list
    answers = ['index_start_from_1']
    #Data Preprocessing
    testcases = data_preprocessing(input_file)
    for n_th, n_th_testcase in enumerate(testcases[1:],1):
        #Model
        answers.append(model(testcase = n_th_testcase))
        #View
        view(output_file = output_file,answers = answers)
          

if __name__=="__main__":
    controller()
        