import numpy as np

class NN:

    def __init__(self,input_set,targets):

        self.weights1 = np.random.rand(3, 1)
        print("self.weights1= ", self.weights1)
        self.biases1 = np.random.rand(1,)
        print("self.biases1= ",self.biases1)


    def feedforward(self, batch):
        # multiply by weights and add bias
        self.batch = np.reshape(batch,[1,3])
        self.z1 = self.batch.dot(self.weights1) + self.biases1
        self.dz1 = np.zeros_like(self.z1)
        self.dz1[self.z1 <= 0] = 0
        self.dz1[self.z1 > 0] = 1
        self.a1 = np.maximum(0,self.z1) # this is the activation function # **** This is working as expected
        return self.a1


    def calc_error(self,target):
        self.error = (self.a1 - target)
        self.meanSquaredError = np.mean(self.error**2)



    def back_prop(self,batch):
        # back propagation chain rule calculus
        learning_rate = 0.001
        self.batchT = np.reshape(batch,[3,1])
        self.gradientWeights = 2/self.batchT.shape[1] * np.dot( self.batchT,self.error * self.dz1)
        self.gradientBias = np.sum(self.error, axis=0, keepdims=True)
        self.weights1Adj  = - learning_rate * self.gradientWeights
        self.biases1Adj = - learning_rate * self.gradientBias
        self.weights1 = self.weights1 + self.weights1Adj
        self.biases1 = self.biases1 + self.biases1Adj





if __name__ == '__main__':

    input_set = np.array([[0, 1, 0],
                          [0, 0, 1],
                          [1, 0, 0],
                          [1, 1, 0],
                          [1, 1, 1],
                          [0, 0, 0]])  # Dependent variable

    labels = np.array([[1],
                       [0],
                       [0],
                       [1],
                       [1],
                       [0]])

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
                # print("feed forward value= ",mynn.z1)
                print("error= ",mynn.meanSquaredError)
                # print("error shape= ",np.shape(mynn.error))
                # print("Input batch transposed shape= ",np.shape(mynn.batch))
                # print("transposed batch= ", mynn.batchT)
                # print ("gradient weights shape = ",np.shape(mynn.gradientWeights))
                # print("Gradient weights=",mynn.gradientWeights)
                # print("activation= ",mynn.a1)
                # print("weights1= ",mynn.weights1)
                # print("Weights shape= ",np.shape(mynn.weights1))
                # print("weightsAdj= ",mynn.weights1Adj)


    # print("final weights= ", mynn.weights1)
    # print("final bias= ", mynn.biases1)
    # print("final error= ", mynn.meanSquaredError)
    print("\n")
    print("test [1, 0, 1] should be 0 = ", mynn.feedforward([[1, 0, 1]]))
    print("test [0, 1, 1] should be 1 = ", mynn.feedforward([[0, 1, 1]]))
