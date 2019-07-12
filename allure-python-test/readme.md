# Allure report integration 

# Main Link : 
- https://docs.qameta.io/allure/#_pytest

# Install Allure

     pip install allure-pytest
# Alure : Run test 

    py.test --alluredir=$allure_result_folder ./tests
    
- if you want specific test to run 
 
          python3 -m pytest test_class --alluredir=$allure_result_folder
# Aluure see reports 
    
    allure serve $allure_result_folder
     
# Local Testing : Installations 

# Jenkins : Installations 
