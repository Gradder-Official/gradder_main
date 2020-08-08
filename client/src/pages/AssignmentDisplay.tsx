import React, { FunctionComponent, useState } from 'react';
import { assignment } from '../components/Interfaces';
import StudentSidebar from '../components/StudentSidebar';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

// Quill.js
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.bubble.css';
import 'react-quill/dist/quill.snow.css';

// Dropzone
import {useDropzone} from 'react-dropzone';

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

const AssignmentDisplay = (props: any) => {
  // TODO: Get assignment
  let id = props.match.params.id;
  let a: assignment = {
    title: "Assignment Title",
    date_assigned: "Fri Aug 07 2020 13:41:27 GMT+0100",
    assigned_to: "assigned_to",
    assigned_by: "assigned_by",
    due_by: "Fri Aug 09 2020 13:41:27 GMT+0100",
    content: "<h1>This is an assignment</h1>Have fun!",
    filenames: ["doctor.png"],
    estimated_time: "30",
    submissions: new Array<string>(),
    id: id,
  }
  
  // TODO: Get from server
  let alreadySubmitted = true;

  // Formatting time
  const deadline = new Date(a.due_by);
  const options = { weekday: 'long', month: 'long', day: 'numeric' };
  const date = deadline.toLocaleDateString(undefined, options);
  const timestamp = deadline.toLocaleTimeString();

  // TODO: actually link the assignment
  const estimation = a.estimated_time === undefined ? "no estimated time" : `around ${a.estimated_time} minutes`;
  
  // Dropzone integration
  const {acceptedFiles, getRootProps, getInputProps} = useDropzone({multiple: true});
  const files = acceptedFiles.map((file: File) => {
    let size = `${file.size} bytes`;
    if (file.size > 1_048_576) {
      // Mb
      size = `${(file.size/1_048_576).toFixed(2)}Mb`;
    } else if (file.size > 1_024) {
      // Kb
      size = `${(file.size/1_024).toFixed(2)}Kb`;
    }

    return (
      <li className="list-group-item d-flex justify-content-between align-items-center" key={(file as any).path}>
        {(file as any).path}
        <span className="badge badge-primary badge-pill">
          {size}
        </span>
      </li>
    )
  });

  let [cached, setCached] = useLocalStorage(a.id!, "Your assignment goes here");
  return (
    <React.Fragment>
      <StudentSidebar/>
      
      <div className="dash-content" id="assignment-display">
        <div className="dash-container">
          <Row className="h-100">
            <Col className="col-12 col-md-5">
              {/* Overview */}
              <h3>{a.title}</h3>
              <div className="assignment-meta-details">
                <p>{a.assigned_by} &bull; <span className="subject-badge">{a.assigned_to}</span></p>
                <p className="assignment-deadline">Due {date}, {timestamp} &bull; {estimation}</p>
              </div>
              <hr/>
              <div>
                {/* Replace w/ Quill.js */}
                <ReactQuill theme="bubble" value={a.content} readOnly/>
              </div>
            </Col>
            <Col className="col-12 col-md-7 d-flex flex-column">
              {/* Submission Form */}
              <h4>Submission</h4>
              <form action="{assignmentLink}/submit" method="post" className="pt-1 d-flex flex-column flex-grow-1">
                <div className="d-flex flex-column flex-grow-1 form-group">
                  <ReactQuill theme="snow" value={cached} onChange={setCached}/>
                  <input type="text" name="content" value={cached} hidden/>
                  <small className="form-text text-muted">
                    We automatically save your work to your 
                    browser when you type - but don't worry,
                    your teachers can't see until you send it.
                  </small>
                </div>
                <div className="form-group">
                  <label htmlFor="files">File attachments</label>
                  <div {...getRootProps({className: 'dropzone border p-3 text-center'})}>
                    <input name="files" type="file" id="files" {...getInputProps()}></input>
                    <p className="p-0 m-0">Drag and drop some files here, or click to select files</p>
                  </div>
                  <ul className="list-group">{files}</ul>
                  <small className="form-text text-muted">
                    Please upload all your files at once. If you do not, any already
                    loaded files will be replaced.
                  </small>
                </div>
                <button type="submit" className="mt-3 btn btn-primary w-100">Submit</button>
                { alreadySubmitted ?
                    <small className="text-muted py-2">
                      <span className="material-icons pr-1">assignment_turned_in</span>
                      Hey! You've already turned this assignment in, however feel free to
                      submit again!
                    </small>
                    :
                    ""
                }
              </form>
            </Col>
          </Row>
          <p className="text-right">
            <small>
              <code>ID: {a.id}</code>
            </small>
          </p>
        </div>
      </div>
    </React.Fragment>
  )
}

export default AssignmentDisplay;