import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import Unauthorized from "../pages/Unauthorized";

const ProtectedRoute = ({ Component, user, scope, render, ...rest }: any) => {
  return (
    <Route {...rest} render={
      (props: any) => {
        if (user.userType === scope) {
          return render(props);
        } else {
          return <Redirect to='/unauthorized' />
        }
      }
    } />
  )
}

export default ProtectedRoute;