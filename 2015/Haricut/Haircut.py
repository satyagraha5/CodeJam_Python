'''
You are waiting in a long line to get a haircut at a trendy barber shop. 
The shop has B barbers on duty, and they are numbered 1 through B. 
It always takes the kth barber exactly Mk minutes to cut a customer's hair, 
and a barber can only cut one customer's hair at a time. Once a barber finishes cutting hair, 
he is immediately free to help another customer.
While the shop is open, the customer at the head of the queue always 
goes to the lowest-numbered barber who is available. When no barber is available, 
that customer waits until at least one becomes available.
You are the Nth person in line, and the shop has just opened. Which barber will cut your hair?
'''
'''
Large Dataset 수정 필요
'''
from collections import namedtuple
from functools import reduce

class TESTCASE():
    def __init__(self,num_of_barbers,my_turn,barbers_duration):
        self.B = int(num_of_barbers)
        self.N = int(my_turn)
        self.B_list = [int(char) for char in barbers_duration]


    def solve(self):
        B = self.B
        B_list = self.B_list
        total_lcm = reduce(lambda x, y: self.lcm(x,y), B_list)
        #print("lcm of {} is {}".format(B_list,total_lcm))
        m_list = [int(total_lcm//duration) for duration in B_list] # M is LCM/B
        period = reduce(lambda x, y: x + y, m_list)
        #print("Period: {}".format(period))
        N = self.N%period
        if N is 0:
            N = period
        #print("N: {}".format(N))
        #matching_list = ['index_start_from_1'] + [0]*period
        remained_duration_list = [0]*B
        for i_th_customer in range(1,N+1):
            #print("select where {}th_customer shoud go".format(i_th_customer))
            #print("remained duration list: {}".format(remained_duration_list))
            if all(remained_duration_list) is True: #There is no barber at rest. all barbers are working
                #print("      There is no barber at rest")
                min_duration = reduce(lambda x, y: min(x,y),remained_duration_list) #Minimum of remained duration
                #print("      min duration: {}".format(min_duration))
                remained_duration_list = list(map(lambda x: x-min_duration,remained_duration_list)) #Wait until one barber at rest
                #print("      new remained duration list: {}".format(remained_duration_list))
            i_th_barber = remained_duration_list.index(0) #Index of one barber at rest
            #print("{}th customer is served by {}th_barber".format(i_th_customer,i_th_barber))
            #matching_list[i_th_customer] = i_th_barber + 1
            remained_duration_list[i_th_barber] += B_list[i_th_barber]
            #print("new remained duration list: {}\n".format(remained_duration_list))
        #print("matching_list: {}".format(matching_list[1:]))
        #print("{}th barber".format(matching_list[N]))
        return i_th_barber


    def gcd(self,a,b):
        if a < b:
            a, b = b, a
        while b > 0:
            a, b = b, a % b
        return a 


    def lcm(self,a,b):
        return int((a*b)//self.gcd(a, b))


def data_preprocessing(input_file):
    testcases=['index_start_from_1']
    with open(input_file,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            #----------------------Parsing Logic----------------------#
            num_of_barbers, my_turn = f.readline().rstrip('\n').split(" ") #String Type
            barbers_duration = f.readline().rstrip('\n').split(" ") #String Type
            testcases.append(TESTCASE(num_of_barbers,my_turn,barbers_duration))
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
    #sample
    #small-practice
    #large-practice
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
        