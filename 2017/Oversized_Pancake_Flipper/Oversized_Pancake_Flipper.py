'''
Last year, the Infinite House of Pancakes introduced a new kind of pancake.
It has a happy face made of chocolate chips on one side (the "happy side"),
and nothing on the other side (the "blank side").
You are the head cook on duty. The pancakes are cooked in a single row over a hot surface. 
As part of its infinite efforts to maximize efficiency, 
the House has recently given you an oversized pancake flipper that flips exactly K consecutive pancakes. 
That is, in that range of K pancakes, it changes every happy-side pancake to a blank-side pancake, 
and vice versa; it does not change the left-to-right order of those pancakes.
You cannot flip fewer than K pancakes at a time with the flipper, 
even at the ends of the row (since there are raised borders on both sides of the cooking surface). 
For example, you can flip the first K pancakes, but not the first K - 1 pancakes.
Your apprentice cook, who is still learning the job, 
just used the old-fashioned single-pancake flipper to flip some individual pancakes 
and then ran to the restroom with it, right before the time when customers come to visit the kitchen. 
You only have the oversized pancake flipper left, 
and you need to use it quickly to leave all the cooking pancakes happy side up, 
so that the customers leave feeling happy with their visit.
Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper 
needed to leave all pancakes happy side up, or state that there is no way to do it.
'''

TEST = 'large-practice'
IN = 'A-{}.in'.format(TEST)
OUT = 'A-{}.out'.format(TEST)


from collections import namedtuple


class TESTCASE():
    def __init__(self,pancake_string, flipper_size):
        self.pancake_string = list(pancake_string)
        self.flipper_size = flipper_size
        self.time_of_flip = 0

    def __repr__(self):
        fmt_string="pancake_string : {0} flipper_size : {1}"
        return fmt_string.format(self.pancake_string,self.flipper_size)
    def solve(self):
        for position, pancake in enumerate(self.pancake_string):
            if position > len(self.pancake_string) - self.flipper_size:
                for pancake in self.pancake_string[position:]:
                    if pancake is "-":
                        return "IMPOSSIBLE"
                return self.time_of_flip
            else:
                if pancake is "-":
                    self.flip(position)
    
    
    def flip(self,position):
        for i_th,pancake in enumerate(self.pancake_string[position:position+self.flipper_size]):
            if pancake is "-":
                self.pancake_string[i_th + position] = "+"
            else:
                self.pancake_string[i_th + position] = "-"
        self.time_of_flip += 1
    


def data_preprocessing():
    testcases=['index_start_from_1']
    with open(IN,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            pancake_string, flipper_size = f.readline().rstrip('\n').split(" ")
            testcases.append(TESTCASE(pancake_string, int(flipper_size)))
    return testcases


def model(*,testcase):
    answer = testcase.solve()
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
        