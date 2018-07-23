import chapter02.kNN

group, labels = chapter02.kNN.create_data_set()

print(chapter02.kNN.classify0([0, 0], group, labels, 3))