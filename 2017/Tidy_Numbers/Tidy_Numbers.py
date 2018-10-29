'''
Tatiana likes to keep things tidy. 
Her toys are sorted from smallest to largest, 
her pencils are sorted from shortest to longest and her computers from oldest to newest. 
One day, when practicing her counting skills, she noticed that some integers, 
when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. 
Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. 
Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.
She just finished counting all positive integers in ascending order from 1 to N. 
What was the last tidy number she counted?
'''

TEST = 'large-practice'
IN = 'B-{}.in'.format(TEST)
OUT = 'B-{}.out'.format(TEST)


from collections import namedtuple

class Not_Tidy(Exception):
    pass

class TESTCASE():
    def __init__(self,original_number):
        self.original_number = original_number


    def __repr__(self):
        fmt_string="original_number : {0}"
        return fmt_string.format(self.original_number)
    

    def investigate(self,suspect):
        start_index = 0
        for index in range(len(suspect)-1):
            if suspect[index+1] < suspect[index]:
                raise Not_Tidy({"start_index" : start_index})
            elif suspect[index+1] > suspect[index]:
                start_index = index+1
            #if suspect[index+1] == suspect[index]:
            #나중에 숫자를 바꿔야할때 다같이 바꿔야한다.


    def surgery(self,start_index,patient):
        patient[start_index] -= 1
        for index in range(start_index+1,len(patient)):
            patient[index] = 9
        return patient



    def solve(self,original_number):
        number_string = [int(num_char) for num_char in original_number]
        answer = number_string
        try:
            self.investigate(suspect=number_string)
        except Not_Tidy as e:
            answer = self.surgery(start_index=e.args[0]["start_index"],patient=number_string)
        return self.list_to_int(answer)

    def list_to_int(self,num_list):
        total = 0
        for number in num_list:
            total = total * 10 + number
        return total
                


def data_preprocessing():
    testcases=['index_start_from_1']
    with open(IN,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            n = f.readline().rstrip('\n')
            testcases.append(TESTCASE(original_number=n))
    return testcases


def model(*,testcase):
    answer = testcase.solve(testcase.original_number)
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
        