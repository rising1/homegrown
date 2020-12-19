import numpy as np

class NN:

    def __init__(self,input_set,labels):

        print(np.shape(input_set))
        print(np.shape(labels))

        # Input layer is 3 points
        input_size = 3

        # We will build a hidden 2nd layer of 4 points
        hidden_size = 4

        # Output layer is 1 point
        output_size = 1

        # we are going to pass 7 sets of values through the network
        # We will connect each point in one layer to every point in the next layer
        # So each point in the first layer connects to 4 points in the second layer
        # Each point in the second layer connects to 1 point in the output layer
        # Every connection will hold inside it a multiplier value which is called a weight






if __name__ == '__main__':

    input_set = np.array([[0, 1, 0],
                          [0, 0, 1],
                          [1, 0, 0],
                          [1, 1, 0],
                          [1, 1, 1],
                          [0, 1, 1],
                          [0, 1, 0]])  # Dependent variable

    labels = np.array([[1],
                       [0],
                       [0],
                       [1],
                       [1],
                       [0],
                       [1]])

    mynn = NN(input_set,labels)



