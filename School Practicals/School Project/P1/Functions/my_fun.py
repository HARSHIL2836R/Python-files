class number:
    class digit:
        def get_sum(self, num):
            _sum_ = 0 
            for _dig_ in str(num):
                _sum_ += int(_dig_)
            return _sum_

class my_list:
    def int_list_to_str(self, l):
        sl = map(str, l)
        return ', '.join(sl)
    
    class var:
        #CREATING THREE LISTS

        #Serial Number
        sr = []
        #Creating list of Fibonacci Numbers till 1000 
        li = [0, 1, 1]
        #Creating list of digital root
        lis = [0, 1, 1]

class dic:
    def print_some_keys(self, d):
        for x in d.keys():
            if x <= 25:
                print('\t', x, ':', d.get(x), end=',\n')

    class var:
        #splitting list for getting numbers between consecutive 9's 
        splitted = [] #LIST
        #number of iterations
        count = 0
        # positions of 9
        occ = (0, ) #TUPLE

        # list of sum of digital roots between consecutive 9's
        sUm = []