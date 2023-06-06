# Given two arguments, return an array which contains these two arguments.

def make_list(num_one, num_two):
    new_list = []
    new_list.append(num_one)
    new_list.append(num_two)
    return f"This is your new list {new_list}"

print(make_list(11, 24))