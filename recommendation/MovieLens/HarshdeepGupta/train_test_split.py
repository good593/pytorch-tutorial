# Author: Harshdeep Gupta
# Date: 07 September, 2018
# Description: Splits the data into train and test using the leave the latest one out strategy 


import pandas as pd
import numpy as np
from utils import save_to_csv
from constants import PATH_INFO


def __get_train_test_df(transactions:pd.DataFrame):
  '''
  return train and test dataframe, with leave the latest one out strategy
  Args:
    transactions: the entire df of user/item transactions
  '''

  print("Size of the entire dataset:{}".format(transactions.shape))
  transactions.sort_values(by = ['timestamp'], inplace = True)
  # duplicated: 중복값 확인 및 처리
  last_transaction_mask = transactions.duplicated(subset = {'userID'}, keep = "last")
  # The last transaction mask has all the latest items of people
  # We want for the test dataset, items marked with a False
  train_df = transactions[last_transaction_mask]
  test_df = transactions[~last_transaction_mask]
  
  train_df.sort_values(by=["userID", 'timestamp'], inplace = True)
  test_df.sort_values(by=["userID", 'timestamp'], inplace = True)
  return train_df, test_df
    

def __report_stats(transactions:pd.DataFrame, train_df:pd.DataFrame, test_df:pd.DataFrame):
  whole_size = transactions.shape[0]*1.0
  train_size = train_df.shape[0]
  test_size = test_df.shape[0]
  print("Total No. of Records = {}".format(whole_size))
  print("Train size = {}, Test size = {}".format(train_size, test_size))
  print("Train % = {}, Test % ={}".format(train_size/whole_size, test_size/whole_size))


def main():

  transactions = pd.read_csv(PATH_INFO.input_u_data.value[1], sep="\t", names = PATH_INFO.input_u_data.value[2], engine = 'python')
  # print(transactions.head())
  print(f'transactions.shape: {transactions.shape}')
  print(f'transactions[userID].nunique(): {transactions["userID"].nunique()}')

  # convert to implicit scenario
  transactions['rating'] = 1
  
  # make the dataset
  train_df, test_df = __get_train_test_df(transactions)
  print(f'train_df.shape: {train_df.shape}')
  save_to_csv(train_df, PATH_INFO.output_train.value[1], header = False,index = False, verbose = True)
  print(f'test_df.shape: {test_df.shape}')
  save_to_csv(test_df, PATH_INFO.output_test.value[1],header = False,index = False, verbose = True)
  __report_stats(transactions, train_df, test_df)




# if __name__ == "__main__":
#     main()

