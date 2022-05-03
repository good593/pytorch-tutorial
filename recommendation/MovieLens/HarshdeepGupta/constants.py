import enum

class PATH_INFO(enum.Enum):
  input_u_data = (enum.auto(), '../../data/MovieLens/ml-100k/u.data', ['userID', 'movieID', 'rating', 'timestamp'])
  output_train = (enum.auto(), './Data/movielens.train.rating')
  output_test = (enum.auto(), './Data/movielens.test.rating')


