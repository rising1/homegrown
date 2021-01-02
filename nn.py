class NN:

    def __init__(self):

        self.weights1 = [[0.5],[0.5],[0.5]]
        self.biases1 = [[0.5]]

    def feedforward(self, batch):

        # multiply a batch of inputs by weights and add bias. Then apply activation rule

        # put the batch into the right vector format
        self.batch = [batch] # changes [0,0,1] to [[0,0,1]] - a (1,3) shape vector

        # multiply the inputs by the weightings
        self.inputWeights = self.dotOperation("multiply_elements",self.batch, self.weights1)

        # add the contents of the above vector together - makes a (1,1) vector
        self.sumInputWeights = self.addVector(self.inputWeights)

        # add the result of the above inputs/weights sum above to the bias vector
        self.z1 = self.dotOperation("add_elements",self.sumInputWeights,self.biases1)

        # now put the result through the 'ReLu' activation function
        self.a1 = max(0,self.z1[0][0])

        return self.a1

    def calc_error(self,target):

        # calculate the difference between the value of the activation above
        # and the correct target result
        self.error = (self.a1 - target[0])

        # calculate the mean squared error (only one value so the mean is the same)
        self.meanSquaredError = (self.error**2)

    def back_prop(self,batch,learning_rate):

        # Prepare gradients of Z  dz/dw d( Batch * Weights + bias)/dw
        self.dz1 = self.z1
        # self.printMatrixShape(self.z1)
        for i in range(len(self.z1)):
            for j in range(len(self.z1[0])):
                if(self.z1[i][j] > 0):
                    self.dz1[i][j] = 1
                else:
                    self.dz1[i][j] = 0

        # Transpose the input batch
        self.batchT = self.reshape(batch)

        if self.z1[0][0] > 0:

            # dMSE/dZ1 = gradient of error with respect to Z1 ( Batch * Weights + bias)
            self.errorIncrement = [[2 * self.error * self.dz1[0][0]]]

            # dMSE/dZ1 * dZ1/dW - split into two lines for clarity
            self.partgradWeights = self.dotOperation(
                        "multiply_elements", self.batchT, self.errorIncrement)
            self.gradientWeights = self.multiplyVector(1/len(self.batchT[1]), self.partgradWeights )

            # dMSE/dB = gradient of error with respect to bias
            self.gradientBias = 2 * self.error

        else:

            self.gradientBias = 0
            self.gradientWeights = 0

        # Calculate the weights and bias adjustment
        self.weights1Adj  = self.multiplyVector(- learning_rate, self.gradientWeights)
        self.biases1Adj = - learning_rate * self.gradientBias

        # Add the adjustements to the weights and the bias
        self.weights1 = self.dotOperation("add_elements",self.weights1, self.weights1Adj)
        self.biases1[0][0] = self.biases1[0][0] + self.biases1Adj



    #*********************************************************************
    #*********************Utility function for matrix operations**********
    #*********************************************************************

    def dotOperation(self,operation,matrix1,matrix2):

        a = len(matrix1)
        b = len(matrix1[0])
        c = len(matrix2)
        d = len(matrix2[0])

        if(a == d and b == c):
            matrix1 = self.reshape(matrix1)
        result = [[0 for col in range(d)] for row in range(c)]
        for i in range(c):
            for j in range(d):
                if operation == "multiply_elements":
                    result[i][j] = matrix1[i][j] * matrix2[i][j]
                if operation == "add_elements":
                    result[i][j] = matrix1[i][j] + matrix2[i][j]

        if( a > c and b == c ):
            result = [[0 for col in range(b)] for row in range(a)]
            for i in range(a):
                for j in range(b):
                    if operation == "multiply_elements":
                        result[i][j] = matrix1[i][j] * matrix2[j][j]
        return result

    def addVector(self, vector):
        sum = 0.0
        for w in range(len(vector)):
            for v in vector[w]:
                sum += v
        return[[sum]]

    def multiplyVector(self, scalar, vector):
        for v in vector:
            v[0] = v[0] * scalar
        return vector

    def reshape(self, matrix):
        a = len(matrix)
        if(not isinstance(matrix[0],int) ):
            b = len(matrix[0])
            newMatrix = [[0 for col in range(a)] for row in range(b)]
            for i in range(a):
                for j in range(b):
                    newMatrix[j][i] = matrix[i][j]
        else:
            newMatrix = [[0] for col in range(a)]
            for i in range(a):
                newMatrix[i][0] = matrix[i]
        return newMatrix

    def printMatrixShape(self, matrix1):
        print("matrix1 shape= (", len(matrix1), len(matrix1[0]), ")")


    # **************************************************************
    # *************** End of utility functions *********************
    # **************************************************************

if __name__ == '__main__':

    # input_set = [[0, 0, 1]]
    # labels = [[0]]

    input_set = [[0, 1, 0],
                 [0, 0, 1],
                 [1, 0, 0],
                 [1, 1, 0],
                 [1, 1, 1],
                 [0, 0, 0]]

    labels = [[1],
              [0],
              [0],
              [1],
              [1],
              [0]]

    mynn = NN()

    # Parameters learning rate and number of iterations in which to learn
    learning_rate = .01 # **** this is the learning rate factor
    number_of_iterations = 200

    for i in range(number_of_iterations):
        for j in range(len(input_set)):
            mynn.feedforward(input_set[j])
            mynn.calc_error(labels[j])
            mynn.back_prop(input_set[j], learning_rate)

            # track the error in the model
            if (i % (number_of_iterations/10) == 0):
                print("error= ", mynn.meanSquaredError)

    # see what the final weights values are and bias value
    print("\n final weights= ", mynn.weights1, "\n")
    print("final bias= ", mynn.biases1, "\n")

    print("test [1, 0, 1] should be 0 = ", mynn.feedforward([1, 0, 1]))
    print("test [0, 1, 1] should be 1 = ", mynn.feedforward([0, 1, 1]))

