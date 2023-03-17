def sum_one(parameter):
    return parameter * 2


age = [15, 65, 34, 78, 23]
new_age = [sum_one(n_age) for n_age in age if n_age > 30]
print(new_age)


# If we need create a new list for iteration, we have to do:

def new_list(list=None):
    if not list:
        list = []
    print(len(list))
    print(list)
    list.append(12)
    print(list)


new_list()
new_list()
new_list()
