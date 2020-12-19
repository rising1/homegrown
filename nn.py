import numpy as np

class NN:

    def __init__(self,input_set,labels):

        print(np.shape(input_set))
        print(np.shape(labels))

        # Input layer is 3 points
        input_size = 3  # np.shape(input_set)[1]

        # We will build a hidden 2nd layer of 4 points
        hidden_size = 4

        # Output layer is 1 point
        output_size = 1 # np.shape(labels)[1]

        # we are going to pass 7 sets of values through the network
        # We will connect each point in one layer to every point in the next layer
        # So each point in the first layer connects to 4 points in the second layer
        # Each point in the second layer connects to 1 point in the output layer
        # Every connection will hold inside it a multiplier value which is called a weight
        # Every layer (but not the input layer) will have a value to add called a bias

        # Now to set up the neural network multipliers (weights) and constants (biases)
        self.input_set = input_set
        self.weights1 = np.random.rand(3,4)
        self.biases1 = np.random.rand(4,)
        self.weights2 = np.random.rand(4,1)
        self.biases2 = np.random.rand(1,)

        # Now multiply the input values by the weights and apply a signal strength test to each
        # this is called an activation. if it passes activation, the result is stored in the point
        # of the next layer. We will call the function feedforward to do this.



    def feedforward(self):
        # multiply by weights and add bias
        z1 = self.input_set.dot(self.weights1) + self.biases1
        a1 = np.maximum(0,z1) # this is the activation function
        z2 = a1.dot(self.weights2) + self.biases2
        a2 = np.maximum(0,z2)
        self.scores = a2
        print("scores= " , self.scores)

    def calc_error(self):
        self.error = np.subtract(self.scores,self.input_set)
        self.error = np.square(self.error)

    def back_prop(self):
        print("backprop tbd")

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

    mynn.feedforward()



