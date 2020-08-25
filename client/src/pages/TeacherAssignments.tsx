import React, { FunctionComponent } from 'react';
import { teacher } from "../components/Interfaces";
import TeacherSidebar from '../components/TeacherSidebar';
import "../assets/styles/assignments.css"
import AssignmentPreview from '../components/AssignmentPreview';

const TeacherAssignments: FunctionComponent<teacher> = ({ userName, userType }) => {

    return (
        <React.Fragment>
            <TeacherSidebar />
            <div className="dash-content">
                <div className="dash-header">
                    <h1>Your assignments</h1>
                </div>
                <AssignmentPreview />
            </div>
        </React.Fragment>
    )
}

export default TeacherAssignments