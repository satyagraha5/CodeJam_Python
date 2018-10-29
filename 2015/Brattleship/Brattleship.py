'''
You're about to play a simplified "battleship" game with your little brother. 
The board for this game is a rectangular grid with R rows and C columns. 
At the start of the game, you will close your eyes, and you will keep them closed 
until the end of the game. Your little brother will take a single rectangular 1 x W ship 
and place it horizontally somewhere on the board. The ship must always fit entirely on the board, 
with each cell of the ship occupying exactly one of the grid's cells, and it can never be rotated.
In each turn of the game, you name a cell on the board, 
and your little brother tells you whether that is a hit 
(one of the cells occupied by the ship) or a miss. 
(Your little brother doesn't say which part of the ship was hit -- 
just that the cell you named has a part of the ship in it.) You have perfect memory, 
and can keep track of all the information he has given you. 
Once you have named all of the cells occupied by the ship, the game is over (the ship is sunk), 
and your score is the number of turns taken. Your goal is to minimize your score.
Although the ship is not supposed to be moved once it is placed, 
you know that your little brother, who is a brat, 
plans to cheat by changing the location of the ship whenever he wants, 
as long as the ship remains horizontal and completely on the board, 
and the new location is consistent with all the information he has given so far. 
For example, for a 1x4 board and 1x2 ship, 
your little brother could initially place the ship such that it overlaps the leftmost two columns. 
If your first guess was row 1, column 2, 
he could choose to secretly move the ship to the rightmost two columns, 
and tell you that (1, 2) was a miss. If your next guess after that was (1, 3), 
though, then he could not say that was also a miss and move the ship back to its original location, 
since that would be inconsistent with what he said about (1, 2) earlier.
Not only do you know that your little brother will cheat, he knows that you know. 
If you both play optimally (you to minimize your score, him to maximize it), 
what is the lowest score that you can guarantee you will achieve, regardless of what your little brother does?
'''

from collections import namedtuple
from math import floor


class TESTCASE():
    def __init__(self,row,column,width):
        self.R = int(row)
        self.C = int(column)
        self.W = int(width)

    def solve(self):
        until_found = int(self.C / self.W)
        after_found = self.W - 1
        if self.C%self.W != 0:
            after_found += 1 #By rule of game, Game Theory. Brother will postpone until the edge of precipice
        answer = self.R * until_found + after_found
        return answer
 

def data_preprocessing(input_file):
    testcases=['index_start_from_1']
    with open(input_file,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            #----------------------Parsing Logic----------------------#
            row, column, width = f.readline().rstrip('\n').split(" ")
            testcases.append(TESTCASE(row, column, width))
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
        