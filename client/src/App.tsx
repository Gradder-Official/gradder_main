// NPM Imports
import React, { useState, FunctionComponent } from 'react';
import { Switch, BrowserRouter as Router, Route, Redirect } from 'react-router-dom';

// Components
import Login from './pages/Login';
import StudentDash from './pages/StudentDash';
import StudentAssignments from './pages/StudentAssignments';
import StudentTimetable from './pages/StudentTimetable';

// Types and interfaces
import { student } from "./components/Interfaces";

// Stylesheets
import 'bootstrap/dist/css/bootstrap.min.css';

const App: FunctionComponent = () => {
  
  // Fetch user type from API. Below is a dummy.
  const [user] = useState<student>({
    userName: 'Bob',
    userType: 'student',
    loggedIn: true,
  });

  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Login} />
        <Route exact path="/auth/logout" component={Login} /> 
        <Route exact path="/dashboard">
          {user.loggedIn ? <Redirect to={'/' + user.userType + '/dashboard'} /> : <Login />}
        </Route>
        <Route exact path="/student/dashboard" render={(props) => (
          <StudentDash {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn}/> 
        )}/>
        <Route exact path="/student/timetable" render={(props) => (
          <StudentTimetable {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn}/> 
        )}/>
        <Route exact path="/student/assignments" render={(props) => (
          <StudentAssignments {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn}/> 
        )}/>
      </Switch>
    </Router>
  );
};

export default App;