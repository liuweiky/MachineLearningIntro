import matplotlib.pyplot as plt

# 定义文本框和箭头样式
decision_node = dict(boxstyle='sawtooth', fc='0.8')
leaf_node = dict(boxstyle='round4', fc='0.8')
arrow_args = dict(arrowstyle='<-')


def plot_node(node_text, centre_pt, parent_pt, node_type):
    create_plot.ax1.annotate(node_text,
                             xy=parent_pt,
                             xycoords='axes fraction',
                             xytext=centre_pt,
                             textcoords='axes fraction',
                             va='center',
                             ha='center',
                             bbox=node_type,
                             arrowprops=arrow_args)


def create_plot(in_tree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    ax_props = dict(xticks=[], yticks=[])
    create_plot.ax1 = plt.subplot(111, frameon=False, **ax_props)
    plot_tree.total_w = float(get_leaf_num(in_tree))
    plot_tree.total_d = float(get_tree_depth(in_tree))
    plot_tree.x_off = -0.5 / plot_tree.total_w
    plot_tree.y_off = 1.0
    plot_tree(in_tree, (0.5, 1.0), '')
    plt.show()


# 获取树的叶结点数
def get_leaf_num(my_tree):
    leaf_num = 0
    sub_tree = my_tree[list(my_tree.keys())[0]]
    for key in sub_tree.keys():
        if type(sub_tree[key]).__name__ == 'dict':
            leaf_num += get_leaf_num(sub_tree[key])
        else:
            leaf_num += 1
    return leaf_num


# 获取树的最大深度
def get_tree_depth(my_tree):
    max_depth = 0
    sub_tree = my_tree[list(my_tree.keys())[0]]
    for key in sub_tree.keys():
        if type(sub_tree[key]).__name__ == 'dict':
            cur_depth = get_tree_depth(sub_tree[key]) + 1
        else:
            cur_depth = 1
        max_depth = max(cur_depth, max_depth)
    return max_depth


def retrieve_tree(i):
    list_of_tree = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                    {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}},
                    ]
    return list_of_tree[i]


def plot_parent_child_info(child, parent, txt):
    x_mid = (parent[0] - child[0]) / 2.0 + child[0]
    y_mid = (parent[1] - child[1]) / 2.0 + child[1]
    create_plot.ax1.text(x_mid, y_mid, txt)


def plot_tree(my_tree, parent, node_txt):
    leaf_num = get_leaf_num(my_tree)
    depth = get_tree_depth(my_tree)
    dict_key = list(my_tree.keys())[0]
    cur_pt = (plot_tree.x_off + (1.0 + float(leaf_num)) / 2.0 / plot_tree.total_w, plot_tree.y_off)
    plot_parent_child_info(cur_pt, parent, node_txt)
    plot_node(dict_key, cur_pt, parent, decision_node)
    sub_tree = my_tree[dict_key]
    plot_tree.y_off = plot_tree.y_off - 1.0 / plot_tree.total_d
    for key in sub_tree.keys():
        if type(sub_tree[key]).__name__ == 'dict':
            plot_tree(sub_tree[key], cur_pt, str(key))
        else:
            plot_tree.x_off = plot_tree.x_off + 1.0 / plot_tree.total_w
            plot_node(sub_tree[key], (plot_tree.x_off, plot_tree.y_off), cur_pt, leaf_node)
            plot_parent_child_info((plot_tree.x_off, plot_tree.y_off), cur_pt, str(key))
    plot_tree.y_off = plot_tree.y_off + 1.0 / plot_tree.total_d

