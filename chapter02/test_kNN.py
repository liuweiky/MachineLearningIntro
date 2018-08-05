from chapter02.kNN import *
import matplotlib
import matplotlib.pyplot as plt

group, labels = create_data_set()

# print(chapter02.kNN.classify0([0, 0], group, labels, 3))

data_matrix, class_labels = file2matrix('datingTestSet2.txt')

# print(data_matrix, class_labels)
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(
#     data_matrix[:, 1],
#     data_matrix[:, 2],
#     15 * array(class_labels),
#     15 * array(class_labels))
# plt.show()

normed_data, ranges, min_vals = auto_norm(data_matrix)

print(normed_data)
print(ranges)
print(min_vals)
