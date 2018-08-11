from chapter02.kNN import *
import os


def img2vector(img_name):
    ret = zeros((1, 1024))
    file = open(img_name)
    for i in range(32):
        line = file.readline()
        for j in range(32):
            ret[0, 32 * i + j] = int(line[j])
    return ret


hw_labels = []
training_file_list = os.listdir('trainingDigits')
m = len(training_file_list)
training_matrix = zeros((m, 1024))

for i in range(m):
    filename = training_file_list[i]
    class_name = filename.split('_')[0]
    hw_labels.append(class_name)
    training_matrix[i, :] = img2vector('trainingDigits/%s' % filename)

test_file_list = os.listdir('testDigits')
err_count = 0.0
m_test = len(test_file_list)
for i in range(m_test):
    filename = test_file_list[i]
    class_name = filename.split('_')[0]
    vec = img2vector('testDigits/%s' % filename)
    recognition_result = classify0(vec, training_matrix, hw_labels, 3)
    print('digit: %s \t result: %s' % (class_name, recognition_result))
    if int(recognition_result) != int(class_name):
        err_count += 1.0

print('err rate: %f' % (err_count / float(m_test)))
