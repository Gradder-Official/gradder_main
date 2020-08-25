import React, { FunctionComponent } from 'react'
import { NavLink } from "react-router-dom";
import WhiteLogo from "../assets/images/white-logo.png"
import "../assets/styles/sidebar.css"

const TeacherSidebar: FunctionComponent = () => {
    return (
        <div className="dash-sidebar">
            <div className="navbar-header">
                <NavLink to="/dashboard" className="sidebar-logo">
                    <img src={ WhiteLogo } alt="Gradder" />
                    <h4>Gradder</h4>
                </NavLink>
            </div>
            <nav className="nav flex-column nav-pills" id="sidebar-nav">
                <NavLink to="/teacher/dashboard" className="nav-link" activeClassName="active">
                    <span className="material-icons-outlined">home</span>
                    Overview
                </NavLink>
                <NavLink to="/teacher/timetable" className="nav-link" activeClassName="active">
                    <span className="material-icons-outlined">calendar_today</span>
                    Timetable
                </NavLink>
                <NavLink to="/teacher/assignments" className="nav-link" activeClassName="active">
                    <span className="material-icons-outlined">check_box</span>
                    Assignments
                </NavLink>
                <NavLink to="/dashboard" className="nav-link" activeClassName="active">
                    <span className="material-icons-outlined">pie_chart</span>   
                    Analytics
                </NavLink>
                <NavLink to="/teacher/profile" className="nav-link" activeClassName="active">
                    <span className="material-icons-outlined">settings</span>
                    Settings
                </NavLink>
            </nav>
        </div>
    )
}

export default TeacherSidebar