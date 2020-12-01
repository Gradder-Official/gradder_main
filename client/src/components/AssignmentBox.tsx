import React, { FunctionComponent } from 'react'
import { Link } from 'react-router-dom'
import { assignment } from './Interfaces'
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

const AssignmentBox: FunctionComponent<assignment> = ({ id, title, assigned_to, due_by }) => {

    // Formatting time
    const deadline = new Date(due_by)
    const options = { weekday: 'long', month: 'long', day: 'numeric' };
    const date = deadline.toLocaleDateString(undefined, options)
    const timestamp = deadline.toLocaleTimeString()

    // TODO: actually link the assignment
    const assignmentLink = "/student/assignment/" + id;

    return (
        <React.Fragment>
            <Link to={assignmentLink} className="assignment-card">
                <h4 className="card-title">{title}</h4>
                <div className="assignment-info">
                    <p className="assignment-deadline">{date} <br></br> {timestamp}</p>
                    <p style={{ marginTop: "10%" }} className="subject-badge text-center">{assigned_to}</p>
                </div>
            </Link>
        </React.Fragment>
    )
}

export default AssignmentBox
