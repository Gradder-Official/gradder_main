import React, { FunctionComponent } from 'react'
import { Link } from 'react-router-dom'
import { assignment } from './Interfaces'

const AssignmentBox: FunctionComponent<assignment> = ({ title, assigned_to, due_by }) => {

    // Formatting time
    const deadline = new Date(due_by)
    const options = { weekday: 'long', month: 'long', day: 'numeric' };
    const date = deadline.toLocaleDateString(undefined, options)
    const timestamp = deadline.toLocaleTimeString()

    // TODO: actually link the assignment
    const assignmentLink = "/assignments/" + title

    return (
        <React.Fragment>
            <Link to={assignmentLink} className="assignment-card">
                <h4 className="card-title">{title}</h4>
                <div className="assignment-info">
                    <p className="subject-badge">{assigned_to}</p>
                    <p className="assignment-deadline">Due {date}, {timestamp}</p>
                </div>
            </Link>
        </React.Fragment>
    )
}

export default AssignmentBox