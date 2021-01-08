import utilities as ut

class NN2:

    def __init__(self):

        self.hidden  = [[0 for col in range(1)] for row in range(4)]
        self.final = [[0 for col in range(1)] for row in range(2)]
        self.weights1 = ut.buildMatrix(input_set[0],self.hidden)
        self.weights2 = ut.buildMatrix(self.hidden,self.final)
        self.biases1 = [[0.5 for col in range(1)] for row in range(4)]
        self.biases2 = [[0.5 for col in range(1)] for row in range(2)]
        # print("self.hidden= ",self.hidden)
        # print("biases1 = ",self.biases1)
        # print("self.final= ",self.final)
        # print("self.weights1= ",self.weights1)

    def feedforward(self, batch):

        # multiply a batch of inputs by weights and add bias. Then apply activation rule

        # put the batch into the right vector format
        self.batch = [batch]  # changes [0,0,1] to [[0,0,1]] - a (1,3) shape vector

        # multiply the inputs by the weightings
        self.inputsTimesWeights1 = ut.dotOperation("multiply_elements", self.batch, self.weights1)
        # print("inputBatch= ",self.batch," self.weights1= ",self.weights1)
        # print("inputsTimesWeights= ",self.inputsTimesWeights1)

        self.sumInputsTimesWeights1 = ut.sumMatrix(self.inputsTimesWeights1)
        # print("sumInputsTimesWeights= ", self.sumInputsTimesWeights1)

        # add the result of the above inputs/weights sum above to the bias vector
        self.z1 = ut.dotOperation("add_elements", self.sumInputsTimesWeights1, self.biases1)
        # print("z1= ",self.z1)

        # now put the result through the 'ReLu' activation function
        self.hidden = ut.Relu(self.z1)
        # print("hidden= ",self.hidden)

        self.inputsTimesWeights2 = ut.dotOperation("multiply_elements", ut.reshape(self.hidden), self.weights2)
        print("inputsTimesWeights2= ",self.inputsTimesWeights2)

        self.sumInputsTimesWeights2 = ut.sumMatrix(self.inputsTimesWeights2)
        print("sumInputsTimesWeights2= ", self.sumInputsTimesWeights2)

        self.z2 = ut.dotOperation("add_elements", self.sumInputsTimesWeights2, self.biases2)
        self.a2 = ut.Relu(self.z2)

        print("a2= ",self.a2)

        return self.a2

    def calc_error(self, target):

        # calculate the difference between the value of the activation above
        # and the correct target result
        self.error = ut.dotOperation("subtract_elements", self.a2, target)

        # calculate the mean squared error (only one value so the mean is the same)
        self.meanSquaredError = ut.addVector(ut.dotOperation(
                            "multiply_elements", self.error, self.error))
        print("mean squared error= ",self.meanSquaredError)

    def back_prop(self, batch, learning_rate):

        # Prepare gradients of Z  dz/dw d( Batch * Weights + bias)/dw
        self.dz1 = self.z1
        # self.printMatrixShape(self.z1)
        for i in range(len(self.z1)):
            for j in range(len(self.z1[0])):
                if (self.z1[i][j] > 0):
                    self.dz1[i][j] = 1
                else:
                    self.dz1[i][j] = 0

        # Transpose the input batch
        self.batchT = ut.reshape(batch)

        if self.z1[0][0] > 0:

            # dMSE/dZ1 = gradient of error with respect to Z1 ( Batch * Weights + bias)
            self.errorIncrement = [[2 * self.error * self.dz1[0][0]]]

            # dMSE/dZ1 * dZ1/dW - split into two lines for clarity
            self.partgradWeights = ut.dotOperation(
                "multiply_elements", self.batchT, self.errorIncrement)
            self.gradientWeights = ut.multiplyVector(1 / len(self.batchT[1]), self.partgradWeights)

            # dMSE/dB = gradient of error with respect to bias
            self.gradientBias = 2 * self.error

        else:

            self.gradientBias = 0
            self.gradientWeights = 0

        # Calculate the weights and bias adjustment
        self.weights1Adj = ut.multiplyVector(- learning_rate, self.gradientWeights)
        self.biases1Adj = - learning_rate * self.gradientBias

        # Add the adjustements to the weights and the bias
        self.weights1 = ut.dotOperation("add_elements", self.weights1, self.weights1Adj)
        self.biases1[0][0] = self.biases1[0][0] + self.biases1Adj


if __name__ == '__main__':

    input_set = [[0, 1, 1]]
    labels = [[1,0]]

    # input_set = [[0, 1, 0],
    #             [0, 0, 1],
    #             [1, 0, 0],
    #             [1, 1, 0],
    #             [1, 1, 1],
    #             [0, 0, 0]]

    #labels = [[1],
    #          [0],
    #          [0],
    #          [1],
    #          [1],
    #          [0]]

    mynn = NN2()

    # Parameters learning rate and number of iterations in which to learn
    learning_rate = .01  # **** this is the learning rate factor
    number_of_iterations = 1

    for i in range(number_of_iterations):
        for j in range(len(input_set)):
            mynn.feedforward(input_set[j])
            mynn.calc_error(labels[j])
            mynn.back_prop(input_set[j], learning_rate)

            # track the error in the model
            if (i % (number_of_iterations / 10) == 0):
                print("error= ", mynn.meanSquaredError)

    # see what the final weights values are and bias value
    print("\n final weights= ", mynn.weights1, "\n")
    print("final bias= ", mynn.biases1, "\n")

    print("test [1, 0, 1] should be 0 = ", mynn.feedforward([1, 0, 1]))
    print("test [0, 1, 1] should be 1 = ", mynn.feedforward([0, 1, 1]))

