from numpy import *
import operator


def create_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]      # numpy函数，读取矩阵第0维长度（行数）
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set     # numpy函数tile，重复inX为dataSetSize*1
    sq_diff_mat = diff_mat**2
    sq_distances = sq_diff_mat.sum(axis=1)     # numpy函数，矩阵行求和
    distances = sq_distances**0.5
    sorted_dis = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dis[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    # print(class_count)
    # print(sorted_class_count)
    return sorted_class_count[0][0]


def file2matrix(filename):
    fr = open(filename)
    lines = fr.readlines()
    data_matrix = zeros((len(lines), 3))
    class_labels = []
    index = 0
    for l in lines:
        ls = l.strip().split('\t')
        # print(ls)
        data_matrix[index, :] = ls[0:3]
        class_labels.append(int(ls[-1]))
        index += 1
    return data_matrix, class_labels


# 特征值归一化
def auto_norm(data_set):
    min_vals = data_set.min(0)
    max_vals = data_set.max(0)
    # print(min_vals)
    ranges = max_vals - min_vals
    normed_data = zeros(shape(data_set))
    m = data_set.shape[0]
    # print(tile(min_vals, (m, 1)))
    normed_data = data_set - tile(min_vals, (m, 1))
    normed_data = normed_data / tile(ranges, (m, 1))
    return normed_data, ranges, min_vals
