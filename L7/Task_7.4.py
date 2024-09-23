def common_elements():
        set_a = set([v for v in range(100) if v %3 == 0])
        set_b = set([v for v in range(100) if v %5 == 0])
        common_set = set_a.intersection(set_b)
        print(common_set)
        return common_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')
