__author__ = 'roctbb'
import pickle
import Orange.classification
with open('credit.pickle', 'rb') as f:
    clf = pickle.load(f)

data = Orange.data.Table("credit.arff")
print(type(data[0]));
data[0]["class"] = ""
data[0]["checking_status"]="0<=X<200"
print(clf(data[0]))