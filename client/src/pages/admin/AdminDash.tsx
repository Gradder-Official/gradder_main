import React, { FunctionComponent } from 'react';
import DashboardSidebar from "../../components/DashboardSidebar"
import { student } from "../../components/ProfileContent";

const AdminDash: FunctionComponent<student> = ({ userName, userType, loggedIn }) => {
  return (
    <div>
      ADMIN DASHBOARD 
      <DashboardSidebar userName={userName} userType={userType} loggedIn={loggedIn}/>
    </div>
  );
};

export default AdminDash;
