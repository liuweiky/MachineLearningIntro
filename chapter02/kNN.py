from numpy import *
import operator


def create_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]      # numpy函数，读取矩阵第0维长度
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
    return sorted_class_count[0][0]
