# EV_Stock_Machine_Learning_Predictions
Machine Learning Project to study and make predictions for Electric Vehicle Stocks as a measure for the public perspective on California and EU initiative to phase out internal combustion vehicles by 2035

**Author**: Brian Matsiko

## Overview & Business Problem

![logo](Images/Ev_Future.jpg)
Goal of this project is to analyze the current stock and forecast futures of the four companies.
Evaluate whether the greater world are onboard with the new future of only electric vehicles.


## Data
Stocking trading information was sourced from the yahoo API.
Entire trading history was included in this project


## Background
TSLA is the only company based in North America and the other three companies are based out of China.
TSLA has been trading for 12 years
NIO has traded for 3 years
Both LI and XPEV have only been trading for a year

## Methods

In this project, I worked with historical data about the stock prices of the four publicly listed fully electric vehicle manufacturing companies. I implemented a mix of machine learning algorithms to attempt and predict the future stock price of
the given companies, first starting with Long ShortTerm Memory (LSTM) algorithm and then moving on to
advanced techniques like Auto Regressive Integrated Moving Average (ARIMA) and Facebook prophet.

***

## Results

***
The machine learning process was started with deep learning algorithm LSTM (Long Short Term Memory). The Mean Absolute Error was used as the metric for optimizing this algorithm. 
![LSMT Model Predictions](./Images/LMST_Predictions.jpg)

***
Facebook prophet was then also used and optimized to make predictions on the four EV stocks as well.
![Facebook prophet model predictions](./Images/Facebook_Prophet.jpg)

***
Time series models ARIMA and SARIMA were also used to make predictions. SARIMA provided predictions with the best MAE for all the four EV stocks.
![SARIMA model predictions](./Images/SARIMA_Predictions.jpg)



## Conclusions

This analysis leads to the following recommendations for creating a movie.
1. **General Automotive Stock Market Trend not included.**
The general stock market trend of all the rest of the automotive industry was not included during this machine learning process for the EV specific stocks. The inclusion of this trend would have further helped in the painting a clear picture on whether the trend observed and predicted on the EV stocks was unique to the EV sector.
2. **General Stock Market trend not included.**
The Stock Market trend in general was also not included in this process and hence the predicted trend of the EV stocks was not compared to the rest of the general market.
3. **Previously, all the EV stocks were observed to be in a short term uptrend**
All the EV stocks were orignally observed to be in a short term upward trend though the data was spilt in 70 - 30 proportions to ensure that the short term trend had no impact on the overall predictions.
4. **Indication of short term interest in the all the EV stocks.**
The machine learning process predicted a 42 day upward trend for all the four EV stocks and thus showing that there is currently active interest and investment in the EV specific stocks.


## Next Steps

Further analysis could provide even more insight into a more wholestic and inclusive valuation trend of these four companies:

**General market and industry inclusion.**
Taking into consideration the general trend of the general stock market and the automotive industry as a whole would greatly help with providing a wholestic picture;

**Stock Volume Analysis.**
Deeper analysis of the volume changes within the stock trading patterns of the four EV stocks would provide a deeper understanding of the trading community interest.

**Publishing all inclusive results on the right medium platform**
Results and evaluation of the all-inclusive machine learning processes should be published on a wide audience medium platform with the goal of creating the respective 


## For More Information

Please review our full analysis in [my Notebook folder](./Notebooks) or my [presentation](./final_presentation.pdf).

For any additional questions, please contact **Brian Matsiko matsikobrian@yahoo.com**

## Repository Structure

```
├── README.md                          
├── Notebooks   
├── final_presentation.pdf         
├── Flas                            
└── Images
```

