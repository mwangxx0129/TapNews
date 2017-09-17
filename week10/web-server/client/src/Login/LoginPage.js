import React, {PropTypes} from 'react';
import Auth from '../Auth/Auth';

import LoginForm from './LoginForm';

class LoginPage extends React.Component {
  constructor(props, context) {
    super(props, context);

    // set the initial component state
    this.state = {
      errors: {},
      user: {
        email: '',
        password: ''
      }
    };

    this.processForm = this.processForm.bind(this);
    this.changeUser = this.changeUser.bind(this);
  }

  // Pre-submission.
  processForm(event) {
    event.preventDefault();

    const email = this.state.user.email;
    const password = this.state.user.password;

    // Post login data.
    fetch('http://localhost:3000/auth/login', {
      method: 'POST',
      cache: false,
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: email,
        password: password
      })
    }).then(response => {
      if (response.status === 200) {
        this.setState({
          errors: {}
        });

        response.json().then(function(json) {
          console.log(json);
          Auth.authenticateUser(json.token, email);
          this.context.router.replace('/');
        }.bind(this));
      } else {
        console.log('Login failed');
        response.json().then(function(json) {
          const errors = json.errors ? json.errors : {};
          errors.summary = json.message;
          this.setState({errors});
        }.bind(this));
      }
    });
  }

  changeUser(event) {
    const field = event.target.name;
    const user = this.state.user;
    user[field] = event.target.value;
    // user['email'] = '123@123.com'
    // user['password'] = '12345678'

    this.setState({ user });
  }

  render() {
    return (
      <LoginForm
        onSubmit={this.processForm}
        onChange={this.changeUser}
        errors={this.state.errors}
        user={this.state.user}
      />
    );
  }
}

// To make react-router work
LoginPage.contextTypes = {
  router: PropTypes.object.isRequired
};

export default LoginPage;