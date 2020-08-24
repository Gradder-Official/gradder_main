// NPM Imports
import React, { useState, FunctionComponent } from 'react';
import { Switch, BrowserRouter as Router, Route, Redirect } from 'react-router-dom';

// Components
import Login from './pages/Login';
import TeacherDash from './pages/TeacherDash';
import TeacherAssignments from './pages/TeacherAssignments';
import TeacherTimetable from './pages/TeacherTimetable';
import TeacherProfile from './pages/TeacherProfile';

import StudentDash from './pages/StudentDash';
import StudentAssignments from './pages/StudentAssignments';
import StudentTimetable from './pages/StudentTimetable';
import StudentProfile from './pages/StudentProfile';
// Types and interfaces
import { teacher } from "./components/Interfaces";

// Stylesheets
import 'bootstrap/dist/css/bootstrap.min.css';

const App: FunctionComponent = () => {
  
  // Fetch user type from API. Below is a dummy.
  const [user] = useState<teacher>({
    userName: 'Stephen King',
    userType: 'teacher',
    loggedIn: true,
    dob: '1973-05-10',
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
          <StudentDash {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob}/> 
        )}/>
        <Route exact path="/student/timetable" render={(props) => (
          <StudentTimetable {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob}/> 
        )}/>
        <Route exact path="/student/assignments" render={(props) => (
          <StudentAssignments {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob}/> 
        )}/>
        <Route exact path="/student/profile" render={(props) => (
          <StudentProfile {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob} />
        )}/>
        <Route exact path="/teacher/dashboard" render={(props) => (
          <TeacherDash {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob}/> 
        )}/>
        <Route exact path="/teacher/timetable" render={(props) => (
          <TeacherTimetable {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob}/> 
        )}/>
        <Route exact path="/teacher/assignments" render={(props) => (
          <TeacherAssignments {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob}/> 
        )}/>
        <Route exact path="/teacher/profile" render={(props) => (
          <TeacherProfile {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob} />
        )}/>
      </Switch>
    </Router>
  );
};

export default App;