import numpy as np

class NN:

    def __init__(self,input_set,targets):

        print(np.shape(input_set))
        print(np.shape(targets))

        # Input layer is 3 points
        input_size = 3  # np.shape(input_set)[1]

        # We will build a hidden 2nd layer of 4 points
        # hidden_size = 4

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
        self.weights1 = np.random.rand(3,1)
        self.biases1 = np.random.rand(1,)
        self.targets = targets

        # Now multiply the input values by the weights and apply a signal strength test to each
        # this is called an activation. if it passes activation, the result is stored in the point
        # of the next layer. We will call the function feedforward to do this.



    def feedforward(self, batch):
        # multiply by weights and add bias
        self.z1 = batch.dot(self.weights1) + self.biases1
        self.a1 = np.maximum(0,self.z1) # this is the activation function
        print("activation value= ",self.a1)

    def calc_error(self,target):
        print("targets= ",target)
        self.error = (target - self.a1) **2
        self.error = np.mean(np.sqrt(self.error))
        print("Error= ", self.error)

    def back_prop(self,batch):
        # back propagation chain rule calculus
        learning_rate = 0.001
        gradientWeights = np.dot(batch.T,self.error)
        gradientBias = np.sum(self.error, axis=0, keepdims=True)
        self.weights1 = self.weights1 - learning_rate * gradientWeights
        self.biases1 = self.biases1  - learning_rate * gradientBias





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


    for i in range(11):
        for j in range(len(input_set)):
            mynn.feedforward(input_set[j])
            mynn.calc_error(labels[j])
            mynn.back_prop(input_set[j])




