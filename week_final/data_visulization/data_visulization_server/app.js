var bodyParser = require('body-parser');
var express = require('express');
var index = require('./routes/index');
var user_data = require('./routes/dataVisulization');
var path = require('path');

//var cors = require('cors');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, '../client/build'));
//app.set('views', path.join(__dirname, 'views'));
app.use('/static', express.static(path.join(__dirname, '../client/build/static/')));

app.all('*', function(req,res,next){
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "X-Requested-with");
  next();
});

// app.use(cors());
// all request convert into json
app.use(bodyParser.json());

app.use('/', index);
app.use('/userdata',user_data);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  res.send('404 not found');
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
