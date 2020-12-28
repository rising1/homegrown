import numpy as np

class NN:

    def __init__(self,input_set,targets):

        #print(np.shape(input_set))
        #print(np.shape(targets))

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
        print("self.weights1= ",self.weights1)
        self.biases1 = np.random.rand(1,)
        print("self.biases1= ",self.biases1)
        self.targets = targets

        # Now multiply the input values by the weights and apply a signal strength test to each
        # this is called an activation. if it passes activation, the result is stored in the point
        # of the next layer. We will call the function feedforward to do this.



    def feedforward(self, batch):
        # multiply by weights and add bias
        self.batch = np.reshape(batch,[1,3])
        self.z1 = self.weights1.dot(self.batch) + self.biases1
        self.dz1 = np.zeros_like(self.z1)
        self.dz1[self.z1 <= 0] = 0
        self.dz1[self.z1 > 0] = 1
        # print(self.dz1)
        self.a1 = np.maximum(0,self.z1) # this is the activation function # **** This is working as expected


    def calc_error(self,target):
        # print("targets= ",target)
        # print("z1 shape= ", np.shape(self.z1))
        # print("target shape= ", np.shape(target))
        self.error = (self.a1 - target)
        # print("raw error shape= ",np.shape(self.error))
        self.meanSquaredError = np.mean(self.error**2)    # ************ This looks fine - mean squared error



    def back_prop(self,batch):
        # back propagation chain rule calculus
        learning_rate = 0.0001
        self.batchT = np.reshape(batch,[3,1])
        self.gradientWeights = 2/self.batchT.shape[1] * np.dot(self.meanSquaredError * self.dz1, self.batchT)
        self.gradientBias = np.sum(self.error, axis=0, keepdims=True)
        self.weights1Adj  =  learning_rate * self.gradientWeights
        self.biases1Adj =  learning_rate * self.gradientBias
        self.weights1 = self.weights1 + self.weights1Adj
        self.biases1 = self.biases1 + self.biases1Adj





if __name__ == '__main__':

    input_set = np.array([[0, 1, 0]])

    labels = np.array([[1]])

    #input_set = np.array([[0, 1, 0],
    #                      [0, 0, 1],
    #                      [1, 0, 0],
    #                      [1, 1, 0],
    #                      [1, 1, 1],
    #                      [0, 1, 1],
    #                      [0, 1, 0]])  # Dependent variable

    #labels = np.array([[1],
    #                   [0],
    #                   [0],
    #                   [1],
    #                   [1],
    #                   [0],
    #                   [1]])

    mynn = NN(input_set,labels)


    for i in range(1000):
        for j in range(len(input_set)):
            mynn.feedforward(input_set[j])
            mynn.calc_error(labels[j])
            mynn.back_prop(input_set[j])
            #if (i == 1):
            if (i % 100 == 0):
                # print("Input batch shape= ", np.shape(mynn.batch))
                # print("batch= ",mynn.batch)
                print("feed forward value= ",mynn.z1)
                # print("error= ",mynn.error)
                # print("error shape= ",np.shape(mynn.error))
                # print("Input batch transposed shape= ",np.shape(mynn.batch))
                # print("transposed batch= ", mynn.batchT)
                # print ("gradient weights shape = ",np.shape(mynn.gradientWeights))
                # print("Gradient weights=",mynn.gradientWeights)
                # print("activation= ",mynn.a1)
                # print("weights1= ",mynn.weights1)
                # print("Weights shape= ",np.shape(mynn.weights1))
                # print("weightsAdj= ",mynn.weights1Adj)


    print("final weights= ",mynn.weights1)
    print("final bias= ",mynn.biases1)
    print("final error= ",mynn.error)


