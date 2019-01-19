from math import log
import operator


def calc_shannon_ent(data_set):     # 获取香农熵
    num_entries = len(data_set)
    label_counts = {}
    for feat_vec in data_set:
        cur_label = feat_vec[-1]
        if cur_label not in label_counts.keys():
            label_counts[cur_label] = 0
        label_counts[cur_label] += 1
    shannon_ent = 0.0
    for key in label_counts:
        prob = float(label_counts[key] / num_entries)
        shannon_ent -= prob * log(prob, 2)
    return shannon_ent


# 按照axis分量为value抽取子集
def split_data_set(data_set, axis, value):
    ret_data = []
    for feat_vec in data_set:
        if feat_vec[axis] == value:
            reduced_feat_vec = feat_vec[:axis]
            # print(reduced_feat_vec)
            reduced_feat_vec.extend(feat_vec[axis + 1:])
            # print(reduced_feat_vec)
            ret_data.append(reduced_feat_vec)
    return ret_data


'''
data格式：
[d1, d2, ..., dn, label (Y/N)]
'''


# 选择可以使熵最低（数据混乱度最低）的划分特征
def choose_best_feature_to_split(data_set):
    feature_num = len(data_set[0]) - 1
    base_ent = calc_shannon_ent(data_set)   # 计算原熵
    best_info_gain = 0.0
    best_feature = -1
    for i in range(feature_num):
        # 取数据集内每个数据项的第i个特征，feat：feature
        feat_list = [example[i] for example in data_set]
        unique_vals = set(feat_list)    # 作为集合，去掉重复
        new_ent = 0.0   # 新熵
        # 求解用第 i 个特征划分时的熵
        for value in unique_vals:
            # 取出第 i 个特征为 value 的集合作为子集
            sub_data_set = split_data_set(data_set, i, value)
            # 计算该子集出现频率
            prob = len(sub_data_set) / float(len(data_set))
            # 求和
            new_ent += prob * calc_shannon_ent(sub_data_set)
        # 记录最优划分 i
        info_gain = base_ent - new_ent
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    return best_feature


# 返回出现频率最高的分类名称
def majority_cnt(class_list):
    class_count = {}
    for vote in class_list:
        if vote not in class_count.keys():
            class_count[vote] = 0
        class_count[vote] += 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def create_tree(data_set, labels):
    class_list = [example[-1] for example in data_set]
    # 当前数据集只有一类标签了，即，数据都是同一类的
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # 数据集被分得只剩标签项
    if len(data_set[0]) == 1:
        return majority_cnt(data_set)

    best_feat = choose_best_feature_to_split(data_set)
    best_feat_label = labels[best_feat]
    my_tree = {best_feat_label: {}}
    # 从标签中删除被选中作根节点的标签
    del(labels[best_feat])
    # 根据最优特征，将数据集分类递归构造决策树
    feat_values = [example[best_feat] for example in data_set]
    unique_values = set(feat_values)
    for value in unique_values:
        sub_labels = labels[:]
        my_tree[best_feat_label][value] = create_tree(split_data_set(data_set, best_feat, value), sub_labels)
    return my_tree
