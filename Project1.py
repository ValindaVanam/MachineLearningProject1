# Your name : Valinda Vanam
# Your UCM ID : 700703487
# Certificate of Authenticity: “I certify that the codes/answers of this assignment are entirely my own work.”

import sys
from collections import Counter
from math import sqrt

# command line arguments for the datasets
testingFile = sys.argv[-1]
trainingFile = sys.argv[-2]


# loading dataset files
def fileHandler(fileName):
    inputs = list()  # list for storing input data features
    outputs = list()  # list for storing output data features

    with open(fileName) as content:
        for text in content:
            temp = text.strip('\r\n').split()
            inputs.append(list(map(int, temp[:-1])))
            outputs.append(float(temp[-1]))
    return inputs, outputs


xTrain, yTrain = fileHandler(trainingFile)
xTest, yTest = fileHandler(testingFile)


class KNN:
    def __init__(self, k):
        self.k = k

    def fit(self, x, y):
        self.xTrain = x
        self.yTrain = y

    def L1Distance(self, x1, x2):
        return sum(abs(i - j) for i, j in zip(x1, x2))

    def predict(self, xTest):
        yPredicted = list()
        for testData in xTest:
            temp = list()
            neighbors = list()
            for trainData in self.xTrain:
                distance = self.L1Distance(trainData, testData)
                temp.append([distance, trainData])
            temp.sort(key=lambda i: i[0])
            temp = temp[0:self.k]
            for _, x in temp:
                neighbors.append(self.yTrain[self.xTrain.index(x)])
            yPredicted.append(Counter(neighbors).most_common(1)[0][0])
        return yPredicted


for k in [1, 3, 5, 7, 9]:
    knn = KNN(k)
    knn.fit(xTrain, yTrain)
    prediction = knn.predict(xTest)
    print('Object ID\t predicted class\t true class\t\t  accuracy')
    for i, j in enumerate(zip(prediction, yTest)):
        pred, y = j
        result = 1 if pred == y else 0
        print(i, pred, y, result, sep='\t\t\t')
    print("\nOptimal Value for k:{} is {:.2f}".format(k,
                                                                        sum([1 if i == j else 0 for i, j in
                                                                             zip(prediction, yTest)]) / len(yTest)))

# Optimal K
print("The optimal K from the list of K-numbers for K-NN are 1 and 3")
