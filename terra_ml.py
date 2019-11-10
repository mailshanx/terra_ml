from surprise import SVD
from surprise import Dataset
from surprise import accuracy
from surprise.model_selection import train_test_split
import pickle

def train_benchmark():
    # Load the movielens-100k dataset (download it if needed),
    data = Dataset.load_builtin('ml-100k')

    # sample random trainset and testset
    # test set is made of 25% of the ratings.
    trainset, testset = train_test_split(data, test_size=.25)

    # We'll use the famous SVD algorithm.
    algo = SVD()

    # Train the algorithm on the trainset, and predict ratings for the testset
    algo.fit(trainset)

    #print benchmark:
    predictions = algo.test(testset)
    print(accuracy.rmse(predictions))

    algo_filename = 'rec_algo.pkl'
    testset_filename = 'testset.pkl'
    with open(algo_filename, 'wb') as f:
        print("saving model to disk")
        pickle.dump(algo, f)

    with open(testset_filename, 'wb') as f:
        print("saving testset to disk")
        pickle.dump(testset, f)


if __name__=='__main__':
    train_benchmark()





