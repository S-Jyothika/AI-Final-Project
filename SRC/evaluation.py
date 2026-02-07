from sklearn.metrics import silhouette_score

def calculate_silhouette(X_reduced, labels):
    score = silhouette_score(X_reduced, labels)
    return score
