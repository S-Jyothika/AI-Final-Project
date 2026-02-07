from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(title, data, matrix, top_n=5):
    index = data[data['title'].str.lower() == title.lower()].index[0]

    similarity_scores = cosine_similarity(
        matrix[index].reshape(1, -1),
        matrix
    )[0]

    ranked_scores = sorted(
        list(enumerate(similarity_scores)),
        key=lambda x: x[1],
        reverse=True
    )

    top_items = ranked_scores[1:top_n+1]
    indices = [i[0] for i in top_items]

    return data.iloc[indices][['title','listed_in','cluster']]
