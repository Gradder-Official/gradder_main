import React, { FunctionComponent } from 'react';
import LoginBox from '../components/LoginBox';
import WhiteLogo from '../assets/images/white-logo.png'
import "../assets/styles/login.css"

const Login: FunctionComponent = () => {
  return (
    <div className="login-page">
      <div className="login-background">
        <img src={ WhiteLogo } alt="Gradder" className="login-logo"/>
      </div>
      <LoginBox/>
    </div>
  );
};

export default Login;