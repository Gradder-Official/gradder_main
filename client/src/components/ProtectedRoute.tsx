import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import Unauthorized from "../pages/Unauthorized";

const ProtectedRoute = ({ Component, userType, scope, render, ...rest }: any) => {
  return (
    <Route {...rest} render={
      (props: any) => {
        if (userType.toLowerCase() === scope.toLowerCase()) {
          console.log(userType.toLowerCase(), " matches ", scope.toLowerCase())
          return render(props);
        } else {
          console.log(userType.toLowerCase(), " does not match ", scope.toLowerCase())
          return <Redirect to='/unauthorized' />
        }
      }
    } />
  )
}

export default ProtectedRoute;