'''
You just made a new friend at an international puzzle conference, 
and you asked for a way to keep in touch. You found the following note slipped 
under your hotel room door the next day:
"Salutations, new friend! I have replaced every digit of my phone number 
with its spelled-out uppercase English representation 
("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" 
for the digits 0 through 9, in that order), and then reordered all of those letters 
in some way to produce a string S. It's up to you to use S to figure out 
how many digits are in my phone number and what those digits are, 
but I will tell you that my phone number consists of those digits in nondecreasing order. 
Give me a call... if you can!"
You would to like to call your friend to tell him that 
this is an obnoxious way to give someone a phone number, 
but you need the phone number to do that! What is it?
'''
from collections import namedtuple,defaultdict

class NUMBER_STRING():
    def __init__(self,number_string):
        self.number_string = number_string
    
    def delete(self,old):
        for char in old:
            self.number_string = self.number_string.replace(char,"",1)
        return self.number_string
    
    def find(self,char):
        return self.number_string.find(char)

    def __repr__(self):
        return self.number_string



class TESTCASE():
    def __init__(self,number_string):
        self.number_string = NUMBER_STRING(number_string)

    def solve(self):
        #print("Original String: {}".format(self.number_string))
        num_dict = {"ZERO": 'Z',"TWO": 'W',"FOUR": 'U',"SIX": 'X',"EIGHT": 'G'}
        occurence = defaultdict(int)
        occurence, remained_string = self.find_number(self.number_string,num_dict,occurence)
        #print("first occurence: {}".format(occurence))
        num_dict = {"ONE": 'O',"THREE": 'H',"FIVE": 'F',"SEVEN": 'V',"NINE": 'N'}
        occurence, _ = self.find_number(remained_string,num_dict,occurence)
        #print("second occurence: {}".format(occurence))
        answer_string = ""
        answer_string = self.concatenate(answer_string,occurence)
        #print("answer string: {}".format(answer_string))
        return answer_string

    
    def concatenate(self,answer_string,occurence):
        all_num_dict = {"ZERO": '0',"ONE": '1',"TWO": '2',"THREE": '3',"FOUR": '4',"FIVE": '5',"SIX": '6',"SEVEN": '7',"EIGHT": '8',"NINE": '9'}
        for num_string, num_integer in all_num_dict.items():
            answer_string += num_integer*occurence[num_string]
        return answer_string
        

    
    
    def find_number(self,number_string,num_dict,occurence):
        remained_string = number_string
        for num, flag in num_dict.items():
            while number_string.find(flag) != -1:
                occurence[num] += 1
                remained_string = NUMBER_STRING(number_string.delete(num))
        return occurence, remained_string
    


def data_preprocessing(input_file):
    testcases=['index_start_from_1']
    with open(input_file,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            #----------------------Parsing Logic----------------------#
            number_string = f.readline().rstrip('\n')
            testcases.append(TESTCASE(number_string))
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
        