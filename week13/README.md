# week13

## From the view of API calling:
When api want to access the data, First check it is on redis; if not existed, poll them from mongodb to redis, return data from access. So, we just read data directly from redis by considering one data source and frequently access.
## From the view of Dashboard:
It implements how to display different charts by using highchart.

## Implementation
1. Clicking number per hour
Hour_clicking_number
Redis: key: [0-23]_hour_clicking_number
 Value: number
Mongo: tapnews[“day_clicking_number”]

Update redis every request in backend.
Update mongodb 60 seconds by a new thread.

2. Daily number of active user
daily_active_user_num
Redis: <[2017_09_25]_daily_active_user_num, int>
Helper: Update redis every request in backend. 
<[2017_09_25]_freq_active_user_num, val ++>
Update mongo one hours for backup.
Helper is store freq of username and times of clicking

3. Past one week number of active user
Past_one_week_active_user
Redis: <[2017_09_25 - i]_daily_active_user_num, int> i in range(0, 6)

4. The number of past one week new users
Past_one_week_signin
Redis <[2017_09_25 - i]_daily_new_user_num, int> i in range(0, 6)

5. The number of certain category
<Total_news_categories_clicking_num, int>
 Daily_news_categories_clicking_num
Redis: <[2017_09_25_category_technology, int>
 

6. Total device num in certain device
Redis: <device_categories_num_2017_09, int>
<"", int>
Get info from user agent

7.total user number
total_user_num


# View of Visualization

1. 

## data
set hour_clicking_number_2017-09-29-08_ 200
set hour_clicking_number_2017-09-29-09_ 500
set hour_clicking_number_2017-09-29-10_ 200
set hour_clicking_number_2017-09-29-11_ 600
set hour_clicking_number_2017-09-29-12_ 1000
set hour_clicking_number_2017-09-29-13_ 800

set hour_clicking_number_2017-09-29-14_ 200
set hour_clicking_number_2017-09-29-15_ 100
set hour_clicking_number_2017-09-29-16_ 600



## Ref
https://stackoverflow.com/questions/37980655/why-is-python-datetime-time-delta-not-found

https://stackoverflow.com/questions/3895434/how-to-get-information-about-the-client-in-node-js