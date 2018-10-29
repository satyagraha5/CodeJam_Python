'''
Annie is a bus driver with a high-stress job. She tried to unwind by going on a Caribbean cruise, 
but that also turned out to be stressful, so she has recently taken up horseback riding.
Today, Annie is riding her horse to the east along a long and narrow one-way road that runs west to east. 
She is currently at kilometer 0 of the road, and her destination is at kilometer D; 
kilometers along the road are numbered from west to east.
There are N other horses traveling east on the same road; all of them will go on traveling forever, 
and all of them are currently between Annie's horse and her destination. 
The i-th of these horses is initially at kilometer Ki and is traveling at its maximum speed of Si kilometers per hour.
Horses are very polite, and a horse H1 will not pass (move ahead of) another horse H2 that started off ahead of H1.
(Two or more horses can share the same position for any amount of time; you may consider the horses to be single points.)
Horses (other than Annie's) travel at their maximum speeds, 
except that whenever a horse H1 catches up to another slower horse H2, H1 reduces its speed to match the speed of H2.
Annie's horse, on the other hand, does not have a maximum speed and can travel at any speed that Annie chooses, 
as long as it does not pass another horse. To ensure a smooth ride for her and her horse, 
Annie wants to choose a single constant "cruise control" speed for her horse for the entire trip, 
from her current position to the destination, such that her horse will not pass any other horses. 
What is the maximum such speed that she can choose?
'''

TEST = 'sample'
IN = 'A-{}.in'.format(TEST)
OUT = 'A-{}.out'.format(TEST)



from collections import namedtuple


class TESTCASE():
    def __init__(self,n_th_testcase,destination,num_of_horses,horses):
        '''
            n_th_testcase : INT
            destination : INT
            num_of_horses : INT
            horses : NAMEDTUPLE(HORSE-kilometer,speed)
        '''
        self.n_th_testcase=n_th_testcase 
        self.destination=destination 
        self.num_of_horses=num_of_horses 
        self.horses=horses
    def __repr__(self):
        fmt_string="n_th_testcase : {}\ndestination : {}\nnum_of_horses : {}\nhorses : {}"
        return fmt_string.format(self.n_th_testcase,self.destination,self.num_of_horses,self.horses[1:])


def data_preprocessing():
    testcases=['index_start_from_1']
    with open(IN,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            destination, num_of_horses=(int(char) for char in f.readline().rstrip('\n').split(" "))
            HORSE=namedtuple("horse","kilometer speed")
            horses=['index_start_from_1']
            for n_th_horse in range(1,num_of_horses+1):
                kilometer, speed=(int(char) for char in f.readline().rstrip('\n').split(" "))
                horses.append(HORSE(kilometer,speed))
            testcases.append(TESTCASE(n_th_testcase,destination,num_of_horses,horses))
    return testcases


def find_answer(*,testcase):
    max_time=0
    for each_horse in testcase.horses[1:]:
        case_time=(testcase.destination-each_horse.kilometer)/each_horse.speed
        max_time=max(max_time,case_time)
        min_speed=testcase.destination/max_time
    return min_speed


    
def controller(*,testcases):
    fmt_string="Case #{0}: {1}\n"
    with open(OUT,'w') as f:
        for n_th, n_th_testcase in enumerate(testcases[1:],1):
            f.write(fmt_string.format(n_th,find_answer(testcase=n_th_testcase)))    


def main():
        testcases=data_preprocessing()
        controller(testcases=testcases)


if __name__=="__main__":
    main()
        