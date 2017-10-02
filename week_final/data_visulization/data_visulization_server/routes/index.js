var express = require('express');
var router = express.Router();
var path = require('path');

/* GET home page. */
router.get('/', function(req, res, next) {
    console.log("data visulization--- server routes");
    res.sendfile('index.html', {root: path.join(__dirname, '../../data_visuilzation/build')});
});

module.exports = router;
