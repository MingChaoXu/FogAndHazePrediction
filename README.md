![](https://github.com/MingChaoXu/Fog_And_Haze_Prediction/tree/master/docs/logo.png)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/MingChaoXu/Fog_And_Haze_Prediction/blob/master/LICENSE) 
![Build Status](https://img.shields.io/appveyor/ci/gruntjs/grunt/master.svg)
# Fog_And_Haze_Prediction
> predict the PM2.5 value
# Environment
* 1.Python v3.6 
* 2.Python packages: pandas, xgboost, matplotlib, xlrd, csv

# Getting Started
* 1.Clone this project : `git clone https://github.com/MingChaoXu/Fog_And_Haze_Prediction.git`
* 2.Enter the folder Fog_And_Haze_Prediction : `cd Fog_And_Haze_Prediction`
* 3.get dataset : 
```
$ cd utils
$ python dataset.py
```
* 3.Run the file main.py : 
```
$ cd ..
$ python main.py
```
# sample
![result](https://github.com/MingChaoXu/Fog_And_Haze_Prediction/blob/master/result.png)
red: prediction
blue: target