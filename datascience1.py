datascience1.py 

from sklearn import tre


#[height, weight, shoe size]
X = [[181, 80,44], [177, 70, 43], [160, 60, 38], [166, 65,40], [190,90,47], [154, 85, 33], [175,64,38], [177,70,40], [177,70,40],[159,55,33],[181,85,43]]

Y = ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male']


clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[111,16,44]])

print (prediction)
