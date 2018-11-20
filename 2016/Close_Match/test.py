from collections import defaultdict
def test_defaultdict():
    test_dict = defaultdict(list)
    print(test_dict[0])


def test_is_digit(test_char):
    print(test_char.isdigit())


def test_is_int(test_char):
    try:
        int(test_char)
    except ValueError:
        return False
    else:
        return True


def test_list_append():
    test_list = []
    a = '1'
    b = '?'
    test_list.append([a,b])
    print(test_list)

def test_string_index():
    test_string = "1?3"
    print(test_string[1])


def test_replace():
    test_string = "1?3"
    print(test_string.replace('?','0'))


def test_same():
    a = '1'
    b = '1'
    print(a == b)


def test_string_int():
    a = list("123")
    b = "5"
    a[0] = str(int(b) + 1)
    print(a)


def test_pretty_print_dict():
    possible_case_tree = defaultdict(list)
    decision = bytearray('1??','utf-8')
    possible_case_tree[0] = decision
    #print(possible_case_tree[0].decode('utf-8'))
    for index,current_decision in possible_case_tree.items():
        print(current_decision)
        #print(current_decision.decode('utf-8'))

if __name__ == "__main__":
    test_pretty_print_dict()