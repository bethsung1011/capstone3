# Capstone 3 : MatchMaker Recommender 


## Overview

The goal of this project is to find the possible best match using unsupervised machine learning algorithms with given data.  Unlike machine learning, the characteristic of Unsupervised learning is No labels. No target. (or we say No gods. No masters.) so the use case of this scenario can be that I have a database of users with their attributes and I want to draw profiles using this technique. 



## The Data

OkCupid is a mobile dating app. It sets itself apart from other dating apps by making use of a pre computed compatibility score, calculated by optional questions the users may choose to answer. In this dataset, there are 60k records containing structured information such as age, sex, orientation as well as text data from open ended descriptions.

![](https://github.com/bethsung1011/capstone3/blob/main/img/tell_us_about_your_self_1.png)

When you sign up on a website in general there is no information about the user. It is called Cold start. Unlike other websites, minimum 15 questions must be answered to match you to other users. 

![](https://github.com/bethsung1011/capstone3/blob/main/img/tell_us_about_your_self_2.png)

In order to increase your match percentage, you can answer optional questions the users may choose to answer, and write down short essays about you and what you are looking for. 



## Flow


![](https://github.com/bethsung1011/capstone3/blob/main/img/Machine-Learning-Explained2.png)

Flow is started like this. Get data, Clean, Prepare, Manipulate data  - >  Discover  latent variables and analyze what this means. -> Do Feature engineering, preprocessing and Autoencoding for making smaller representations of the original data as in data compression. -> Train test and Evaluate improve the model  

## Recommender Systems​
​
![](https://github.com/bethsung1011/capstone3/blob/main/img/recommend.png)

Not like movie recommenders or product reviews, there are no harsh ratings between people. We cannot say like this person is 1 start or that person is 5 stars. ​ We are all different.  Predictions are made based on the properties or characteristics of the user.  

![](https://github.com/bethsung1011/capstone3/blob/main/img/cosine_similarity.png)

I focus on content based filtering between user and user. In general, people tend to get attracted to similar-looking or similar preferences. 



## Model


### CountVectorizer​
![](https://github.com/bethsung1011/capstone3/blob/main/img/countvec.png)

CountVectorizer​ is to use a natural language process and I utilized this to analyze users’ essays. It transforms a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text. It helps to know what the user is like and finding other users with similar attributes by analyzing the essay part of the profile composed by users to increase their match percentage to other users.  

CountVectorizer uses a similarity metric for the evaluation. I tried cosine distance, euclidean distance, manhattan distance and chose cosine distance, calculated similarity to others and delivered top recommendations. 

![](https://github.com/bethsung1011/capstone3/blob/main/img/symmetry-12-00121-g001.png)


### Singular Value Decomposition (SVD)

Singular Value Decomposition (SVD)​ is a method from linear algebra that has been generally used as a dimensionality reduction technique.​  Matrix Factorization interactions reduced to linear combinations to reconstruct missing values. Data turns into the matrix and is factorized using SVD. Matrices contain orthogonal vectors and These vectors are latent topics. 
By selecting the number of singular values, you are simultaneously reducing dimensionality and eliminating collinearity, and finding latent topics that can be used to reconstruct your original data and provide recommendations. 



## Demo 

![](https://github.com/bethsung1011/capstone3/blob/main/img/streamlit_intro.png)

http://192.168.0.105:8501

In order to show this demo, I used streamlit web app and I am going to present  the outcome of matchmaker recommender;

Also, 14 cohort crews participated and entered the test dataset. I matched them against okcupid 60000 users. Also to keep it anonymous, everyone used a nickname and all attributes were randomly shuffled. You see your nickname but that is not you   for your information.  
Ok, I picked Miranda. She is 22 and I will find her match using Singular Value Decomposition, CountVectorizer . 

In Singular Value Decomposition, individual feature categories become columns and individual users become rows, this makes a matrix then decomposes three matrices (U sigma V)  and the latent factors show the characteristics of the users. It reduces the dimension through latent factors’ extraction and recommends the top matches based on the calculation . 

In CountVectorizer, it analyzes the profile essay portion with natural language process and provides recommendations based on that. This test dataset only fed non-verval information, so  it automatically eliminates people who wrote lengthy essay and only matches around 5000 people out of 60,000 people who have not wrote essay neither;   This used cosine similarity metrics to make the match recommendation 


## Future Implementation Considerations

The issue is that live recommendation is not available because adding information to a given database is not capable for me yet. 
The solution ​is to create the schema in the database and store based on input and feed as needed​.
New features to implement ​is the Gensim Doc2Vec approach for NLP​​.



## Tools

![](https://github.com/bethsung1011/capstone3/blob/main/img/source.png)
