import numpy as np


class LDA:
    def fit(X,y):
        # 1. Calculate the between-class variance
        # 2. Calculate the within-class variance
        # 3. Compute the eigenvectors and the corresponding eigenvalues.
        # 4. Put the eigenvalues in decreasing order and select k eigenvectors with the largest eigenvalues.
        # 5. Create a k dimensional matrix containing the eigenvectors.
        number_of_features = len(X[0])
        classes = np.unique(y)

        # scatter within classes
        Sw = np.zeros((number_of_features,number_of_features))

        # scatter between classes
        Sb = np.zeros((number_of_features,number_of_features))

        for i in classes:
            X_i=X[y==i]
            means = np.mean(X_i)
            Sw += (X_i-means).T.dot((X_i-means))

            diff = (means-np.mean(X,axis=0)).reshape(number_of_features,1)
            Sb += len(classes) * (diff).dot(diff.T)

        A = np.linalg.inv(Sw).dot(Sb)
        eigen_values, eigen_vectors = np.linalg.eig(A)
        eigen_vectors = eigen_vectors.T


        sorted_eigens = np.argsort(abs(eigen_values))[::-1]
        eigen_values,eigen_vectors = eigen_values[sorted_eigens], eigen_vectors[sorted_eigens]
        linear_discriminants = eigen_vectors[0:2]

        explained_variance_ratio = np.sort(eigen_values/np.sum(eigen_values))[::-1][:2]
        print(explained_variance_ratio)

        
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
    testDataSet = np.random.random((100, 10))
    testYVariables = np.random.randint(2,size=100)
    LDA.fit(testDataSet,testYVariables)

if __name__ == "__main__":
    main()