import React, { FunctionComponent } from 'react';
import { Link } from 'react-router-dom';;
import { assignment } from '../components/Interfaces';
import StudentSidebar from '../components/StudentSidebar';

const AssignmentBox: FunctionComponent<assignment> = ({ title, date_assigned, assigned_to, assigned_by, due_by, content, filenames, estimated_time, submissions, _id}: assignment) => {

    // Formatting time
    const deadline = new Date(due_by);
    const options = { weekday: 'long', month: 'long', day: 'numeric' };
    const date = deadline.toLocaleDateString(undefined, options);
    const timestamp = deadline.toLocaleTimeString();

    // TODO: actually link the assignment
    const assignmentLink = "/assignments/" + title;
    const estimation = estimated_time == undefined ? "no estimated time" : `around ${estimated_time} minutes`;
    
    return (
        <React.Fragment>
            <StudentSidebar/>
            
            <div className="dash-content" id="assignment-display">
                <div className="row">
                    <div className="col-12 col-md-6">
                        {/* Overview */}
                        <h3>{title}</h3>
                        <div className="assignment-meta-details">
                            <p>{assigned_by} &bull; <span className="subject-badge">{assigned_to}</span></p>
                            <p className="assignment-deadline">Due {date}, {timestamp} &bull; {estimation}</p>
                        </div>
                        <hr/>
                        <div>
                            {/* Replace w/ Quill.js */}
                            {content}
                        </div>
                    </div>
                    <div className="col-12 col-md-6">
                        {/* Submission Form */}
                        <form action="{assignmentLink}/submit" method="post">
                            <div className="form-group">
                                <label htmlFor="content">Submission</label>
                                {/* TODO: Replace with quill */}
                                <textarea className="form-control" name="content" id="content" rows={10}></textarea>
                                <small className="form-text text-muted">
                                    Your content can be formatted, and your
                                    teachers will be able to see your submission
                                    as you do right now.
                                </small>
                            </div>
                            <div className="form-group">
                                <label htmlFor="files">File attachments</label>
                                <input name="files" type="file" className="form-control-file" id="files"></input>
                            </div>
                            <button className="btn w-100" type="submit"></button>
                        </form>
                    </div>
                </div>
            </div>
        </React.Fragment>
    )
}

export default AssignmentBox