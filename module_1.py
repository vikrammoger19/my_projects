# a module is a file consisting python code. It can define functions, variable and also classes.
def is_even(l):
    even_list = []
    odd_list = []

    for i in l:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list


