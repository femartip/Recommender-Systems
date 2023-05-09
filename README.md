# Recommender-Systems

## Non-Personalized Recommender

The goal was to develop a non-personalized recommender based on product association rules:

  - Simple product association: (𝑋 𝑎𝑛𝑑 𝑌)/𝑋
  - Advanced product association: ((𝑋 𝑎𝑛𝑑 𝑌)/𝑋)/((!𝑋 𝑎𝑛𝑑 𝑌)/!𝑋)

As input for the recommender,  I used the MovieLens 1M dataset. This dataset contains ratings collected from the MovieLens web site. https://movielens.org/.
The Notebook contains the following methods:

  - A method for reading the dataset and storing the data in an appropriate format.
  - A method to calculate the simple association value of 2 movies.
  - A method to calculate the advanced association value of 2 movies.
  - A method that provides for a given MovieID, the Top-N MovieIDs with the highest simple association value. In case of a tie, the movie with the higher ID is ranked before the movie with the lower ID. 
  - A method that provides for a given MovieID, the Top-N MovieIDs with the highest advanced association value. In case of a tie, the movie with the higher ID is ranked before the movie with the lower ID. 
  - A method to select the Top-N MovieIDs with the highest frequency. This means, a list of the 
most rated items.

## Personalized Recommender

The goal was to develop a set of personalized recommendation algorithms and run these to generate recommendations.

As input for the recommender, I used the MovieLens 100k dataset. This dataset contains ratings collected from the MovieLens web site. https://movielens.org/. For this recommendations we use the following algorithms:

  - USER USER CF: To compare users, you use the Pearson correlation.
 
  ![image](https://github.com/femartip/Recommender-Systems/assets/99536660/035db32c-2832-4eda-848a-cbd8fddccef8)
  ![image](https://github.com/femartip/Recommender-Systems/assets/99536660/8e826eb1-acfa-47a4-bcec-6a5800eed796)
  
  - ITEM ITEM CF: Model based recommender, we store similarity between items. To compare items in the item item CF, we will use the cosine similarity based on normalized data. 
  
  ![image](https://github.com/femartip/Recommender-Systems/assets/99536660/b7f75caf-254a-4676-ba14-b552af90325e)
  
  - BASKET RECOMMENDATIONS: IICF used for direct Top-N recommendations based on the content of the shopping basket.
  
  ![image](https://github.com/femartip/Recommender-Systems/assets/99536660/b406904a-c639-4d25-a6e5-bbce977133b4)
  
  - HYBRID RECOMMENDATIONS: Combine the rating predictions of UUCF and IICF in a hybrid recommender.

## Content Based Recommender

 The goal was to create and use some content-based recommendation models.
 
 As input for the recommender, I used the MovieLens small dataset from October 2016. The model I build are the following:
 
 -  Basic content-based recommender: Simple content-based recommender that uses the genres as the user's preferences by taking for each user the sum of the positive and negative. In order to compare the movies with the user profiles, one-hot encode the movies so that each row represents a movie and the columns represent features rating values associated with each genre. Finally, to get the predicted score for each user for each movie, compute the dot-product between the movies and the user profile.
 -  Normalizing features: Dividing the values of each feature by the square root of the number of genres.
 -  Accounting for differences in frequency: Include the inverse document frequency (IDF) into our prediction function.
 -  Diversifying the recommendations: Apply maximum marginal relevance (MMR). With MMR, items are selected according to a combined criterion that takes the similarity with the user profile and already selected items into account.

## Lensekit

Use Lenskit (https://lenskit.org/) recommender toolkit to build a recommender.

As input for the recommender, you will use the MovieLens 100k dataset. This dataset contains ratings collected from the MovieLens web site. https://movielens.org/. I tried the following algorithms:

- Personalized Mean Rating Prediction (basic.Bias) with damping=5, other parameters have the default value.
- Item-based k-NN Collaborative Filtering (item_knn.ItemItem) with nnbrs = 20 (number of neighbors), other parameters have the default value.
- User-based k-NN Collaborative Filtering (user_knn.UserUser) with nnbrs = 20 (number of neighbors), other parameters have the default value.
- Biased matrix factorization with Alternating Least Squares (als.BiasedMF) with 50 features, other parameters have the default value.
- Implicit matrix factorization trained with Alternating Least Squares (als.ImplicitMF) with 50 features, other parameters have the default value.
 -  The Funk SVD algorithm. (funksvd.FunkSVD) with 50 features, other parameters have the default value

Then some predictions and evaluations were tested using this algorithms.

 
