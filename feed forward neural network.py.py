import numpy as np

def sigmoid(x): return 1/(1+np.exp(-x))
def sigmoid_deriv(x): return x*(1-x)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(1)
w1 = np.random.rand(2,2)
w2 = np.random.rand(2,1)

for _ in range(10000):
    l1 = sigmoid(np.dot(X, w1))
    out = sigmoid(np.dot(l1, w2))
    error = y - out
    d_out = error * sigmoid_deriv(out)
    d_l1 = np.dot(d_out, w2.T) * sigmoid_deriv(l1)
    w2 += np.dot(l1.T, d_out)
    w1 += np.dot(X.T, d_l1)

print("Predicted Output:\n", np.round(out, 3))