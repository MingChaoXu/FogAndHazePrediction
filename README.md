<div align=center><img width="300" height="150" src="https://github.com/MingChaoXu/Fog_And_Haze_Prediction/blob/master/docs/logo.png"/></div>

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
<div align=center><img width="500" height="350" src="https://github.com/MingChaoXu/Fog_And_Haze_Prediction/blob/master/result.png"/></div>
red: prediction
blue: target
