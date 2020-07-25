import React, { FunctionComponent } from 'react';
import DashboardSidebar from "../../components/DashboardSidebar"
import { student } from "../../components/ProfileContent";

const TeacherDash:FunctionComponent<student> = ({ userName, userType, loggedIn }) => {
  return (
    <div>
      TEACHER DASHBOARD 
      <DashboardSidebar userName={userName} userType={userType} loggedIn={loggedIn}/>
    </div>
  );
};

export default TeacherDash;
