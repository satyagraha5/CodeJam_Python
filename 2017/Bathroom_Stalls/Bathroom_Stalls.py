'''
A certain bathroom has N + 2 stalls in a single row; 
the stalls on the left and right ends are permanently occupied by the bathroom guards. 
The other N stalls are for users.
Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible.
To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values LS and RS,
each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively.
Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal.
If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal.
If there are still multiple tied stalls, they choose the leftmost stall among those.
K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.
When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?
'''


'''
실행시간 개선 필요
'''

TEST = 'C-small-practice-2'
IN = '{}.in'.format(TEST)
OUT = '{}.out'.format(TEST)


class TESTCASE():

    def __init__(self,num_of_stalls,num_of_people):
        self.num_of_stalls=num_of_stalls
        self.num_of_people=num_of_people

    def __repr__(self):
        fmt_string=""
        return fmt_string.format()

class BATHROOM():

    def __init__(self,num_of_stalls):
        self.num_of_stalls=num_of_stalls
        self.bathroom_array=[0]*self.num_of_stalls
        self.bathroom_array[0]=1
        self.bathroom_array[-1]=1
    

    def locate(self):
        location, max_LR, min_LR=self.find_location_length()
        self.bathroom_array[location]=1
        return max_LR, min_LR


    def find_location_length(self):
        max_length=0
        left_index=0
        for current_index,exist in enumerate(self.bathroom_array[1:],1):
            if exist is 1:
                length=current_index-left_index
                if length>max_length:
                    max_length=length
                    location=left_index+int((current_index-left_index)/2)
                    min_LR=location-left_index-1
                    max_LR=length-1-1-min_LR
                left_index=current_index
        return location, max_LR, min_LR


def data_preprocessing():
    testcases=['index_start_from_1']
    with open(IN,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            num_of_stalls, num_of_people=(int(char) for char in f.readline().rstrip('\n').split(" "))
            testcases.append(TESTCASE(num_of_stalls+2,num_of_people))
    return testcases


def model(*,testcase):
    bathroom=BATHROOM(testcase.num_of_stalls)
    for n_th in range(testcase.num_of_people):
        max_LR, min_LR=bathroom.locate()
    return max_LR, min_LR


    
def controller_view(*,testcases):
    fmt_string="Case #{0}: {1} {2}\n"
    with open(OUT,'w') as f:
        for n_th, n_th_testcase in enumerate(testcases[1:],1):
            max_LR,min_LR=model(testcase=n_th_testcase)
            f.write(fmt_string.format(n_th,max_LR,min_LR))    


def main():
        testcases=data_preprocessing()
        controller_view(testcases=testcases)


if __name__=="__main__":
    main()
        