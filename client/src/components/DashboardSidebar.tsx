import React, { FunctionComponent } from 'react'
import { Link } from "react-router-dom";
import "../assets/styles/dashboard.css"
import WhiteLogo from "../assets/images/White Logo.png";

import { student } from "./ProfileContent";


const DashboardSidebar: FunctionComponent<student> = ({ userName }) => {
    return (
        <div className="dash-sidebar">
            <div className="navbar-header">
                <Link to="/dashboard" className="sidebar-logo">
                    <img src={WhiteLogo} alt="Gradder" />
                    <h4>Gradder</h4>
                </Link>
                <div className="dash-profile">
                    <h4>Hello, { userName }</h4>
                    <img src="https://www.iambetter.org/wp-content/uploads/2020/04/Albert_Einstein_1024x1024.jpg" alt="Profile" className="profile-pic" />
                    {/* Dummy image, will ultimately be replaced */}
                </div>
            </div>
            <nav className="nav flex-column nav-pills" id="sidebar-nav">
                <Link to="/dashboard" className="nav-link active" >Overview</Link>
                <Link to="/dashboard" className="nav-link" >Timetable</Link>
                <Link to="/student/assignments" className="nav-link">Assignments</Link>
                <Link to="/dashboard" className="nav-link">Analytics</Link>
                <Link to="/profile" className="nav-link">Profile</Link>
            </nav>
            <div className="navbar-bottom">
                <Link to="/dashboard">
                    <i className="material-icons">mail</i>
                </Link>
                <Link to="/auth/logout">
                    <i className="material-icons">exit_to_app</i>
                </Link>
            </div>
        </div>
    )
}

export default DashboardSidebar
