
# from yellowbrick.text import DispersionPlot, dispersion
# from yellowbrick.datasets import load_hobbies
#
# # Load the text data
# corpus = load_hobbies()
# print(corpus.data)

# # Create a list of words from the corpus text
# text = [doc.split() for doc in corpus.data]
#
# # Choose words whose occurence in the text will be plotted
# target_words = ['features', 'mobile', 'cooperative', 'competitive', 'combat', 'online']
#
# # Create the visualizer and draw the plot
# dispersion(target_words, text, colors=['olive'])

# from sklearn.svm import SVR
# from sklearn.model_selection import cross_val_score
# import numpy as np
#
# # X, y = make_friedman1(n_samples=50, n_features=10, random_state=0)
# X = np.random.random([50, 400, 10])
# y = np.random.random([50])
# print(X.shape, y.shape)
#
#
# estimator = SVR(kernel="linear")
# # selector = RFE(estimator, n_features_to_select=3, step=1)
# selector = estimator.fit(X, y)
#
# scores = cross_val_score(estimator, X, y, cv=5)
# print(scores)
#
# # embedding = {"a": 1, "b": 12}
# # print(len(embedding))

from Article2.Datasets import get_usas_feature
import pandas as pd
nlp = get_usas_feature()


dataset_path = "/Users/jinchenji/Developer/Datasets/healthcare/Article2/main.csv"
save_dir = "/Users/jinchenji/Developer/Datasets/healthcare/Article2/npz_files/train"

csv_data = pd.read_csv(dataset_path)
data_length = len(csv_data)


for idx in range(data_length):
    label = csv_data["Label (1=Mistake present, 0= No mistake)"][idx]
    text = csv_data["Text"][idx]
    doc = nlp(text)
    vec = doc[0]._.pymusas_tags
    print(vec)
    break
    # for i, word in enumerate(doc):
    #     tokens = []
    #     print(word._.pymusas_tags)
    #
    # break