'''
The kitchen at the Infinite House of Pancakes has just received an order for a stack of K pancakes!
The chef currently has N pancakes available, where N ≥ K. Each pancake is a cylinder,
and different pancakes may have different radii and heights.
As the sous-chef, you must choose K out of the N available pancakes, discard the others,
and arrange those K pancakes in a stack on a plate as follows. First, take the pancake that has the largest radius,
and lay it on the plate on one of its circular faces. (If multiple pancakes have the same radius, you can use any of them.)
Then, take the remaining pancake with the next largest radius and lay it on top of that pancake,
and so on, until all K pancakes are in the stack and the centers of the circular faces are aligned in a line perpendicular to the plate,
You know that there is only one thing your diners love as much as they love pancakes: syrup!
It is best to maximize the total amount of exposed pancake surface area in the stack,
since more exposed pancake surface area means more places to pour on delicious syrup.
Any part of a pancake that is not touching part of another pancake or the plate is considered to be exposed.
If you choose the K pancakes optimally, what is the largest total exposed pancake surface area you can achieve?
'''

'''
정밀도 향상 필요
'''


TEST = 'large-practice'
IN = 'A-{}.in'.format(TEST)
OUT = 'A-{}.out'.format(TEST)


from collections import namedtuple
from math import pi,pow
from decimal import Decimal

class TESTCASE():
    def __init__(self,n_th_testcase,num_of_pancakes,num_of_choice,pancakes):
        '''
            n_th_testcase : INT
            num_of_pancakes : INT
            num_of_choice : INT
            pancakes : NAMEDTUPLE(pancake-radius,height)
        '''
        self.n_th_testcase=n_th_testcase
        self.num_of_pancakes=num_of_pancakes
        self.num_of_choice=num_of_choice
        self.pancakes=pancakes

    def __repr__(self):
        fmt_string=""
        return fmt_string.format()

class PANCAKE():
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
    def upper(self):
        return pi*pow(self.radius,2)
    def side(self):
        return 2*pi*self.radius*self.height


def data_preprocessing():
    testcases=['index_start_from_1']
    with open(IN,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            num_of_pancakes, num_of_choice = (int(char) for char in f.readline().rstrip('\n').split(" "))
            pancakes=['index_start_from_1']
            for n_th in range(1,num_of_pancakes+1):
                radius, height=(int(char) for char in f.readline().rstrip('\n').split(" "))
                pancakes.append(PANCAKE(radius,height))
            testcases.append(TESTCASE(n_th_testcase,num_of_pancakes,num_of_choice,pancakes))
    return testcases


def model(*,testcase):
    answer=0
    testcase.pancakes[1:]=sorted(testcase.pancakes[1:],key=lambda pancake: (pancake.radius)*(pancake.height),reverse=True)
    for n_th, base in enumerate(testcase.pancakes[1:],1):
        surface=0
        surface+=base.upper()
        surface+=base.side()
        left_choice=testcase.num_of_choice-1
        for m_th,pancake in enumerate(testcase.pancakes[1:],1):
            if left_choice<=0:
                break
            if m_th is not n_th:
                if pancake.radius<=base.radius:
                    left_choice-=1
                    surface+=pancake.side()
        answer=max(answer,surface)
    return answer

    
def controller_view(*,testcases):
    fmt_string="Case #{0}: {1:.6f}\n"
    with open(OUT,'w') as f:
        for n_th, n_th_testcase in enumerate(testcases[1:],1):
            f.write(fmt_string.format(n_th,model(testcase=n_th_testcase)))    


def main():
        testcases=data_preprocessing()
        controller_view(testcases=testcases)


if __name__=="__main__":
    main()
        