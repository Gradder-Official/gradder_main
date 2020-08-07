import React, { FunctionComponent, useState } from 'react';
import { assignment } from '../components/Interfaces';
import StudentSidebar from '../components/StudentSidebar';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

// Quill.js
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.bubble.css';
import 'react-quill/dist/quill.snow.css';

// Custom styles
import "../assets/styles/assignment.css";

// Hook (credit: https://usehooks.com/useLocalStorage/)
function useLocalStorage(key: string, initialValue: any) {
    // State to store our value
    // Pass initial state function to useState so logic is only executed once
    const [storedValue, setStoredValue] = useState(() => {
      try {
        // Get from local storage by key
        const item = window.localStorage.getItem(key);
        // Parse stored json or if none return initialValue
        return item ? JSON.parse(item) : initialValue;
      } catch (error) {
        // If error also return initialValue
        console.log(error);
        return initialValue;
      }
    });
  
    // Return a wrapped version of useState's setter function that ...
    // ... persists the new value to localStorage.
    const setValue = (value: any) => {
      try {
        // Allow value to be a function so we have same API as useState
        const valueToStore =
          value instanceof Function ? value(storedValue) : value;
        // Save state
        setStoredValue(valueToStore);
        // Save to local storage
        window.localStorage.setItem(key, JSON.stringify(valueToStore));
      } catch (error) {
        // A more advanced implementation would handle the error case
        console.log(error);
      }
    };
  
    return [storedValue, setValue];
}

const AssignmentDisplay: FunctionComponent<assignment> = ({ title, date_assigned, assigned_to, assigned_by, due_by, content, filenames, estimated_time, submissions, _id}: assignment) => {

    // Formatting time
    const deadline = new Date(due_by);
    const options = { weekday: 'long', month: 'long', day: 'numeric' };
    const date = deadline.toLocaleDateString(undefined, options);
    const timestamp = deadline.toLocaleTimeString();

    // TODO: actually link the assignment
    const assignmentLink = "/assignments/" + title;
    const estimation = estimated_time === undefined ? "no estimated time" : `around ${estimated_time} minutes`;
    
    let [cached, setCached] = useLocalStorage(_id!, "Your assignment goes here");
    return (
        <React.Fragment>
            <StudentSidebar/>
            
            <div className="dash-content" id="assignment-display">
                <div className="dash-container">
                    <Row>
                        <Col className="col-12 col-md-6">
                            {/* Overview */}
                            <h3>{title}</h3>
                            <div className="assignment-meta-details">
                                <p>{assigned_by} &bull; <span className="subject-badge">{assigned_to}</span></p>
                                <p className="assignment-deadline">Due {date}, {timestamp} &bull; {estimation}</p>
                            </div>
                            <hr/>
                            <div>
                                {/* Replace w/ Quill.js */}
                                <ReactQuill theme="bubble" value={content} readOnly/>
                            </div>
                        </Col>
                        <Col className="col-12 col-md-6">
                            {/* Submission Form */}
                            <form action="{assignmentLink}/submit" method="post">
                                <div className="form-group">
                                    <h4>Submission</h4>
                                    <ReactQuill theme="snow" value={cached} onChange={setCached}/>
                                    <small className="form-text text-muted">
                                        We automatically save your work to your 
                                        browser when you type - but don't worry,
                                        your teachers can't see until you send it.
                                    </small>
                                </div>
                                <div className="form-group">
                                    <label htmlFor="files">File attachments</label>
                                    <input name="files" type="file" className="form-control-file" id="files"></input>
                                </div>
                                <button className="btn w-100" type="submit"></button>
                            </form>
                        </Col>
                    </Row>
                </div>
            </div>
        </React.Fragment>
    )
}

export default AssignmentDisplay;