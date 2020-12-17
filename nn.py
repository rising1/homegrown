import numpy as np

class nn:
    def __init__(self,input_set,labels):
        self.labels = labels.reshape(7, 1)  # to convert labels to vector
        print(np.shape(self.labels))

if __name__ == '__main__':

    print("in main")
    input_set = np.array([[0, 1, 0],
                          [0, 0, 1],
                          [1, 0, 0],
                          [1, 1, 0],
                          [1, 1, 1],
                          [0, 1, 1],
                          [0, 1, 0]])  # Dependent variable

    labels = np.array([[1,
                        0,
                        0,
                        1,
                        1,
                        0,
                        1]])

    mynn = nn(input_set,labels)



