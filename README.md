# Netflix Content Clustering & Recommendation System  

## Project Overview
This project implements an Unsupervised Machine Learning based system to cluster Netflix movies and TV shows based on semantic content and generate content-based recommendations. Unlike traditional systems that rely on user ratings or watch history, this approach uses only textual metadata such as title, genres, cast, directors, and description. The system uses Natural Language Processing (NLP) to convert text into numerical features, reduces dimensionality, applies clustering to group similar content, and uses cosine similarity to recommend similar titles.

## Dataset
The dataset used is a Netflix catalogue CSV containing the following columns:
| Column Name | Description |
|-------------|-------------|
| title       | Movie / TV Show title |
| listed_in   | Genres/categories |
| description | Short overview of content |
| cast        | Actors/actresses |
| director    | Director name |
| type        | Movie or TV Show |
| country     | Country of origin |

The dataset is located in the  
'data/NetflixSimple.csv' file.

## Methodology
  1. **Data Loading**  
       - Load Netflix data from CSV and handle missing values.
  2. **Text Combination**  
       - Combine key fields into a single textual feature for semantic understanding.
  3. **NLP Preprocessing**  
       - Clean and normalize text (lowercase, remove stopwords, remove symbols).
  4. **Feature Extraction**  
       - Convert text to numerical vectors using **TF-IDF Vectorizer**.
  5. **Dimensionality Reduction**  
       - Reduce high-dimensional TF-IDF vectors using **Truncated Singular Value Decomposition (SVD)**.
  6. **Clustering**  
       - Apply **KMeans Clustering** to group similar content.
  7. **Evaluation**  
       - Compute **Silhouette Score** to evaluate cluster quality.
  8. **Similarity Modeling**  
       - Use **Cosine Similarity** to calculate similarity between content vectors.
  9. **Recommendation System**  
       - Return the top 5 most similar titles for a given content item.

## Technologies Used
| Category                 | Tools & Libraries |
|--------------------------|-------------------|
| Language                 | Python |
| NLP                      | NLTK   |
| Vectorization            | Scikit-learn TF-IDF |
| Dimensionality Reduction | Truncated SVD |
| Clustering               | KMeans |
| Similarity               | Cosine Similarity |
| Evaluation               | Silhouette Score |
| Development              | Google Colab |

## Sample Outputs
 ==> Clustered Data Snapshot
     |      | title                       | type    | listed_in  	             | cluster |
     |------|-----------------------------|---------|--------------------------|---------|
     | 4572	| Oddbods: Party Monsters	    | Movie	  | Movies	                 | 4   |
     | 2120	| Fast & Furious Spy Racers   |	TV Show | 	Kids' TV               | 4 |
     | 5437	| Scooby-Doo on Zombie Island |	Movie	  | Children & Family Movies | 4 |
     | 1558	| Cutie and the Boxer       	| Movie	  | Documentaries            | 3 |
     | 7230	| Triumph of the Heart	      | Movie	  | Dramas, Sports Movies	   | 4 |

 ==> Recommendations for “3 Idiots”
      - PK
      - Dil Chahta Hai
      - Rang De Basanti
      - War Chhod Na Yaa

## Project Description
This project implements a content-based recommendation system for Netflix content using unsupervised machine learning techniques. The system clusters movies and TV shows based on semantic similarity derived from textual metadata such as genres, descriptions, cast, and directors. The goal of the project is to group similar content and provide recommendations without relying on user ratings or viewing history. The model uses NLP techniques, feature extraction, dimensionality reduction, clustering algorithms, and similarity measures to achieve accurate and scalable recommendations.
=> This project demonstrates practical applications of:
    -- Natural Language Processing (NLP)
    -- Machine Learning
    -- Unsupervised Learning
    -- Recommendation Systems

## Future Enhancements
 -> Integration of user behavior data (ratings, watch history)
 -> Hybrid recommendation system (content-based + collaborative filtering)
 -> Real-time recommendation engine
 -> Web-based interface for interactive usage
 -> Personalized user profiles

## Author
  Jyothika Sigirisetty
  B.Tech – Computer Science and Engineering
  Lakireddy Balireddy College of Engineering, Mylavaram  
  **Email:** 
    - jyothisigirisetty@gmail.com  
  **GitHub:**
    - [S-Jyothika](https://github.com/S-Jyothika)

## License
This project was developed as part of the **AI Final Project** coursework for educational purposes.
