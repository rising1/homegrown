import numpy as np


class nn:
    def __init__(self,input_set,labels):
        self.labels = self.labels.reshape(7, 1)  # to convert labels to vector
        print("done")





if __name__ == '__Main__':
    # Independent variables
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
    mynn = nn()


