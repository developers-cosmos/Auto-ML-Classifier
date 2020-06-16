import os, ast
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
import pickle

def main():
    dataset_path = "https://raw.githubusercontent.com/" + os.environ["GITHUB_REPOSITORY"] +"/master/dataset.csv"
    data = pd.read_csv(dataset_path)
    print()
    print(data.describe())

    x=data.iloc[:,:-1]
    y=data.iloc[:,-1]


    column_trans = make_column_transformer((OneHotEncoder(),[-1]),remainder='passthrough')
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)
    
    pipe = make_pipeline(column_trans,SVC())

    pipe.fit(x_train,y_train)
    print("\nModel Training Finished")
    accuracy = pipe.score(x_test,y_test)

    print("\nAccuracy of the Model: "+str(accuracy*100))
    if pipe:
        pickle.dump(pipe,open('model.pkl','wb'))

    if not os.environ["INPUT_MYINPUT"] == 'zeroinputs':
        inputs = ast.literal_eval(os.environ["INPUT_MYINPUT"])
        print("\nThe Predicted Ouput is :")
        output = pipe.predict([inputs])
        print(output)
    else:
        output = ["None"]
        print("\nUser didn't provided inputs to predict")
    print("\n=======================Action Completed========================")


    print(f"::set-output name=myOutput::{output[0]}")


if __name__ == "__main__":
    main()