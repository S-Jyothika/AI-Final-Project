from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(X_reduced):
    similarity_matrix = cosine_similarity(X_reduced)
    return similarity_matrix
