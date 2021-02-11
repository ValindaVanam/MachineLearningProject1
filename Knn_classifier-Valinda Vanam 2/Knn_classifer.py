# Your name :Valinda Vanam
# Your UCM ID : 700703487
# Certificate of Authenticity: “I certify that the codes/answers of this assignment are entirely my own work.”

import sys

# array to store the training dataset
x_train = []
y_train = []

# loading training files and save the content in two arrays
dataset = open(sys.argv[-2], 'r')
data = dataset.read().splitlines()
for d in data:
    int_data = list(map(int, d.split()))
    y_train.append(int_data.pop())
    x_train.append(int_data)

# array to store the testing dataset
x_test = []
y_test = []

dataset = open(sys.argv[-1], 'r')
data = dataset.read().splitlines()
for d in data:
    int_data = list(map(int, d.split()))
    y_test.append(int_data.pop())
    x_test.append(int_data)

print(f"The length of training dataset and testing dataset is {len(x_train)} and {len(x_test)}")

K = [1, 3, 5, 7, 9]  # different K values
optimal = 0
maxAccuracy = 0
for k in K:
    print(f'Process started for k : {k}')
    y_pred = []  # array to store prediction result
    for testData in x_test:
        temp = [[sum([abs(i - j) for i, j in zip(trainData, testData)]), i] for i, trainData in
                enumerate(x_train)]  # calculating nearest neighbours using L1 distance
        temp.sort()  # sorting the array based on the L1 score
        temp = temp[0:k]  # taking k neighbours only
        y_pred.append([y_train[x] for _, x in temp][0])  # appending the results to the prediction list

    print('Object ID  Predicted Class  True Class  Accuracy')  # printing the output headers
    cnt = 1
    total = 0
    for predClass, trueClass in zip(y_pred, y_test):  # iteration over the predicted results and original results
        result = 0
        if predClass == trueClass:  # calculating the result based on the comparison of prediction and actual
            result = 1
            total += 1
        print(cnt, " " * 10, predClass, " " * 14, trueClass, " " * 10, result)
        cnt += 1
    print()
    accuracy = total / len(y_test)  # calculating overall accuracy
    if accuracy > maxAccuracy:
        optimal = k
    print("Classification accuracy : %0.2f" % accuracy)

# finding te optimal K value based on the accuracy
print(f"The optimal K values is {optimal}")
