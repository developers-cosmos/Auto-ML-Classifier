# GitHub Action to Train a Machine Learning Classifier
This action will allow the users to train a Machine Learning Model with the given dataset. The user can able to download the model file after training.
## Environment Variable
- GITHUB_REPOSITORY - <i>Required</i> This variable is used to get the username and repository name. The repository must contain dataset to train the model with name 'dataset.csv'
## Arguments
- <i>Required</i> - After the model is trained, user can pass the inputs to predict the classified output with format ```[input1,input2,input2]```
## Examples
Here's an example workflow that uses Auto ML Classifier action. The workflow is triggered by a ```PUSH``` event and looks for the dataset.csv
```
name: Iris Dataset Classifier
on: [push]
jobs:
  build_model:
    runs-on: ubuntu-latest
    steps:
    - name: Train the model
      id: model
      uses: developers-cosmos/Auto-ML-Classifier@master
      with:
        myInput: "[5.1,3.5,1.4,0.2]"
    - name: Upload model.pkl 
      uses: actions/upload-artifact@v2
      with:
        name: my-artifact
        path: model.pkl
```
