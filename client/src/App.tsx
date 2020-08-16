// NPM Imports
import React, { useState, useEffect, FunctionComponent } from "react";
import {
  Switch,
  BrowserRouter as Router,
  Route,
  Redirect,
} from "react-router-dom";

// Components
import Login from './pages/Login';
import StudentDash from './pages/Student/Dash';
import StudentAssignments from './pages/Student/Assignments';
import AssignmentDisplay from './pages/Student/AssignmentDisplay';
import StudentTimetable from './pages/Student/Timetable';
import TeacherTimetable from "./pages/Teacher/Timetable"
import StudentProfile from './pages/Student/Profile';
import Unauthorized from './pages/Unauthorized';
import ProtectedRoute from './components/ProtectedRoute'

// Types and interfaces
import { student, teacher } from "./components/Interfaces";

// Stylesheets
import "bootstrap/dist/css/bootstrap.min.css";
import TeacherDash from "./pages/Teacher/Dash";
import TeacherCourses from "./pages/Teacher/Courses";


const App: FunctionComponent = () => {

  const blankUser: student | teacher = {
    userName: '',
    userType: '',
    loggedIn: false,
    dob: '',
  }

  const [user, setUser] = useState<student | teacher>(blankUser);

  useEffect(() => {
    fetch('/api/auth/login')
      .then(res => res.json()).then(response => {
        setUser(response['user_info']);
      }
      )
    // Cleanup and reset
    return function cleanup() {
      setUser(blankUser);
    };
  }, []);

  console.log(user);

  function logOutUser() {
    setUser(blankUser);
    console.log(user);
  }

  return (
    <Router>
      <Switch>
        <Route exact path="/">
          {user.loggedIn ? (
            <Redirect to={"/" + user.userType + "/dashboard"} />
            ) : (
              <Login />
          )}
        </Route>
        <Route exact path="/auth/logout" render={() => {
          logOutUser();
          return <Login />;
        }
        } />
        <Route exact path="/dashboard">
          {user.loggedIn ? (
            <Redirect to={"/" + user.userType + "/dashboard"} />
            ) : (
            <Login />
          )}
        </Route>
        <ProtectedRoute user={user} scope="Student" exact path="/student/dashboard" render={(props: any) => (
          <StudentDash {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob} />
        )} />
        <ProtectedRoute user={user} scope="Student" exact path="/student/timetable" render={(props: any) => (
          <StudentTimetable {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob} />
        )} />
        <ProtectedRoute user={user} scope="Student" exact path="/student/assignments" render={(props: any) => (
          <StudentAssignments {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob} />
        )} />
        <ProtectedRoute user={user} scope="Student" exact path="/student/profile" render={(props: any) => (
          <StudentProfile {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob} />
        )} />
        <ProtectedRoute user={user} scope="Teacher" exact path="/teacher/dashboard" render={(props: any) => (
          <TeacherDash {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob} />
        )} />
        <ProtectedRoute user={user} scope="Teacher" exact path="/teacher/classes" render={(props: any) => (
          <TeacherCourses {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob} />
        )} />
        <ProtectedRoute user={user} scope="Teacher" exact path="/teacher/timetable" render={(props: any) => (
          <TeacherTimetable {...props} userName={user.userName} userType={user.userType} loggedIn={user.loggedIn} dob={user.dob} />
        )} />
        
        <Route
          exact
          path="/student/assignment/:id"
          render={(props) => (
            <AssignmentDisplay
              {...props}
            />
          )}
        />
        <Route exact path="/unauthorized" render={(props: any) => (
          <Unauthorized {...props} />
        )} />
      </Switch>
    </Router>
  );
};

export default App;
