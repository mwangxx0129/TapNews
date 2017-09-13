var express = require('express');
var router = express.Router();

/* GET news summary list. */
router.get('/', function(req, res, next) {
  news = [
        {'url':'http://us.cnn.com/2017/02/15/politics/andrew-puzder-failed-nomination/index.html',
         'title':"Inside Andrew Puzder's failed nomination",
         'description':"In the end, Andrew Puzder had too much baggage -- both personal and professional -- to be confirmed as President Donald Trump's Cabinet.",
         'source':'cnn',
         'urlToImage':'http://i2.cdn.cnn.com/cnnnext/dam/assets/170215162504-puzder-trump-file-super-tease.jpg',
         'digest':"3RjuEomJo26O1syZbU7OHA==\n",
         'reason':"Recommend"
        },
        {'title': 'Zero Motorcycles CTO Abe Askenazi on the future of two-wheeled EVs',
         'description': "Electric cars and buses have already begun to take over the world, but the motorcycle industry has been much slower to put out all-electric and hybrid models...",
         'url': "https://techcrunch.com/2017/03/23/zero-motorcycles-cto-abe-askenazi-on-the-future-of-two-wheeled-evs/",
         'urlToImage': "https://tctechcrunch2011.files.wordpress.com/2017/03/screen-shot-2017-03-23-at-14-04-01.png?w=764&h=400&crop=1",
         'source': 'techcrunch',
         'digest':"3RjuEomJo26O1syZbUdOHA==\n",
         'time':"Today",
         'reason':"Hot"
        }
        ];
  res.json(news);

});

module.exports = router;