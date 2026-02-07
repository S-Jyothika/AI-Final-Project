from sklearn.decomposition import TruncatedSVD

def apply_svd(X, n_components=200):
    svd = TruncatedSVD(n_components=n_components, random_state=42)
    X_reduced = svd.fit_transform(X)
    return X_reduced, svd
