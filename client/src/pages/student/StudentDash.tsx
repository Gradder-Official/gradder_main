import React, { FunctionComponent } from 'react';
import DashboardSidebar from "../../components/DashboardSidebar"
import { student } from "../../components/ProfileContent";

const StudentDash:FunctionComponent<student> = ({ userName, userType, loggedIn }) => {
  return (
    <React.Fragment>
      STUDENT DASHBOARD 
      <DashboardSidebar userName={userName} userType={userType} loggedIn={loggedIn}/>
    </React.Fragment>
  );
};

export default StudentDash;
