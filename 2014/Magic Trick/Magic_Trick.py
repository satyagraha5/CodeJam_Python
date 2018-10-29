'''
Recently you went to a magic show. You were very impressed by one of the tricks,
so you decided to try to figure out the secret behind it!
The magician starts by arranging 16 cards in a square grid: 4 rows of cards, with 4 cards in each row. 
Each card has a different number from 1 to 16 written on the side that is showing. 
Next, the magician asks a volunteer to choose a card, and to tell him which row that card is in.
Finally, the magician arranges the 16 cards in a square grid again, possibly in a different order. 
Once again, he asks the volunteer which row her card is in. 
With only the answers to these two questions, the magician then correctly determines which card the volunteer chose. Amazing, right?
You decide to write a program to help you understand the magician's technique. 
The program will be given the two arrangements of the cards, and the volunteer's answers to the two questions: 
the row number of the selected card in the first arrangement, and the row number of the selected card in the second arrangement. 
The rows are numbered 1 to 4 from top to bottom.
Your program should determine which card the volunteer chose; 
or if there is more than one card the volunteer might have chosen (the magician did a bad job); 
or if there's no card consistent with the volunteer's answers (the volunteer cheated).
'''

TEST = 'small-practice'
IN = 'A-{}.in'.format(TEST)
OUT = 'A-{}.out'.format(TEST)


from collections import namedtuple


class TESTCASE():
    def __init__(self):
        self.first_guess = 0
        self.second_guess = 0
        self.first_map = []
        self.second_map = []
    

    def __repr__(self):
        fmt_string="first_guess: {0}\nfirst_map: {1}\nsecond_guess: {2}\nsecond_map: {3}"
        return fmt_string.format(self.first_guess,self.first_map,self.second_guess,self.second_map)


def data_preprocessing():
    testcases=['index_start_from_1']
    with open(IN,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            testcase = TESTCASE()
            testcase.first_guess = int(f.readline())
            for n_th_line in range(4):
                 testcase.first_map.append([int(num) for num in f.readline().rstrip('\n').split(" ")])
            testcase.second_guess = int(f.readline())
            for n_th_line in range(4):
                testcase.second_map.append([int(num) for num in f.readline().rstrip('\n').split(" ")])
            testcases.append(testcase)
    return testcases


def model(*,testcase):
    first_suspect = set(testcase.first_map[testcase.first_guess-1])
    second_suspect = set(testcase.second_map[testcase.second_guess-1])
    criminal = first_suspect & second_suspect
    if len(criminal) > 1:
        answer = "Bad magician!"
    elif len(criminal) == 1:
        answer = str(list(criminal)[0])
    else:
        answer = "Volunteer cheated!"
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
        