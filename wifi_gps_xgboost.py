# coding=utf-8
"""
加入GPS特征

@author: 许铭潮
"""
import pandas as pd
import numpy as np
from sklearn import preprocessing
import xgboost as xgb

# import lightgbm as lgb
path = './DataSet/'
df = pd.read_csv(path + u'trainingdata-ccf_first_round_user_shop_behavior.csv')
shop = pd.read_csv(path + u'trainingdata-ccf_first_round_shop_info.csv')
test = pd.read_csv(path + u'testData-evaluation_public.csv')
df = pd.merge(df, shop[['shop_id', 'mall_id']], how='left', on='shop_id')
df['time_stamp'] = pd.to_datetime(df['time_stamp'])
train = pd.concat([df, test])  # 纵向拼接df

# print(df)
# print(train)

mall_list = list(set(list(shop.mall_id)))
# print(mall_list)

result = pd.DataFrame()
for mall in mall_list:  # 分商场训练
    train1 = train[train.mall_id == mall].reset_index(drop=True)  # 过滤掉非当前商场的样本
    # print(train1)   
    l = []
    wifi_dict = {}  # 记录在当前mall中某个wifi出现的次数
    for index, row in train1.iterrows():
        # print(row)
        wifi_list = [wifi.split('|') for wifi in row['wifi_infos'].split(
            ';')]  # 递推式，最外面要加[]，输出:[['b_1104622', '-64', 'false'],..., ['b_39379174', '-64', 'false']]
        # print(wifi_list)
        for i in wifi_list:
            row[i[0]] = int(i[1])  # 直接在某个样本后面添加字典，wifi名称-强度
            if i[0] not in wifi_dict:
                wifi_dict[i[0]] = 1
            else:
                wifi_dict[i[0]] += 1
        l.append(row)
    delate_wifi = []
    for i in wifi_dict:  # 出现次数过少的wifi就不考虑了
        if wifi_dict[i] < 20:
            delate_wifi.append(i)
    m = []
    for row in l:
        new = {}
        for n in row.keys():
            if n not in delate_wifi:
                new[n] = row[n]
        m.append(new)
    # print(m)
    train1 = pd.DataFrame(m)
    # print(train1)
    df_train = train1[train1.shop_id.notnull()]
    df_test = train1[train1.shop_id.isnull()]
    # 对标签编码，非数值型转化成数值型
    lbl = preprocessing.LabelEncoder()
    lbl.fit(list(df_train['shop_id'].values))
    df_train['label'] = lbl.transform(list(df_train['shop_id'].values))
    # print(df_train)

    # 准备xgboost参数
    num_class = df_train['label'].max() + 1  # 每个商场的店铺数，即类别数
    # print(num_class)
    params = {
        'objective': 'multi:softmax',
        'eta': 0.1,
        'max_depth': 8,
        'eval_metric': 'merror',
        'seed': 0,
        'missing': -999,
        'num_class': num_class,
        'silent': 1
    }
    features = [x for x in train1.columns if
                x not in ['user_id', 'label', 'shop_id', 'time_stamp', 'mall_id', 'wifi_infos', 'row_id']]

    # wifi计算特征权重，出现次数越少的wifi权重越大
    # weight_list = []
    # for feature in features:
    # 	if feature in wifi_dict:
    # 		weight_list.append(20.0/wifi_dict[feature]+1)
    # weight_list += [2,2,0]	#A再加上经度，维度，row_id的权重

    print(df_train[features][1])

    # xgboost训练
    xgbtrain = xgb.DMatrix(df_train[features], df_train['label'])
    # print(features)
    xgbtest = xgb.DMatrix(df_test[features])
    watchlist = [(xgbtrain, 'train'), (xgbtrain, 'test')]
    num_rounds = 60
    model = xgb.train(params, xgbtrain, num_rounds, watchlist, early_stopping_rounds=15)

    print(min(model.predict(xgbtest, pred_contribs=True)[:, -1]))
    df_test['label'] = model.predict(xgbtest)
    df_test['shop_id'] = df_test['label'].apply(lambda x: lbl.inverse_transform(int(x)))  # 将lbl转换后的shop_id加入到df的最后一列
    result_per_mall = df_test[['row_id', 'shop_id']]
    result = pd.concat([result, result_per_mall])
    # 写入文件
    result['row_id'] = result['row_id'].astype('int')
    result.to_csv(path + 'result_20171104_mlogloss.csv', index=False)

# break
