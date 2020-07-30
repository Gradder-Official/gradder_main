import React, { FunctionComponent } from 'react';
import { Link } from "react-router-dom";
import { student } from "../components/Interfaces";
import StudentSidebar from '../components/StudentSidebar';
import "../assets/styles/assignments.css"
import "../assets/styles/dashboard.css"
import "../assets/styles/main.css"

const StudentAssignments:FunctionComponent<student> = ({userName}) => {


    return(<React.Fragment>


        
{/*<div className="dash-sidebar">
    <div className="navbar-header">
        <a href="{{ url_for('main.dashboard') }}" className="sidebar-logo">
            <img src="{{ url_for('static', filename='images/White Logo.png') }}" alt="Gradder"/>
            <h4>Gradder</h4>
        </a>
        <div className="dash-profile">
            <h4>Hello, {{ userName.first_name }}</h4>
            <img src="https://www.iambetter.org/wp-content/uploads/2020/04/Albert_Einstein_1024x1024.jpg"
                alt="Profile picture" className="profile-pic"/>
        </div>
    </div>
    <nav className="nav flex-column nav-pills" id="sidebar-nav">
        <a className="nav-link" href="{{ url_for('main.dashboard') }}">Overview</a>
        <a className="nav-link" href="#">Timetable</a>
        <a className="nav-link active" href="{{ url_for('student.assignments') }}">Assignments</a>
        <a className="nav-link" href="#">Analytics</a>
        <a className="nav-link" href="{{ url_for('main.profile') }}">Profile</a>
    </nav>
    <div className="navbar-bottom">
        <a href="#">
            <i className="material-icons">mail</i>
        </a>
        <a href="{{ url_for('auth.login') }}">
            <i className="material-icons">exit_to_app</i>
        </a>
    </div>
    </div>*/}

    <StudentSidebar/>


    <div className="dash-content" id="student-assignments">
    <div className="jumbotron">
        <h1>Your assignments</h1>
    </div>
            <div className="assignments">
                {userName.assignments.map(({ className, dueDate, content, estimatedTime, title, fileNames,ID }) => {
                    <React.Fragment>

<div className="card assignment-card">
    <h4 className="card-title task_name">{title}</h4>
    <div className="card-badges">
        <p className="subject-badge">{className}</p>
        <button type="button" className="info-badge" data-toggle="modal" data-target={ID}>
            <i className="material-icons">
                info
            </i>
        </button>
    </div>
</div>

<div className="modal fade" id={ID} tabindex="-1" role="dialog">
    <div className="modal-dialog">
        <div className="modal-content">
            <div className="modal-header">
                                        <h5 className="modal-title">{title}</h5>
                <button type="button" className="btn btn-light modal-btn" data-dismiss="modal">Close</button>
            </div>
            <div className="modal-body">
                <p className="subject">Subject: <b>{className}</b></p>
                <p className="submit_by">Due by: <b>{dueDate}</b></p>
                <p className="estimated_time">Estimated time: <b>{estimatedTime}</b></p>
                                        <p className="content">Content: {content}</p>
                <p className="attachments">Attached files: 
                {fileNames.map(({link})=> <a target="_blank" href="{{ url_for('student.view_assignment', filename=link[0]) }}">{link[1]}</a> )}
                </p>
            </div>
        </div>
    </div>
</div>
                    </React.Fragment>
                })}

    </div>
    </div>
    </React.Fragment>

    )
}