# House prices prediction

# Goal and problem to solve
Evaluating the house price is a complicated task dependent on large amount of variables. Nowadays this task is usually given to professionals in exchange for gratification. But what if we wanted to predict our house price without big costs just based on data we have? Well, with our prediction system now it is possible. As mention before this task is not a simple one that's why in our application we predict the price of a house, based on many features: number of square meters, year of construction, garage and pool availability, and others.

## Users
We are targeting house owners or any person interested in evaluating some property, without any cost. Our dataset is coming from city of Ames, Iowa (US) that's why for now only properties in this city can be evaluated accurately. We don't recommend using application for evaluating properties in different cities as the results may not be accurate.

## Dataset
House prices dataset taken from [kaggle competition.](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

## Project management framework
As project wasn't very broad and team consisted of only 2 people, we decided to proceed with initial meeting where we have shaped the requirements and planned the work, then we proceed with on-demand meetings when we had any doubts about our parts or integrating different components together. For code versioning we used git and Github, with different branches for separate compontents of application.

## Work division
### Megha 
Data preparation, integration of SHAP library into project, generation of sphinx documentation.
### Mateusz
Feature engineering, model training, model inference and mlflow integration.
