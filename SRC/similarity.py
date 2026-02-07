from sklearn.metrics.pairwise import cosine_similarity

def compute_cosine_similarity(X_reduced):
    sim_matrix = cosine_similarity(X_reduced)
    return sim_matrix
