from chapter03.trees import *

data_set = [
    [1, 1, 'yes'],
    [1, 1, 'yes'],
    [1, 0, 'no'],
    [0, 1, 'no'],
    [0, 1, 'no']]
#
# labels = ['no surfing', 'flippers']
#
# print(calc_shannon_ent(data_set))

print(split_data_set(data_set, 0, 1))