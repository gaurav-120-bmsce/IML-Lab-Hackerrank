import json, sys
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import HashingVectorizer

if sys.version_info[0] >= 3:
    user_input = input

vectorizer = HashingVectorizer(stop_words='english')

training_data = []
training_labels = []
file = open('training.json')

for _ in range(int(file.readline())):
    data = json.loads(file.readline())
    training_data.append(data['question'] + "\r\n" + data['excerpt'])
    training_labels.append(data['topic'])

file.close()

transformed_training_data = vectorizer.fit_transform(training_data)
classifier = LinearSVC()
classifier.fit(transformed_training_data, training_labels)

test_data = []
for _ in range(int(user_input())):
    data = json.loads(user_input())
    test_data.append(data['question'] + "\r\n" + data['excerpt'])

transformed_test_data = vectorizer.transform(test_data)
predicted_labels = classifier.predict(transformed_test_data)

for label in predicted_labels:
    print(label)
