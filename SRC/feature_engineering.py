def build_content(df):
    df['content'] = (
        df['title'] + ' ' +
        df['listed_in'] + ' ' +
        df['description'] + ' ' +
        df['cast'] + ' ' +
        df['director']
    )
    return df
