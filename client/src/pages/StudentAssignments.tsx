import React, { FunctionComponent } from 'react';
import { student } from "../components/Interfaces";
import StudentSidebar from '../components/StudentSidebar';
import "../assets/styles/assignments.css"
import AssignmentPreview from '../components/AssignmentPreview';

const StudentAssignments: FunctionComponent = () => {

    return (
        <React.Fragment>
            <StudentSidebar />
            <div className="dash-content">
                <div className="dash-header">
                    <h1>Your assignments</h1>
                </div>
                <AssignmentPreview />
            </div>
        </React.Fragment>
    )
}

export default StudentAssignments