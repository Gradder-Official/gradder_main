import React, { FunctionComponent } from 'react';
import DashboardSidebar from "../../components/DashboardSidebar"
import { student } from "../../components/ProfileContent";

const ParentDash: FunctionComponent<student> = ({ userName, userType, loggedIn }) => {
  return (
    <div>
      PARENT DASHBOARD 
      <DashboardSidebar userName={userName} userType={userType} loggedIn={loggedIn}/>
    </div>
  );
};

export default ParentDash;
