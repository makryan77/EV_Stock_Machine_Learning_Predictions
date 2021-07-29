# EV_Stock_Machine_Learning_Predictions
Machine Learning Project to study and make predictions for Electric Vehicle Stocks as a measure for the public perspective on California and EU initiative to phase out internal combustion vehicles by 2035

**Author**: Brian Matsiko

## Overview & Business Problem

![logo](images/logo.jpeg)
Goal of this project is to analyze the current stock and forecast futures of the four companies.
Evaluate whether the greater world are onboard with the new future of only electric vehicles.

***
* How much money to budget for the movie
* A look at the top competitors
* Which director to choose
* When to release the movie
* How long to make the movie
***

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
Consider a larger budget for the movie production. This tends to lead towards higher revenue and profits.
![Budget](./images/budget_profit_revenue.png)

***
Make reference to major competitor work (Walt Disney and Warner Bros studios) who statistically generate the most average and total revenue per movie
![Top Studios](./images/top_studios_revenue.png)

***
Consider working with the highest rated Directors.

| Director           | Average Rating|
| -------------      |:-------------:| 
| Christopher Nolan  |8.455479       | 
| Lee Unkrich        |8.349254       | 
| Joe Russo          |8.198621       |
| S.S. Rajamouli     |8.193333       | 
| Asif Kapadia       |8.148718       | 


***
Consider releasing movies at the beginning of May as the three most profitable months are May, June and July
![Average Profit per Month Since 2010](./images/profit_per_month.png)
![Most profitable Movies for May, June & July](./images/most_profitable_movies.png)

***
Consider making the movie longer rather than shorter

![graph1](./images/rating_runtime_minutes.png)

***


## Conclusions

This analysis leads to the following recommendations for creating a movie.
1. **Spend more money to make more money.**
There is a positive corrrelation with how much money is budgeted for a film and how much revenue and profit the film will make. Spending more money on the film usually generates more revenue and profit. If you look at the top 5 most profitable movies released in May since 2010, they had an average budget of around $223 million. These were all movies in one of our highest rated genres, Action,Adventure,Sci-Fi.
2. **Understand your competitors (Walt Disney and Warner Bros) who generate the most revenue per movie.**
These studios have the highest average grossing revenue for those studios who have made over 100 movies. During May, which is the most profitable month of the year, Walt Disney distributed the top 5 highest profitable movies while Warner Brothers distributed top movies by profit in June and July, the 2nd and 3rd highest average profit months respectively.
3. **Engage with the top directors (Christopher Nolan and Joe Russo)**
These top directors have the highest everage rating for movies with more than 30,000 votes in IMDb. Joe Russo and Christopher Nolan directed two of the most profitable films, Captain America: Civil War, and The Dark Knight Rises. They both also direct films in one of the highest rated genres, which is Action,Adventure,Sci-Fi. In addition, they also direct movies for your competitors, Walt Disney and Warner Bros.
4. **Consider releasing during May which is the month that generates the most profit.**
It makes the most sense to release your film during May. May, June and July are the most profitable months of the year. The top 5 most profitable movies in May over the last 10 years were distributed by Walt Disney and profited over $500 million combined.
5. **Consider making your movie longer, rather than shorter.**
The average ratings of movies tend to increase as the length of the movie increases. Our analysis shows the most positive incerease in ratings for movies in the Action, Advneture, Sci-Fi genre up to 200 minute movies.

## Next Steps

Further analysis could provide even more insight into a more wholestic and inclusive valuation trend of these four companies:

**General market and industry inclusion.**
Taking into consideration the general trend of the general stock market and the automotive industry as a whole would greatly help with providing a wholesticndfblk;

**Better qualitative analysis on why studios, writers, directors, actors/actresses, would want to work with Microsoft.**
Maybe there are certain things they look for from the company producing the film other than money. This could be done by surveys to individual writers/directors/actors.

**Better idea of studio culture, the benefits of other studios and how they treat there employees and operate the business.**
We could look at what HR benefits the studio offers, compensation, community events. Do they have a "feelings Friday?"


## For More Information

Please review our full analysis in [my Notebook folder](./Notebooks) or my [presentation](./final_presentation.pdf).

For any additional questions, please contact **Brian Matsiko matsikobrian@yahoo.com**

## Repository Structure

```
├── README.md                          
├── final_notebook.ipynb   
├── final_presentation.pdf         
├── Data                            
└── Images
```

