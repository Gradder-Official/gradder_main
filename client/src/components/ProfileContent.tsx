import React, { FunctionComponent } from 'react'
import { Link } from "react-router-dom";
import "../assets/styles/dashboard.css"
import "../assets/styles/profile.css"

export interface student {
    userName: string,
    userType: string;
    loggedIn: boolean;
}

const Profile:FunctionComponent<student> = ({ userName, userType }) => {
    return (
        <div className="dash-content">
            <div className="jumbotron" id="profile-jumbo">
                <div style={{minWidth: "500px"}}>
                    <h1>Welcome, {userName}!</h1>
                    <br/>
                    <h4>Status: {userType}</h4>
                </div>
                <div className="welcome-top-right">
                    {/* Dummy profile picture, to be replaced */}
                    <img src="https://www.iambetter.org/wp-content/uploads/2020/04/Albert_Einstein_1024x1024.jpg" alt="Profile" className="profile-pic" id="welcome-profile-pic"/>
                    <div className="welcome-buttons">
                        <button type="button" className="btn btn-light">
                            <Link to="/auth/change-password">Change password</Link>
                        </button>
                        <button type="button" className="btn btn-light">
                            <Link to="/auth/change-secret-question">Change secret question</Link>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Profile
