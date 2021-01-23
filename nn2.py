import utilities as ut1
import ut

class NN2:

    def __init__(self):

        self.hidden  = [[0 for col in range(1)] for row in range(4)]
        self.final = [[0 for col in range(1)] for row in range(2)]
        self.weights1 = ut.buildMatrix(input_set[0],self.hidden,0.5)
        self.weights1adj = ut.buildMatrix(input_set[0],self.hidden,0)
        self.weights2 = ut.buildMatrix(self.hidden,self.final,0.5)
        self.weights2adj = ut.buildMatrix(self.hidden, self.final,0)
        self.biases1 = [[0.5 for col in range(1)] for row in range(4)]
        self.biases1adj = [[0.0 for col in range(1)] for row in range(4)]
        self.biases2 = [[0.5 for col in range(1)] for row in range(2)]
        self.biases2adj = [[0.0 for col in range(1)] for row in range(2)]
        # print("self.hidden= ",self.hidden)
        # print("biases1 = ",self.biases1)
        # print("self.final= ",self.final)
        # print("self.weights1= ",self.weights1)

    def feedforward(self, batch):

        # multiply a batch of inputs by weights and add bias. Then apply activation rule

        # put the batch into the right vector format
        self.batch = [batch]  # changes [0,0,1] to [[0,0,1]] - a (1,3) shape vector

        # multiply the inputs by the weightings
        self.sumInputsTimesWeights1 = ut.m("dot", self.batch, self.weights1)
        # print("inputBatch= ",self.batch," self.weights1= ",self.weights1)
        # print("inputsTimesWeights= ",self.inputsTimesWeights1)

        # self.sumInputsTimesWeights1 = ut.sumMatrix(self.inputsTimesWeights1)
        # print("sumInputsTimesWeights= ", self.sumInputsTimesWeights1)

        # add the result of the above inputs/weights sum above to the bias vector
        self.z1 = ut.m("add", self.sumInputsTimesWeights1, self.biases1)
        # print("z1= ",self.z1)

        # now put the result through the 'ReLu' activation function
        self.hidden = ut.Relu(self.z1)
        # print("hidden= ",self.hidden)

        self.sumInputsTimesWeights2 = ut.m("dot", ut.reshape(
                                                    self.hidden), self.weights2)
        # print("inputsTimesWeights2= ",self.inputsTimesWeights2)

        # self.sumInputsTimesWeights2 = ut.sumMatrix(self.inputsTimesWeights2)
        # print("sumInputsTimesWeights2= ", self.sumInputsTimesWeights2)

        self.z2 = ut.m("add", self.sumInputsTimesWeights2, self.biases2)
        self.a2 = ut.Relu(self.z2)

        # print("a2= ",self.a2)

        return self.a2

    def calc_error(self, labels):
        target = [labels]
        # calculate the difference between the value of the activation above
        # and the correct target result
        self.error = ut.m("minus", target, self.a2)
        # print("error= ",self.error)

        # calculate the mean squared error (only one value so the mean is the same)
        self.mse = ut.m("mse", self.error, self.error)
        # print("mse= ",self.mse)


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

        self.dz2 = self.z2
        # self.printMatrixShape(self.z1)
        for i in range(len(self.z2)):
            for j in range(len(self.z2[0])):
                if (self.z2[i][j] > 0):
                    self.dz2[i][j] = 1
                else:
                    self.dz2[i][j] = 0

        # print("dz1= ",self.dz1, " dz2= ", self.dz2)

        ####################################################################
        # calculate dE/dW2
        ####################################################################
        #    2 x 1                              2 x 1    2 x 1
        self.activatedGradient = ut.m("mult", self.dz2, self.error)
        # print("activatedGradient= ", self.activatedGradient)
        #  4 x 2         =                  4 x 1       1 x 2
        self.weights2adj = ut.m("mult", self.hidden, ut.reshape(self.activatedGradient))
        # multiply the weights adj by the learning rate
        self.weights2adj = ut.times(learning_rate, 1, self.weights2adj)
        # print("weights2adj= ", self.weights2adj)


        ####################################################################
        # calculate dE/dB2
        ####################################################################

        self.biases2adj = ut.times(learning_rate, 1, self.activatedGradient)

        ####################################################################
        # calculate dE/dW1
        ####################################################################
        #    2 x 1                              2 x 1    2 x 1
        self.activatedGradient = ut.m("mult", self.dz2, self.error)
        self.weights1partadj = ut.m("mult", ut.reshape(self.activatedGradient),
                                                ut.reshape(self.weights2))
        self.weights1adj = ut.m("mult", ut.reshape(batch), self.weights1partadj)
        self.weights1adj = ut.times(learning_rate, 1, self.weights1adj)
        # print("weights1adj= ", self.weights1adj)

        ####################################################################
        # calculate dE/dB1
        ####################################################################

        self.biases1adj = ut.times(learning_rate, 1, self.weights1partadj)

        # subtract the adjusted weights
        self.weights2 = ut.m("minus", self.weights2adj, self.weights2)
        self.weights1 = ut.m("minus", self.weights1adj, self.weights1)
        # print("weights2= ", self.weights2)
        self.biases2 = ut.m("minus", self.biases2adj, self.biases2)
        self.biases1 = ut.m("minus", self.biases1adj, self.biases1)
        # print("biases2= ", self.biases2)

if __name__ == '__main__':

    #input_set = [[0, 1, 1]]
    #labels = [[1, 0]]

    input_set = [[0, 1, 0],
                 [0, 0, 1],
                 [1, 0, 0],
                 [1, 1, 0],
                 [1, 1, 1],
                 [0, 0, 0]]

    labels = [[1,0],
              [0,0],
              [0,0],
              [1,0],
              [1,0],
              [0,0]]

    mynn = NN2()

    # Parameters learning rate and number of iterations in which to learn
    learning_rate = .01  # **** this is the learning rate factor
    number_of_iterations = 10000
    start_time = ut.getTime()
    for i in range(number_of_iterations):
        for j in range(len(input_set)):
            # print("input set[j] = ", input_set[j], "  labels[j]= ",labels[j])
            mynn.feedforward(input_set[j])
            mynn.calc_error(labels[j])
            mynn.back_prop(input_set[j], learning_rate)

            # track the error in the model
            if (i % (number_of_iterations / 10) == 0):
                print("mse= ", mynn.mse)
    end_time = ut.getTime()
    print("\n--- %s seconds ---" % (end_time - start_time))
    # see what the final weights values are and bias value
    print("\n final weights1= ", mynn.weights1, "\n")
    print("\n final weights=2 ", mynn.weights2, "\n")
    print("final bias1= ", mynn.biases1, "\n")
    print("final bias2= ", mynn.biases2, "\n")
    print("test [1, 0, 1] should be 0 = ", mynn.feedforward([1, 0, 1]))
    print("test [0, 1, 1] should be 1 = ", mynn.feedforward([0, 1, 1]))

