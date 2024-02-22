import numpy as np


class LDA:
    def fit(X,y):
        print(X)
        print(y)
        return NotImplementedError
    def predict_proba(Xtest):
        return NotImplementedError
    def predict(Xtest):
        return NotImplementedError
    def get_params():
        return NotImplementedError
    
class QDA:
    def fit(X,y):
        return NotImplementedError
    def predict_proba(Xtest):
        return NotImplementedError
    def predict(Xtest):
        return NotImplementedError
    def get_params():
        return NotImplementedError
    

class NB:
    def fit(X,y):
        return NotImplementedError
    def predict_proba(Xtest):
        return NotImplementedError
    def predict(Xtest):
        return NotImplementedError
    def get_params():
        return NotImplementedError
    


def main():
    testDataSet = np.random.random((5, 10))
    testYVariables = np.random.randint(2,size=5)
    LDA.fit(testDataSet,testYVariables)

if __name__ == "__main__":
    main()