# AI_Project_Methodology

## Code Documentation Using Sphinx

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
    
    
    
    
    
