var jayson = require('jayson');

// Create a client connected to backend server
var client = jayson.client.http({
  port: 4040,
  hostname: 'localhost'
});

// Test RPC method
function add(a, b, callback) {
  client.request('add', [a, b], function(err, error, response) {
    if (err) throw err;
    console.log(response);
    callback(response);
  });
}

// Get news summaries for a user
function getNewsSummariesForUser(user_id, page_num, callback) {
  client.request('getNewsSummariesForUser', [user_id, page_num], function(err, error, response) {
    if (err) throw err;
    console.log(response);
    callback(response);
  });
}

// Log a news click event for a user
function logNewsClickForUser(user_id, news_id, user_agent, news_category) {
  client.request('logNewsClickForUser', [user_id, news_id, user_agent, news_category], function(err, error, response) {
    console.log('==========rpc_client/logNewsClickForUser=================');
    console.log('user_id: %s\n news_id: %s\n user_agent: %s\n news_category: %s\n', user_id , news_id, user_agent, news_category);
    if (err) throw err;
    // console.log(response);
  });
}

module.exports = {
  add : add,
  getNewsSummariesForUser : getNewsSummariesForUser,
  logNewsClickForUser : logNewsClickForUser
};