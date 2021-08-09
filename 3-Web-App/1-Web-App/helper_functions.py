import pandas as pd
import matplotlib.pyplot as plt
from typing import Union
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression

class TrainingSet():
    def __init__(self, dataframe:pd.DataFrame, Selected_features:list, Target_feature:str, **kwargs) -> None:
        df = dataframe
        self.X = df[Selected_features]
        self.y = df[Target_feature]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, **kwargs)
        return

    def Build_LogisticRegression(self, **kwargs) -> None:
        self.model = LogisticRegression(**kwargs)
        self.model.fit(self.X_train, self.y_train)
        self.predictions = self.model.predict(self.X_test)
        return

    def Print_ClassificationReport(self) -> None:
        print(classification_report(self.y_test, self.predictions))
        print('Predicted labels: ', self.predictions)
        print('Accuracy ', accuracy_score(self.y_test, self.predictions))

def plot_scatter(x_label: str, y_label:str, dataset:pd.DataFrame, hue:Union[str, None]=None) -> None:
    plt.scatter(x_label,y_label,data=dataset, c=hue)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    print('correlation')
    print(dataset[x_label].corr(dataset[y_label]))
    return

def plot_correlation(dataframe:pd.DataFrame) -> pd.DataFrame.corr:
    corr = dataframe.corr()
    return corr.style.background_gradient(cmap='coolwarm')