# week13
我要每小时的用户点击量 number类型。
近七天每天新增 和 活跃用户数 number类型。不同类型新闻的点击数量。不同登录设备的数量。需要转换成百分比


1. 每小时点击量
1. hour_clicking_number
	redis 
	[0-23]_hour_clicking_number
	backend: when a request from front end, add 
	[0-23]_hour_clicking_number by 1

	maintain: 1 hours, dump to mongo day_clicking_number 

	rest api: 

	dashboard: get data from redis

2. 当天活跃用户数量
2. daily_active_user_num
	redis
	[2017_09_25]_freq_username ++ expire 2 day
 
3. 近七天每天活跃用户量
3. past_one_week_active_user
 
4. 近七天每天新增用户量
4. past_one_week_signin

5. 每天不同新闻类型点击量
5. daily_news_categories_clicking_num
6. total_news_categories_clicking_num
 
6. 每天设备百分比
6. daily_device_categories_precentage
 
5，6不用每天 累计就行 

7.累计用户数
7. total_user_num

8. 平均使用时间（option）
8. average_using_time

### QA