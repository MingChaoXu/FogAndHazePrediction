# coding=utf-8
"""
@author: 许铭潮
"""
import pandas as pd
import numpy as np
from sklearn import preprocessing
import xgboost as xgb
import matplotlib.pyplot as plt

path = u'./data/'
train_data = pd.read_csv(path + u'train.csv')
test_data = pd.read_csv(path + u'test.csv')
train_data.rename(columns={'PM2.5': 'label'}, inplace=True)
test_data.rename(columns={'PM2.5': 'label'}, inplace=True)
# print(test_data)


def main():
    features = [x for x in train_data.columns if x not in ['id', '质量等级', 'label']]
    # print(train_data[features])
    # print(train_data['label'])

    # XGBoost
    # params = {
    #     'objective': 'reg:linear',
    #     'eta': 0.1,
    #     'max_depth': 8,
    #     'eval_metric': 'rmse',
    #     'seed': 0,
    #     'missing': -999,
    #     'silent': 1
    # }
    # xgbtrain = xgb.DMatrix(train_data[features], label=train_data['label'])
    # xgbtest = xgb.DMatrix(test_data[features])
    # watchlist = [(xgbtrain, 'train'), (xgbtest, 'test')]
    # num_rounds = 60
    # model = xgb.train(params, xgbtrain, num_rounds, watchlist, early_stopping_rounds=15)
    # print(model.predict(xgbtest, pred_contribs=True))

    gbm = xgb.XGBRegressor().fit(train_data[features], train_data['label'])
    predictions = gbm.predict(test_data[features])
    actuals = test_data['label']
    print(predictions)
    # 画图

    x = range(len(predictions))
    plt.plot(x, predictions,color='red')
    plt.plot(x, actuals, color='blue')
    plt.show()

if __name__ == '__main__':
    main()
