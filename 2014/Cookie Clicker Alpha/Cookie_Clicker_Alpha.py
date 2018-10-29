'''
Cookie Clicker is a Javascript game by Orteil, where players click on a picture of a giant cookie. 
Clicking on the giant cookie gives them cookies. They can spend those cookies to buy buildings. 
Those buildings help them get even more cookies. Like this problem, the game is very cookie-focused. 
This problem has a similar idea, but it does not assume you have played Cookie Clicker. 
Please don't go play it now: it might be a long time before you come back.
In this problem, you start with 0 cookies. You gain cookies at a rate of 2 cookies per second, 
by clicking on a giant cookie. Any time you have at least C cookies, you can buy a cookie farm. 
Every time you buy a cookie farm, it costs you C cookies and gives you an extra F cookies per second.
Once you have X cookies that you haven't spent on farms, you win! 
Figure out how long it will take you to win if you use the best possible strategy.
계산 시간 단축 필요
'''
TEST = 'small-practice'
IN = 'B-{}.in'.format(TEST)
OUT = 'B-{}.out'.format(TEST)


from collections import namedtuple


class TESTCASE():
    def __init__(self,cost_of_farm, cookie_per_time, goal_cookies):
        self.cost_of_farm = float(cost_of_farm)
        self.cookie_per_time = float(cookie_per_time)
        self.goal_cookies = float(goal_cookies)

    def __repr__(self):
        fmt_string=""
        return fmt_string.format()
    
    def simulate(self,num_of_farms):
        spent_time = 0.0
        for n_th in range(num_of_farms):
            spent_time += self.cost_of_farm/(2 + self.cookie_per_time * n_th)
        spent_time += self.goal_cookies/(2+self.cookie_per_time * num_of_farms)
        return 1/spent_time
    def solve(self):
        max_num_of_farms = int(self.goal_cookies/self.cost_of_farm)
        max_inverse_of_time = 0
        suspect = 0
        for num_of_farms in range(max_num_of_farms + 1):
            suspect = self.simulate(num_of_farms)
            if suspect > max_inverse_of_time :
                max_inverse_of_time = suspect
            else:
                return 1/max_inverse_of_time
        return 1/max_inverse_of_time


def data_preprocessing():
    testcases=['index_start_from_1']
    with open(IN,'r') as f:
        num_of_testcase=int(f.readline())
        for n_th_testcase in range(1,num_of_testcase+1):
            cost_of_farm, cookie_per_time, goal_cookies = f.readline().rstrip('\n').split(" ")
            testcases.append(TESTCASE(cost_of_farm, cookie_per_time, goal_cookies))
    return testcases


def model(*,testcase):
    answer = testcase.solve()
    return answer


    
def controller_view(*,testcases):
    fmt_string="Case #{0}: {1:.7f}\n"
    with open(OUT,'w') as f:
        for n_th, n_th_testcase in enumerate(testcases[1:],1):
            f.write(fmt_string.format(n_th,model(testcase=n_th_testcase)))    


def main():
        testcases=data_preprocessing()
        controller_view(testcases=testcases)


if __name__=="__main__":
    main()
        