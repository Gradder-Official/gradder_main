// NPM Imports
import React, { FunctionComponent } from 'react';
import { Container } from 'reactstrap';
import DashboardSidebar from "../components/DashboardSidebar"
import ProfileContent from "../components/ProfileContent";

import { student } from "../components/ProfileContent";

const Profile:FunctionComponent<student> = ({ userName, userType, loggedIn }) => {
    return (
        <Container>
            <DashboardSidebar userName={userName} userType={userType} loggedIn={loggedIn}/>
            <ProfileContent userName={userName} userType={userType} loggedIn={loggedIn}/>
        </Container>
    );
};

export default Profile;
