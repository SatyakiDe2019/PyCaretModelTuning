#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 31-Mar-2023                     ####
#### Modified On 31-Mar-2023                     ####
####                                             ####
#### Objective: This is the main class that      ####
#### contains the core logic of low-code         ####
#### machine-learning library to evaluate the    ####
#### best model for your solutions.              ####
####                                             ####
#####################################################

import clsL as cl
from clsConfigClient import clsConfigClient as cf
import datetime

# Import necessary libraries
import pandas as p
from pycaret.classification import *

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
###############################################
###    End of Global Section                ###
###############################################


class clsTrainModel:
    def __init__(self):
        self.model_path = cf.conf['MODEL_PATH']
        self.model_name = cf.conf['MODEL_NAME']

    def trainModel(self, FullFileName):
        try:
            df = p.read_csv(FullFileName)
            row_count = int(df.shape[0])
            print('Number of rows: ', str(row_count))

            print(df)

            # Initialize the setup in PyCaret
            clf_setup = setup(
            data=df,
            target="Survived",
            train_size=0.8, # 80% for training, 20% for testing
            categorical_features=["Sex", "Embarked"],
            ordinal_features={"Pclass": ["1", "2", "3"]},
            ignore_features=["Name", "Ticket", "Cabin", "PassengerId"],
            #silent=True,  # Set to False for interactive setup
            )

            # Compare various models
            best_model = compare_models()

            # Create a specific model (e.g., Random Forest)
            rf_model = create_model("rf")

            # Hyperparameter tuning
            tuned_rf_model = tune_model(rf_model)

            # Evaluate model performance
            plot_model(tuned_rf_model, plot="confusion_matrix")
            plot_model(tuned_rf_model, plot="auc")

            # Finalize the model (train on the complete dataset)
            final_rf_model = finalize_model(tuned_rf_model)

            # Make predictions on new data
            new_data = df.drop("Survived", axis=1)
            predictions = predict_model(final_rf_model, data=new_data)

            # Writing into the Model
            FullModelName = self.model_path + self.model_name

            print('Model Output @:: ', str(FullModelName))
            print()

            # Save the fine-tuned model
            save_model(final_rf_model, FullModelName)

            return 0

        except Exception as e:
            x = str(e)
            print('Error: ', x)

            return 1
