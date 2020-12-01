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
import TeacherAnalytics from "./pages/Teacher/Analytics";
import TeacherAssignments from "./pages/TeacherAssignments";

const App: FunctionComponent = () => {
  const [requestErrors, setRequestErrors] = useState<string>();

  const userName = sessionStorage.getItem('userName') || "";
  const userType = sessionStorage.getItem('userType') || "";
  const loggedIn = sessionStorage.getItem('loggedIn') || 'false';
  const dob = sessionStorage.getItem('dob') || "";

  console.log(userName, userType, loggedIn)

  // TODO: add the "home page" for the multiple schools and the school urls/subdomains
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          {(loggedIn === 'true') ? (
            <Redirect to={"/" + userType.toLowerCase() + "/dashboard"} />
            ) : (
            <Login />
          )}
        </Route>
        <Route exact path="/auth/logout" render={() => {
          sessionStorage.clear()
          fetch('/api/auth/logout').then(res => res.json())
          .catch(error => { return <Redirect to="/"/>})
          return <Login />;
        }} />
        <Route exact path="/dashboard">
          {(loggedIn === 'true') ? (
            <Redirect to={"/" + userType.toLowerCase() + "/dashboard"} />
            ) : (
            <Login />
          )}
        </Route>

        <ProtectedRoute userType={userType} scope="student" exact path="/student/dashboard" render={(props: any) => (
          <StudentDash {...props} userName={userName} userType={userType} loggedIn={loggedIn} dob={dob} />
        )} />
        <ProtectedRoute userType={userType} scope="student" exact path="/student/timetable" render={(props: any) => (
          <StudentTimetable {...props} userName={userName} userType={userType} loggedIn={loggedIn} dob={dob} />
        )} />
        <ProtectedRoute userType={userType} scope="student" exact path="/student/assignments" render={(props: any) => (
          <StudentAssignments {...props} userName={userName} userType={userType} loggedIn={loggedIn} dob={dob} />
        )} />
        <ProtectedRoute userType={userType} scope="student" exact path="/student/profile" render={(props: any) => (
          <StudentProfile {...props} userName={userName} userType={userType} loggedIn={loggedIn} dob={dob} />
        )} />

        <ProtectedRoute userType={userType} scope="teacher" exact path="/teacher/dashboard" render={(props: any) => (
          <TeacherDash {...props} userName={userName} userType={userType} loggedIn={loggedIn} dob={dob} />
        )} />
        <ProtectedRoute userType={userType} scope="teacher" exact path="/teacher/classes" render={(props: any) => (
          <TeacherCourses {...props} userName={userName} userType={userType} loggedIn={loggedIn} dob={dob} />
        )} />
        <ProtectedRoute userType={userType} scope="teacher" exact path="/teacher/timetable" render={(props: any) => (
          <TeacherTimetable {...props} userName={userName} userType={userType} loggedIn={loggedIn} dob={dob} />
        )} />
        <ProtectedRoute userType={userType} scope="teacher" exact path="/teacher/assignmentss" render={(props: any) => (
          <TeacherAssignments {...props} userName={userName} userType={userType} loggedIn={loggedIn} dob={dob} />
        )} />
        <ProtectedRoute userType={userType} scope="teacher" exact path="/teacher/analytics" render={(props: any) => (
          <TeacherAnalytics {...props} userName={userName} userType={userType} loggedIn={loggedIn} dob={dob} />
        )} />

        <Route exact path="/student/assignment/:id" render={(props) => (
            <AssignmentDisplay {...props}/>
        )}/>
        <Route exact path="/unauthorized" render={(props: any) => (
          <Unauthorized {...props} />
        )}/>

      </Switch>
    </Router>
  );
};

export default App;
