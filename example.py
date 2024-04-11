from sklearn.datasets import make_blobs

X,y=make_blobs(n_samples=100,n_features=2,centers=2,random_state=1)
print(X.shape,y.shape)
print(X[:5])
print(y[:5])