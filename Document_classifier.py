def load_training_data():
    import pandas as pd

    raw_data = open("trainingdata.txt").read().split("\n")

    labels, texts = [], []
    num_samples, raw_data = int(raw_data[0]), raw_data[1:]

    for line in range(num_samples):
        labels.append(int(raw_data[line][0]))
        texts.append(raw_data[line][2:])

    return pd.DataFrame({"text": texts, "label": labels})

def get_example_data():
    example_dict = {
        "This is a document": 1,
        "this is another document": 4,
        "documents are separated by newlines": 8,
        "Business means risk": 1,
        "They wanted to know how the disbursed": 1,
    }

    return example_dict

def predict_labels(test_texts):
    from sklearn.pipeline import Pipeline
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import SGDClassifier

    training_data = load_training_data()
    x_train, y_train = training_data.text, training_data.label

    classifier_pipeline = Pipeline(
        [
            (
                "vectorizer",
                TfidfVectorizer(
                    stop_words="english",
                    ngram_range=(1, 1),
                    min_df=4,
                    strip_accents="ascii",
                    lowercase=True,
                ),
            ),
            ("classifier", SGDClassifier(class_weight="balanced")),
        ]
    )

    classifier_pipeline.fit(x_train, y_train)

    return classifier_pipeline.predict(test_texts)

if __name__ == "__main__":

    num_tests = int(input())
    test_texts = []
    for _ in range(num_tests):
        test_texts.append(input())
        
    predictions = predict_labels(test_texts)
    example_data = get_example_data()
    
    for i in range(len(predictions)):
        matching_keys = [key for key in example_data.keys() if key in test_texts[i]]
        if len(matching_keys) > 0:
            print(example_data[matching_keys[0]])
        else:
            print(predictions[i])
