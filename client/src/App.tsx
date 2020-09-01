/** @format */

// NPM Imports
import React, {
  useState,
  useEffect,
  FunctionComponent,
  useReducer,
} from "react";
import {
  Switch,
  BrowserRouter as Router,
  Route,
  Redirect,
} from "react-router-dom";

// Components


import TeacherDash from './pages/TeacherDash';
import TeacherAssignments from './pages/TeacherAssignments';
import TeacherTimetable from './pages/TeacherTimetable';
import TeacherProfile from './pages/TeacherProfile';

import Login from "./pages/Login";
import StudentDash from "./pages/Student/Dash";
import StudentAssignments from "./pages/Student/Assignments";
import AssignmentDisplay from "./pages/Student/AssignmentDisplay";
import StudentTimetable from "./pages/Student/Timetable";
import StudentProfile from "./pages/Student/Profile";
import Unauthorized from "./pages/Unauthorized";
import ProtectedRoute from "./components/ProtectedRoute";

// Types and interfaces
import { teacher } from "./components/Interfaces";

// Stylesheets
import "bootstrap/dist/css/bootstrap.min.css";

const App: FunctionComponent = () => {
  const [requestErrors, setRequestErrors] = useState<string>();

  const blankUser: teacher = {
    userName: 'Stephen King',
    userType: 'teacher',
    loggedIn: true,
    dob: '1973-05-10',
  };

  const [user, setUser] = useState<teacher>(blankUser);

  useEffect(() => {
    let isMounted = true;
    if (isMounted) {
      fetch("/api/auth/login")
        .then((res) => res.json())
        .then((response) => {
          setUser(response["user_info"]);
        });
    }
    // Cleanup and reset
    return function cleanup() {
      isMounted = false;
      setUser(blankUser);
    };
  }, []);
  
  // Fetch user type from API. Below is a dummy.

  console.log(user);

  function logOutUser() {
    fetch("/api/auth/logout")
      .then((res) => res.json())
      .then((response) => {
        setUser(blankUser);
      })
      .catch((error) => {
        // Return errors
        console.error("There was an error!", error);
        setRequestErrors("Sorry, there was a problem logging out.");
      });
  }

  // TODO: add the "home page" for the multiple schools and the school urls/subdomains
  return (
    <Router>
      <Switch>
        <Route exact path="/login">
          {user.loggedIn ? (
            <Redirect to={"/" + user.userType + "/dashboard"} />
          ) : (
            <Redirect to="/auth/login" />
          )}
        </Route>
        <Route exact path="/auth/login">
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

        <Route exact path="/unauthorized" render={(props: any) => (
          <Unauthorized {...props}/>
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

        <Route
          exact
          path="/auth/logout"
          render={() => {
            logOutUser();
            return <Redirect to="/auth/login" />;
          }}
        />
        <Route exact path="/dashboard">
          {user.loggedIn ? (
            <Redirect to={"/" + user.userType + "/dashboard"} />
          ) : (
            <Redirect to="/auth/login" />
          )}
        </Route>
        <ProtectedRoute
          user={user}
          scope="Student"
          exact
          path="/student/dashboard"
          render={(props: any) => (
            <StudentDash
              {...props}
              userName={user.userName}
              userType={user.userType}
              loggedIn={user.loggedIn}
              dob={user.dob}
            />
          )}
        />
        <ProtectedRoute
          user={user}
          scope="Student"
          exact
          path="/student/timetable"
          render={(props: any) => (
            <StudentTimetable
              {...props}
              userName={user.userName}
              userType={user.userType}
              loggedIn={user.loggedIn}
              dob={user.dob}
            />
          )}
        />
        <ProtectedRoute
          user={user}
          scope="Student"
          exact
          path="/student/assignments"
          render={(props: any) => (
            <StudentAssignments
              {...props}
              userName={user.userName}
              userType={user.userType}
              loggedIn={user.loggedIn}
              dob={user.dob}
            />
          )}
        />
        <ProtectedRoute
          user={user}
          scope="Student"
          exact
          path="/student/profile"
          render={(props: any) => (
            <StudentProfile
              {...props}
              userName={user.userName}
              userType={user.userType}
              loggedIn={user.loggedIn}
              dob={user.dob}
            />
          )}
        />
        <ProtectedRoute
          user={user}
          scope="Student"
          exact
          path="/student/assignment/:id"
          render={(props: any) => <AssignmentDisplay {...props} />}
        />
        <Route
          exact
          path="/unauthorized"
          render={(props: any) => <Unauthorized {...props} />}
        />
      </Switch>
    </Router>
  );
};

export default App;
