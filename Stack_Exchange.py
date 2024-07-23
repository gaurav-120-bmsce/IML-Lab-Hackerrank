import json, sys
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import HashingVectorizer

if sys.version_info[0] >= 3:
    get_input = input

text_vectorizer = HashingVectorizer(stop_words='english')

train_texts = []
train_labels = []
train_file = open('training.json')

for _ in range(int(train_file.readline())):
    record = json.loads(train_file.readline())
    train_texts.append(record['question'] + "\r\n" + record['excerpt'])
    train_labels.append(record['topic'])

train_file.close()

transformed_train_texts = text_vectorizer.fit_transform(train_texts)
svm_classifier = LinearSVC()
svm_classifier.fit(transformed_train_texts, train_labels)

test_texts = []
for _ in range(int(get_input())):
    test_record = json.loads(get_input())
    test_texts.append(test_record['question'] + "\r\n" + test_record['excerpt'])

transformed_test_texts = text_vectorizer.transform(test_texts)
predicted_labels = svm_classifier.predict(transformed_test_texts)

for predicted_label in predicted_labels:
    print(predicted_label)
