import React, { FunctionComponent } from 'react';
import { student } from "../components/Interfaces";
import StudentSidebar from '../components/StudentSidebar';
import "../assets/styles/assignments.css"
import AssignmentPreview from '../components/AssignmentPreview';

const StudentAssignments: FunctionComponent<student> = ({ userName }) => {

    return (
        <React.Fragment>
            <StudentSidebar />
            <AssignmentPreview />
        </React.Fragment>
    )
}

export default StudentAssignments