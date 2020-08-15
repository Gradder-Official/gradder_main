import React, { FunctionComponent } from 'react'
import { studentInfo } from './Interfaces'
import "../assets/styles/manage-courses.css";

const MyStudent: FunctionComponent<studentInfo> = ({ email, first_name, last_name, password, courses, assignments }) => {
    return (
        <div className="student-dash-info">
            <h4 className="student-name">{last_name}, {first_name}</h4>
            <p>{email}</p>
            <p>{courses}</p>
        </div>
    )
}

export default MyStudent