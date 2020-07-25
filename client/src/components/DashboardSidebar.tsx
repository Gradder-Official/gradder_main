import React, { FunctionComponent } from 'react'
import "../assets/styles/dashboard.css"
import WhiteLogo from "../assets/images/White Logo.png";

import { student } from "./ProfileContent";


const DashboardSidebar: FunctionComponent<student> = ({ userName }) => {
    return (
        <div className="dash-sidebar">
            <div className="navbar-header">
                <a href="/dashboard" className="sidebar-logo">
                    <img src={WhiteLogo} alt="Gradder" />
                    <h4>Gradder</h4>
                </a>
                <div className="dash-profile">
                    <h4>Hello, { userName }</h4>
                    {/* Need to insert username from API */}
                    <img src="https://www.iambetter.org/wp-content/uploads/2020/04/Albert_Einstein_1024x1024.jpg" alt="Profile" className="profile-pic" />
                </div>
            </div>
            <nav className="nav flex-column nav-pills" id="sidebar-nav">
                <a className="nav-link active" href="/dashboard">Overview</a>
                <a className="nav-link" href="/dashboard">Timetable</a>
                <a className="nav-link" href="/student/assignments">Assignments</a>
                <a className="nav-link" href="/dashboard">Analytics</a>
                <a className="nav-link" href="/profile">Profile</a>
            </nav>
            <div className="navbar-bottom">
                <a href="/dashboard">
                    <i className="material-icons">mail</i>
                </a>
                <a href="/auth/logout">
                    <i className="material-icons">exit_to_app</i>
                </a>
            </div>
        </div>
    )
}

export default DashboardSidebar
