import numpy as np

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
        self.sumInputWeights = self.addVector(self.inputWeights)
        self.z1 = self.dotOperation("add_elements",self.sumInputWeights,self.biases1)
        # self.z1 = np.dot(self.batch,self.weights1) + self.biases1
        print("z1= ",self.z1)
        self.a1 = np.maximum(0,self.z1) # this is the activation function
        return self.a1

    def calc_error(self,target):
        self.error = (self.a1 - target)
        self.meanSquaredError = np.mean(self.error**2)

    def back_prop(self,batch,learning_rate):
        # back propagation chain rule calculus
        # self.dz1 = np.zeros_like(self.z1)
        self.dz1 = self.z1
        self.printMatrixShape(self.z1)
        for i in range(len(self.z1)):
            for j in range(len(self.z1[0])):
                self.dz1[i][j] = 0
        print("dz1= ",self.dz1)
        # self.dz1[self.z1 <= 0] = 0
        # self.dz1[self.z1 > 0] = 1
        self.batchT = np.reshape(batch,[3,1])
        # self.gradientWeights = 2/self.batchT.shape[1] * self.dotOperation("add_elements", self.batchT,self.error * self.dz1)
        self.gradientWeights = 2 / self.batchT.shape[1] * np.dot(self.batchT, self.error * self.dz1)
        self.gradientBias = np.sum(self.error, axis=0, keepdims=True)
        self.weights1Adj  = - learning_rate * self.gradientWeights
        self.biases1Adj = - learning_rate * self.gradientBias
        self.weights1 = self.weights1 + self.weights1Adj
        self.biases1 = self.biases1 + self.biases1Adj

    #*********************************************************************
    #*********************Utility function for matrix operations**********
    #*********************************************************************

    def dotOperation(self,operation,matrix1,matrix2):
        a = len(matrix1)
        b = len(matrix1[0])
        c = len(matrix2)
        d = len(matrix2[0])
        # if(a != c or b != d):
            # print("\n","error - matrices should be same shape")
            # print(" matrix 1= (",a,b,") matrix 2= (",c,d,")")
        result = [[None for col in range(a)] for row in range(b)]
        # print(result)
        # print("a= ",a)
        if(c>0):
            for i in range(c):
                # for j in range(d):
                    # print("j=",j," i=",i)
                    # print("multiplying ", matrix1[j][i], matrix2[i][j])
                if operation == "multiply_elements":
                    result[i][j] = matrix1[j][i] * matrix2[i][j]
                if operation == "add_elements":
                    result[i][j] = matrix1[j][i] + matrix2[i][j]
        return result

    def addVector(self,vector):
        sum = 0.0
        for v in vector[0]:
            # print("Vector v= ",v)
            sum += v
        # print("Vector sum= ",sum)
        return[[sum]]

    def printMatrixShape(self,matrix1):
        print("matrix1 shape= (",len(matrix1),len(matrix1[0]),")")


    # **************************************************************
    # *************** End of utility functions *********************
    # **************************************************************

if __name__ == '__main__':

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
    number_of_iterations = 1

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
    print("test [1, 0, 1] should be 0 = ", mynn.feedforward([[1, 0, 1]]))
    print("test [0, 1, 1] should be 1 = ", mynn.feedforward([[0, 1, 1]]))

    # mynn.dotOperation("multiply_elements",input_set,labels)
