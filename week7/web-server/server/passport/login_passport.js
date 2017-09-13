const jwt = require('jsonwebtoken');
const User = require('mongoose').model('User');
const PassportLocalStrategy = require('passport-local').Strategy;
const config = require('../config/config.json');

module.exports = new PassportLocalStrategy({
  usernameField: 'email',
  passwordField: 'password',
  session: false,
  passReqToCallback: true
}, (req, email, password, done) => {
  const userData = {
    email: email.trim(),
    password: password
  };

  // find a user by email address
  return User.findOne({ email: userData.email }, (err, user) => {
    if (err) { return done(err); }

    if (!user) {
      const error = new Error("Incorrect email or password.");
      error.name = "IncorrectCredentialsError";

      return done(error);
    }

    // check user's password
    return user.comparePassword(userData.password, (passwordErr, isMatch) => {
      if (err) { return done(err); }

      if (!isMatch) {
        const error = new Error("Incorrect email or password.");
        error.name = "IncorrectCredentialsError";
        return done(error);
      }

      const payload = {
        sub: user._id
      }

      const token = jwt.sign(payload, config.jwtSecret);
      const data = {
        name: user.email
      };

      return done(null, token, data);
    });
  });
});