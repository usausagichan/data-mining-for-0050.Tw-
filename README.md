# data-mining-for-0050.Tw-
scrape the portfolio data of 0050.TW from https://mops.twse.com.tw/mops/web/t78sb04_q2

1. you should install requests, pandas, numpy package in your python execution environment first. 
2. the get_cat() function help you to get the first table in https://mops.twse.com.tw/mops/web/t78sb04_q2,
  which is the 0050.TW portfolio, and it rerurns a panda dataframe.
3. the get_hist() and p_to_float() functions help us to convert string type object for ‘持股比率’ and '持股比率.1' column
  into integer type object. It will make the building dashboard job much easier. Besides, the function help us add the 
  category of ‘現金’ in 0050.TW which is not shown in https://mops.twse.com.tw/mops/web/t78sb04_q2.
4. In the main execution part, all we have down is first build a dataframe include the 2022(Q3) data called 'his' and 
  append the data of Q3 for past few years in for loop. Finally the his dataframe will include Q3 data from 111-96 (ROC years)
  and be transformed into excel files(xlsx file) and save in your location.
  you may modify the code line 44,46,47 and change the year and season to your advantage.

I use these data to build a dashboard for visualizing mainstream industry and company in Taiwan.
