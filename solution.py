import numpy as np


class LDA:
    def fit(X,y):
        print(X)
        print(y)
        print("\n")
        print(X[y==1])
        # 1. Calculate the between-class variance
        # 2. Calculate the within-class variance
        # 3. Compute the eigenvectors and the corresponding eigenvalues.
        # 4. Put the eigenvalues in decreasing order and select k eigenvectors with the largest eigenvalues.
        # 5. Create a k dimensional matrix containing the eigenvectors.
        number_of_features = len(X[0])
        Sw = np.zeros((number_of_features,number_of_features))
        Sb = np.zeros((number_of_features,number_of_features))

        for i in range(0,1):
            return NotImplementedError



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