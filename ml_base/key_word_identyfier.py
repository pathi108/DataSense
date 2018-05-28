import distance
import pandas as pd
from sklearn.cluster import KMeans
class KeyWordIdentifier:
    def identify_keywords(self,key_words,headers):
        key_words=[x.lower() for x in key_words]
        headers = [x.lower() for x in headers]
        all_words = []
        all_words.extend(key_words)
        all_words.extend(headers)
        print(all_words)
        featers = []
        for column_word in all_words:
            featuer_dict = {}
            featuer_dict['word'] = column_word
            for word in key_words:
                featuer_dict[word] = distance.nlevenshtein(word, column_word, method=1)
            featers.append(featuer_dict)

        data_frame = pd.DataFrame(featers)
        train_df = data_frame.drop(['word'], axis=1)
        kmeans = KMeans(n_clusters=len(key_words), random_state=0).fit(train_df)
        clusters=kmeans.labels_.tolist()
        duplicates=set([x for x in clusters if clusters.count(x) > 1])

        df=pd.DataFrame({'header':all_words,'cluster':clusters})
        header_pairs=[]
        for duplicate in duplicates:
            header_pairs.append(df['header'][df['cluster']==duplicate])
        return header_pairs