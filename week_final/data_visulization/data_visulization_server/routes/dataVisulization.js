var express = require('express');
var router = express.Router();

const bodyParser = require('body-parser');
const jsonParser = bodyParser.json();

//*****node js to call a REST Service */
const nodeRestClient = require('node-rest-client').Client;
const restClient = new nodeRestClient();
const USER_STATISTICS_DATA_URL = 'http://localhost:5000/userStatisticsData';
const USER_TREND_URL = 'http://localhost:5000/userTrend';
const USER_DEVICE_URL = 'http://localhost:5000/userDevice';
const NEWS_CATEGORY_URL = 'http://localhost:5000/newsCategory';
const USER_ACTIVE_TIME_URL = 'http://localhost:5000/userActiveTimeDistribution';


//register remote methods
restClient.registerMethod('user_statistic_data', USER_STATISTICS_DATA_URL, 'GET');
restClient.registerMethod('userTrend', USER_TREND_URL, 'GET');
restClient.registerMethod('userDevice', USER_DEVICE_URL, 'GET');
restClient.registerMethod('newsCategory', NEWS_CATEGORY_URL, 'GET');
restClient.registerMethod('userActiveTimeDistribution', USER_ACTIVE_TIME_URL, 'GET');

/*GET User Total Num, New User, Active User and Average Reading Info */
router.get('/statistic', jsonParser, function(req,res,next){
    console.log("Send user_data from data visulization server");

  //  user_data = null;

    return restClient.methods.user_statistic_data(
        {
            headers: {
                'Content-Type': 'application/json'
            }
        },
        (data, response) => {
            console.log(data);
            res.json(data);
        }
    );

});

/*GET User Trend Data */
router.get('/usertrend', jsonParser, function(req,res,next){
    return restClient.methods.userTrend(
        {
            headers: {
                'Content-Type': 'application/json'
            }
        },
        (data, response) => {
            console.log(data);
            res.json(data);
        }
    );

});

/*GET User Device Data */
router.get('/userdevice', jsonParser, function(req,res,next){
    console.log("Send user_device from data visulization server");
    return restClient.methods.userDevice(
        {
            headers: {
                'Content-Type': 'application/json'
            }
        },
        (data, response) => {
            console.log(data);
            res.json(data);
        }
    );
});

/*GET User news category Data */
router.get('/newscategory', jsonParser, function(req,res,next){ 
    return restClient.methods.newsCategory(
        {
            headers: {
                'Content-Type': 'application/json'
            }
        },
        (data, response) => {
            console.log(data);
            res.json(data);
        }
    );
});

/*GET User active time Data */
router.get('/activetime', jsonParser, function(req,res,next){
    return restClient.methods.userActiveTimeDistribution(
        {
            headers: {
                'Content-Type': 'application/json'
            }
        },
        (data, response) => {
            console.log(data);
            res.json(data);
        }
    );
});

module.exports = router;