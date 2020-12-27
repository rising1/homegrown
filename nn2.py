import numpy as np

input_size = 4
hidden_size = 10
num_classes = 3
num_inputs = 5

def init_toy_model():
  np.random.seed(0)
  return TwoLayerNet(input_size, hidden_size, num_classes, std=1e-1)

def init_toy_data():
  np.random.seed(1)
  X = 10 * np.random.randn(num_inputs, input_size)
  y = np.array([0, 1, 2, 2, 1])
  return X, y

net = init_toy_model()
X, y = init_toy_data()

# First layer pre-activation
z1 = X.dot(W1) + b1

# First layer activation
a1 = np.maximum(0, z1)

# Second layer pre-activation
z2 = a1.dot(W2) + b2

scores = z2