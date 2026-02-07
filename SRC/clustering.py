from sklearn.cluster import KMeans

def perform_clustering(X_reduced):
    kmeans = KMeans(n_clusters=10, random_state=42)
    cluster_labels = kmeans.fit_predict(X_reduced)
    return cluster_labels, kmeans
