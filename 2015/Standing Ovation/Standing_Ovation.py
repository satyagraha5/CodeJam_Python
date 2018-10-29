'''
It's opening night at the opera, and your friend is the prima donna (the lead female singer). 
You will not be in the audience, but you want to make sure she receives a standing ovation 
-- with every audience member standing up and clapping their hands for her.
Initially, the entire audience is seated. Everyone in the audience has a shyness level.
An audience member with shyness level Si will wait until at least Si other audience members have already stood up to clap, 
and if so, she will immediately stand up and clap. If Si = 0, then the audience member will always stand up and clap immediately, 
regardless of what anyone else does. For example, an audience member with Si = 2 will be seated at the beginning, 
but will stand up to clap later after she sees at least two other people standing and clapping.
You know the shyness level of everyone in the audience, and you are prepared to invite additional friends of the prima donna 
to be in the audience to ensure that everyone in the crowd stands up and claps in the end. 
Each of these friends may have any shyness value that you wish, not necessarily the same. 
What is the minimum number of friends that you need to invite to guarantee a standing ovation?
'''

TEST = 'large-practice'
IN = 'A-{}.in'.format(TEST)
OUT = 'A-{}.out'.format(TEST)


from collections import namedtuple


class TESTCASE():
    def __init__(self, s_max, s_list):
        self.s_max = s_max
        self.s_list = s_list

    def __repr__(self):
        fmt_string="s_max : {0}\ns_list:{1}"
        return fmt_string.format(self.s_max, self.s_list)


def data_preprocessing():
    testcases=['index_start_from_1']
    with open(IN,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            s_max, s_list_raw = f.readline().rstrip('\n').split(" ")
            s_list = [int(char) for char in s_list_raw]
            testcases.append(TESTCASE(s_max = s_max, s_list = s_list))
    return testcases


def model(*,testcase):
    num_standing_people = 0
    additional_people = 0
    for s_i, num_s_i in enumerate(testcase.s_list):
        if num_standing_people >= s_i:
            num_standing_people += num_s_i
        else:
            additional_people += s_i - num_standing_people
            num_standing_people = s_i + num_s_i
    return additional_people


    
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
        