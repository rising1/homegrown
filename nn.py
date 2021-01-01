class NN:

    def __init__(self):

        self.weights1 = [[0.5],[0.5],[0.5]]  #  np.random.rand(3, 1)
        # print("\n self.weights1= ", self.weights1)
        self.biases1 = [[0.5]]  #   np.random.rand(1,)
        # print("\n self.biases1= ",self.biases1,"\n")

    def feedforward(self, batch):
        # multiply by weights and add bias
        self.batch = [batch] #    np.reshape(batch,[1,3])
        self.inputWeights = self.dotOperation("multiply_elements",self.batch, self.weights1)
        # print("self.inputWeights= ",self.inputWeights)
        # print("input weights=", self.inputWeights)
        self.sumInputWeights = self.addVector(self.inputWeights)
        # print("sumInputWeights=",self.sumInputWeights,"  Bias=",self.biases1)
        self.z1 = self.dotOperation("add_elements",self.sumInputWeights,self.biases1)
        # self.z1 = np.dot(self.batch,self.weights1) + self.biases1
        # print(" feed forward z1= ",self.z1)
        self.a1 = max(0,self.z1[0][0]) # this is the activation function
        return self.a1

    def calc_error(self,target):
        self.error = (self.a1 - target[0])
        print("self.error= ",self.error)
        self.meanSquaredError = (self.error**2)

    def back_prop(self,batch,learning_rate):
        # back propagation chain rule calculus
        # self.dz1 = np.zeros_like(self.z1)
        self.dz1 = self.z1
        # self.printMatrixShape(self.z1)
        for i in range(len(self.z1)):
            for j in range(len(self.z1[0])):
                if(self.z1[i][j] > 0):
                    self.dz1[i][j] = 1
                else:
                    self.dz1[i][j] = 0
        # print("dz1= ",self.dz1)
        # self.dz1[self.z1 <= 0] = 0
        # self.dz1[self.z1 > 0] = 1
        self.batchT = self.reshape(batch)
        # print("batchT=",self.batchT)
        # print("error= ",self.error,"dz1= ",self.dz1)
        self.errorIncrement = [[self.error * self.dz1[0][0]]]
        # print("errorIncrement= ",self.errorIncrement)
        self.partgradWeights = self.dotOperation(
                        "multiply_elements", self.batchT, self.errorIncrement)
        # self.partgradWeights = self.addVector(self.partgradWeights)
        # print("partgradWeights= ", self.partgradWeights)
        self.gradientWeights = self.multiplyVector(2/len(self.batchT[1]), self.partgradWeights )
        # print("gradient weights= ",self.gradientWeights)
        # self.gradientWeights = 2 / self.batchT.shape[1] * np.dot(self.batchT, self.error * self.dz1)
        # print("self.error= ", self.error)
        self.gradientBias = self.error
        # self.gradientBias = np.sum(self.error, axis=0, keepdims=True)
        self.weights1Adj  = self.multiplyVector(- learning_rate , self.gradientWeights)
        # print("weightsAdj= ",self.weights1Adj)
        self.biases1Adj = - learning_rate * self.gradientBias
        # print("weights1= ",self.weights1," weightsAdj= ",self.weights1Adj)
        self.weights1 = self.dotOperation("add_elements",self.weights1, self.weights1Adj)
        self.biases1[0][0] = self.biases1[0][0] + self.biases1Adj

    #*********************************************************************
    #*********************Utility function for matrix operations**********
    #*********************************************************************

    def dotOperation(self,operation,matrix1,matrix2):
        # print("matrix1= ",matrix1)
        # print("matrix2= ",matrix2)
        a = len(matrix1)
        b = len(matrix1[0])
        c = len(matrix2)
        d = len(matrix2[0])
        if(a == d and b == c):
            matrix1 = self.reshape(matrix1)
        result = [[0 for col in range(d)] for row in range(c)]
        # print("a= ",a)
        for i in range(c):
            for j in range(d):
                # print("i=",i," j=",j)
                # print("multiplying ", matrix1[j][i], matrix2[i][j])
                if operation == "multiply_elements":
                    result[i][j] = matrix1[i][j] * matrix2[i][j]
                if operation == "add_elements":
                    # print("in add_elements")
                    result[i][j] = matrix1[i][j] + matrix2[i][j]
        # if operation == "add_elements":
        # print("matrix1= ",matrix1," matrix2= ",matrix2," result= ",result)
        # print("result= ",result)

        if( a > c and b == c ):
            result = [[0 for col in range(b)] for row in range(a)]
            # print("empty result= ",result)
            for i in range(a):
                for j in range(b):
                    if operation == "multiply_elements":
                        result[i][j] = matrix1[i][j] * matrix2[j][j]
            # print("matrix1= ", matrix1, " matrix2= ", matrix2, " result= ", result)
        return result

    def addVector(self,vector):
        # print("Vector input=",vector)
        sum = 0.0
        for w in range(len(vector)):
            for v in vector[w]:
                # print("Vector v= ",v)
                sum += v
                # print("Vector sum= ",sum)
        return[[sum]]

    def multiplyVector(self,scalar, vector):
        for v in vector:
            v[0] = v[0] * scalar
        # print("vector= ",vector," scalar= ",scalar,"multiplyVector result= ",vector)
        return vector

    def reshape(self,matrix):
        a = len(matrix)
        if(not isinstance(matrix[0],int) ):
            # print("type of matrix is ",type(matrix[0]))
            b = len(matrix[0])
            newMatrix = [[0 for col in range(a)] for row in range(b)]
            for i in range(a):
                for j in range(b):
                    newMatrix[j][i] = matrix[i][j]
        else:
            newMatrix = [[0] for col in range(a)]
            # print("newMatrix is ",newMatrix)
            for i in range(a):
                newMatrix[i][0] = matrix[i]
        return newMatrix



    def printMatrixShape(self,matrix1):
        print("matrix1 shape= (",len(matrix1),len(matrix1[0]),")")


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
                 [0, 0, 0]]  # Dependent variable

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
            mynn.back_prop(input_set[j],learning_rate)

            # track the error in the model
            if (i % (number_of_iterations/10) == 0):
                print("error= ",mynn.meanSquaredError)

    # see what the final weights values are and bias value
    print("\n final weights= ", mynn.weights1,"\n")
    print("final bias= ", mynn.biases1,"\n")

    # print("final error= ", mynn.meanSquaredError)
    print("test [1, 0, 1] should be 0 = ", mynn.feedforward([1, 0, 1]))
    print("test [0, 1, 1] should be 1 = ", mynn.feedforward([0, 1, 1]))

    # mynn.dotOperation("multiply_elements",input_set,labels)
