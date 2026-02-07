from sklearn.decomposition import TruncatedSVD

def reduce_dimensions(X):
    svd = TruncatedSVD(n_components=200, random_state=42)
    X_reduced = svd.fit_transform(X)
    return X_reduced, svd
