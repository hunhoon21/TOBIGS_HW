import numpy as np

class TwoLayerNet():
    """
    2 Layer Network를 만드려고 합니다.

    해당 네트워크는 다음과 같은 구조를 따릅니다.

    input - Linear - ReLU - Linear - Softmax

    Softmax 결과는 입력 N개의 데이터에 대해 각 클래스에 대한 확률입니다.
    """

    def __init__(self, input_size, hidden_size, output_size, std=1e-4):
         """
         네트워크에 필요한 가중치들을 initialization합니다.
         해당 가중치들은 self.params 라는 Dictionary에 담아둡니다.

         input_size: 데이터의 변수 개수 - D
         hidden_size: 히든 층의 H 개수 - H
         output_size: 클래스 개수 - C

         """

         self.params = {}
         self.params["W1"] = std * np.random.randn(input_size, hidden_size)
         self.params["b1"] = np.zeros(hidden_size)
         self.params["W2"] = std * np.random.randn(hidden_size, output_size)
         self.params["b2"] = np.zeros(output_size)

    def forward(self, X, y=None):
        """

        X: input 데이터 (N, D)
        y: 레이블 (N,)

        Linear - ReLU - Linear - Softmax - CrossEntropy Loss

        y가 주어지지 않으면 Softmax 결과 p와 Activation 결과 a를 return합니다. p와 a 모두 backward에서 미분할때 사용합니다.
        y가 주어지면 CrossEntropy Error를 return합니다.

        """

        W1, b1 = self.params["W1"], self.params["b1"]
        W2, b2 = self.params["W2"], self.params["b2"]
        N, D = X.shape

        # 여기에 p를 구하는 작업을 수행하세요.

        h = np.dot(X, W1) + b1
        a = np.maximum(h, 0)
        scores = np.dot(a, W2) + b2

        o = np.exp(scores - np.max(scores, axis=1, keepdims=True))  # stable exponential for scores
        p = o / np.sum(o, axis=1, keepdims=True)

        if y is None:
            return p, a

        # 여기에 Loss를 구하는 작업을 수행하세요.

        Loss = None

        LL = -np.log(p[np.arange(N), y])  # get LogLikelihood
        Loss = np.mean(LL)  # get p loss

        return Loss


    def backward(self, X, y, learning_rate=1e-5):
        """

        X: input 데이터 (N, D)
        y: 레이블 (N,)

        grads에는 Loss에 대한 W1, b1, W2, b2 미분 값이 기록됩니다.

        원래 backw 미분 결과를 return 하지만
        여기서는 Gradient Descent방식으로 가중치 갱신까지 합니다.

        """
        W1, b1 = self.params["W1"], self.params["b1"]
        W2, b2 = self.params["W2"], self.params["b2"]

        N = X.shape[0] # 데이터 개수
        grads = {}

        p, a = self.forward(X)

        # 여기에 각 파라미터에 대한 미분 값을 저장하세요.

        dp = np.array(p)
        dp[np.arange(N), y] -= 1  # p-y

        da = np.dot(dp, W2.T) * (a > 0)

        grads["W2"] = 1 / N * np.dot(a.T, dp)
        grads["b2"] = np.mean(dp, axis=0)
        grads["W1"] = 1 / N * np.dot(X.T, da)
        grads["b1"] = np.mean(da, axis=0)

        self.params["W2"] -= learning_rate * grads["W2"]
        self.params["b2"] -= learning_rate * grads["b2"]
        self.params["W1"] -= learning_rate * grads["W1"]
        self.params["b1"] -= learning_rate * grads["b1"]

    def accuracy(self, X, y):

        p, _ = self.forward(X)
        y_pred = np.argmax(p, axis=1)

        return np.sum(y_pred==y)/len(X)