'''
When Sergeant Argus's army assembles for drilling, they stand in the shape of an N by N square grid, 
with exactly one soldier in each cell. Each soldier has a certain height.
Argus believes that it is important to keep an eye on all of his soldiers at all times. 
Since he likes to look at the grid from the upper left, he requires that:
Within every row of the grid, the soldiers' heights must be in strictly increasing order, from left to right.
Within every column of the grid, the soldiers' heights must be in strictly increasing order, from top to bottom.
Although no two soldiers in the same row or column may have the same height, 
it is possible for multiple soldiers in the grid to have the same height.
Since soldiers sometimes train separately with their row or their column, 
Argus has asked you to make a report consisting of 2*N lists of the soldiers' heights: 
one representing each row (in left-to-right order) and column (in top-to-bottom order). 
As you surveyed the soldiers, you only had small pieces of paper to write on, 
so you wrote each list on a separate piece of paper. However, on your way back to your office, 
you were startled by a loud bugle blast and you dropped all of the pieces of paper, 
and the wind blew one away before you could recover it! The other pieces of paper are now in no particular order, 
and you can't even remember which lists represent rows and which represent columns, since you didn't write that down.
You know that Argus will make you do hundreds of push-ups if you give him an incomplete report. 
Can you figure out what the missing list is?
'''

from collections import namedtuple


class TESTCASE():
    def __init__(self,map_length,height_lists):
        self.map_length = map_length
        self.heigth_lists = height_lists

    def __repr__(self):
        fmt_string=""
        return fmt_string.format()

    def solve(self):
        sieve = []
        for height_list in self.heigth_lists:
            for num in height_list:
                if num not in sieve:
                    sieve.append(num)
                else: #num is in sieve
                    sieve.pop(sieve.index(num))
        sieve.sort(key=int)
        return " ".join(sieve)
        

def data_preprocessing(input_file):
    testcases=['index_start_from_1']
    with open(input_file,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            #----------------------Parsing Logic----------------------#
            map_length = int(f.readline())
            height_lists = []
            for n_th_list in range(1,2*map_length - 1 + 1):
                height_list = f.readline().rstrip('\n').split(" ")
                height_lists.append(height_list)
            testcases.append(TESTCASE(map_length, height_lists))
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
        