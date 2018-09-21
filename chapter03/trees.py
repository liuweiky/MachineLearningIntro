from math import log


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
