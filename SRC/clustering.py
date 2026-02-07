from sklearn.cluster import KMeans

def apply_kmeans(X_reduced, k=10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_reduced)
    return labels, kmeans
