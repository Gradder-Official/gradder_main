// NPM Imports
import React, { useState, FunctionComponent } from 'react';
import { Switch, BrowserRouter as Router, Route, Redirect } from 'react-router-dom';

// Components
import Lander from './pages/Lander';
import Login from './pages/Login';
import Register from './pages/Register';
import StudentDash from './pages/student/StudentDash';
import TeacherDash from './pages/teacher/TeacherDash';
import AdminDash from './pages/admin/AdminDash';
import ParentDash from './pages/parent/ParentDash';
import Profile from "./pages/Profile";

// Types and interfaces
import { student } from "./components/ProfileContent";

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
        <Route exact path="/" component={Lander} />
        <Route exact path="/auth/login" component={Login} />
        <Route exact path="/auth/logout" component={Login} />
        <Route exact path="/auth/register" component={Register} />
        <Route exact path="/dashboard">
          {user.loggedIn ? <Redirect to={'/' + user.userType + '/dashboard'} /> : <Login />}
        </Route>
        <Route exact path="/student/dashboard" render={(props) => (
          <StudentDash {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn}/> 
        )}/>
        <Route exact path="/teacher/dashboard" render={(props) => (
          <TeacherDash {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn}/> 
        )}/>
        <Route exact path="/parent/dashboard" render={(props) => (
          <ParentDash {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn}/> 
        )}/>
        <Route exact path="/admin/dashboard" render={(props) => (
          <AdminDash {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn}/> 
        )}/>
        <Route exact path="/profile" render={(props) => (
          <Profile {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn}/> 
        )}/>
      </Switch>
    </Router>
  );
};

export default App;
