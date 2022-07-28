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

# Model
We trained Random Forest Classifier model to predict house price. The output of the model is float value - estimated number of dollars the property is worth.
# Inference
Predictions of test set can be found in the notebook. Also there we can find examples of the usage of our model.<br /><br />


# Code Documentation Using Sphinx

### Steps

1. install Sphinx using 

  ```bash 
        $ pip install sphinx sphinx_rtd_theme
   ```
2. To start, go to docs folder and run the command 

  ```bash 
        $ sphinx-quickstart
   ```
   And give the necessary details like project name, authors, etc
   Then it will create a template for the documentation.
   
   The generated conf.py file can be modified to change the theme and adding additional confgurations. 
   
   <img width="337" alt="image" src="https://user-images.githubusercontent.com/68321717/180651954-f04a5008-9542-4f4d-b8f1-d0b12126365e.png">
    <img width="337" alt="image" src="https://user-images.githubusercontent.com/68321717/180651975-b6f25f85-7e92-466b-9650-07038a63b909.png">
    <img width="337" alt="image" src="https://user-images.githubusercontent.com/68321717/180652005-2c4610c7-2bfb-477c-85a2-80f9d61b07da.png">


3. Go to the root folder and specify the folder where the code to be documented is located. 
   In our example, src is the folder containg the scripts
    ```bash 
        $ cd ..
        $ sphinx-apidoc -o docs src/
    ```
    It will generate .rst file for all the .py scripts, index.rst and module.rst
    
 4. To generate HTML, 
    First include module file inside index.rst
    
    
    <img width="428" alt="image" src="https://user-images.githubusercontent.com/68321717/180652139-9c022c71-26cd-4619-976b-48e4d57e1342.png">


    Go to the docs folder and excecute the following command
    ```bash 
        $ cd docs
        $ make html
    ```
    This will generate the html files inside build directory. 
    
 5. If you change your code and need to update html, follow the code
    ```bash 
        $ make clean
        $ make html
    ```
    
    
# Visualisation of model decision using SHAP

It is a tool to interpret machine learning model using visualisation.

### Steps

1. install SHAP using 

  ```bash 
        pip install shap
     or
        conda install -c conda-forge shap
   ```
   
2. In our application we are using 'RandomForestRegressor' model for the prediction. 
   The suitable method in SHAP to explain this model is 'TreeExplainer'.
   We give the model as input to the SHAP TreeExplainer. 
   
   The results we obtained is stored under reports directory
   
    
