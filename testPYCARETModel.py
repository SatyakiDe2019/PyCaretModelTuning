#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 31-Mar-2023                     ####
#### Modified On 31-Mar-2023                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### testing script for PyCaret package.         ####
####                                             ####
#####################################################

import clsL as cl
from clsConfigClient import clsConfigClient as cf
import datetime

from pycaret.classification import load_model, predict_model

import pandas as p

# Disbling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

######################################
### Get your global values        ####
######################################
debug_ind = 'Y'

# Initiating Logging Instances
clog = cl.clsL()

model_path = cf.conf['MODEL_PATH']
model_name = cf.conf['MODEL_NAME']

######################################
####         Global Flag      ########
######################################

def main():
    try:
        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('*'*120)
        print('Start Time: ' + str(var))
        print('*'*120)

        FullFileName = model_path + model_name

        # Load the saved model
        loaded_model = load_model(FullFileName)

        # Prepare new data for testing (make sure it has the same columns as the original data)
        new_data = p.DataFrame({
            "Pclass": [3, 1],
            "Sex": ["male", "female"],
            "Age": [22, 38],
            "SibSp": [1, 1],
            "Parch": [0, 0],
            "Fare": [7.25, 71.2833],
            "Embarked": ["S", "C"]
        })

        # Make predictions using the loaded model
        predictions = predict_model(loaded_model, data=new_data)

        # Display the predictions
        print(predictions)

        print('*'*120)
        var1 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('End Time: ' + str(var1))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()
