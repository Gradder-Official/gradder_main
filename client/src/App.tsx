// NPM Imports
import React, { useState, FunctionComponent } from "react";
import {
  Switch,
  BrowserRouter as Router,
  Route,
  Redirect,
} from "react-router-dom";

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
<<<<<<< HEAD
import Unauthorized from './pages/Unauthorized';
import ProtectedRoute from './components/ProtectedRoute'

=======
>>>>>>> 4021de8ba5042d7eeb0233b8e41cc91d4b19a4d5
// Types and interfaces
import { teacher } from "./components/Interfaces";

// Stylesheets
import "bootstrap/dist/css/bootstrap.min.css";


const App: FunctionComponent = () => {
<<<<<<< HEAD

  const [user, setUser] = useState<student>({
    userName: '',
    userType: '',
    loggedIn: false,
    dob: '',
  });

  // Pre-filled dummy info
  const dummyUser: student = {
    userName: 'Bob Jones',
    userType: 'student',
    loggedIn: true,
    dob: '2003-01-08',
  }

  // TODO: set logged in status to true
  useEffect(() => {
    fetch('/api/auth/login').
      then(res => res.json()).then(response => {
        if (response['user_info']) {
          setUser(response['user_info']);
        }
        setUser(dummyUser);
      }
    )
    console.log(user);
  }, []);
=======
  
  // Fetch user type from API. Below is a dummy.
  const [user] = useState<teacher>({
    userName: 'Stephen King',
    userType: 'teacher',
    loggedIn: true,
    dob: '1973-05-10',
  });
>>>>>>> 4021de8ba5042d7eeb0233b8e41cc91d4b19a4d5

  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Login} />
        <Route exact path="/auth/logout" component={Login} />
        <Route exact path="/dashboard">
          {user.loggedIn ? (
            <Redirect to={"/" + user.userType + "/dashboard"} />
          ) : (
            <Login />
          )}
        </Route>
        <ProtectedRoute user={user} scope="student" exact path="/student/dashboard" render={(props: any) => (
          <StudentDash {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob}/> 
        )}/>
        <ProtectedRoute user={user} scope="student" exact path="/student/timetable" render={(props: any) => (
          <StudentTimetable {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob}/> 
        )}/>
        <ProtectedRoute user={user} scope="student" exact path="/student/assignments" render={(props: any) => (
          <StudentAssignments {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob}/> 
        )}/>
        <ProtectedRoute user={user} scope="student" exact path="/student/profile" render={(props: any) => (
          <StudentProfile {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob} />
        )}/>
<<<<<<< HEAD
        <Route exact path="/unauthorized" render={(props: any) => (
          <Unauthorized {...props}/>
=======
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
>>>>>>> 4021de8ba5042d7eeb0233b8e41cc91d4b19a4d5
        )}/>
      </Switch>
    </Router>
  );
};

export default App;
