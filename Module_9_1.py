def apply_all_func(int_list, *functions):
    res_dict = {}
    for function in functions:
        res = function(int_list)
        res_dict.update({function.__name__: res})
    return res_dict

def min(_list):
    min_res = _list[0]
    for i in _list:
        if i<min_res:
            min_res = i
    return min_res

def max(_list):
    max_res = _list[0]
    for i in _list:
        if i>max_res:
            max_res = i
    return max_res

def len(_list):
    count = 0
    for i in _list:
        count += 1
    return count

def sum(_list):
    sum = 0
    for i in _list:
        sum += i
    return sum

def sorted(_list):
    for i in range(len(_list)):
        lowest = i
        for j in range(i + 1, len(_list)):
            if _list[j] < _list[lowest]:
                lowest = j
        _list[lowest], _list[i] = _list[i], _list[lowest]
    return _list


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))