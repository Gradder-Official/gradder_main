import React, { FunctionComponent, useEffect, useState } from "react";
import { assignment, student } from "../components/Interfaces";
import "../assets/styles/assignments.css";
import AssignmentBox from "../components/AssignmentBox";
import 'bootstrap/dist/css/bootstrap.min.css';
import Row from 'react-bootstrap/Row';

const AssignmentPreview: FunctionComponent = () => {
  const [assignments, setAssignments] = useState<Array<assignment>>([]);

  // TODO: get assignments by user ID
  useEffect(() => {
    fetch("/api/student/assignments").then((response) =>
      response.json().then((info) => {
        setAssignments(info.data);
      })
    );
  }, []);

  // DUMMY ASSIGNMENT
  const dummy_assignment = [
    {
      title: "Assignment 1",
      assigned_to: "Math",
      due_by: "Fri, 02 Feb 1996 03:04:05 GMT",
    },
    {
      title: "Assignment 2",
      assigned_to: "Physics",
      due_by: "Fri, 04 Feb 1996 03:04:05 GMT",
    },
    {
      title: "Assignment 3",
      assigned_to: "Chemistry",
      due_by: "Fri, 04 Feb 1996 03:04:05 GMT",
    },
  ];
  
  // eslint-disable-next-line
  useEffect(() => {
    setAssignments(dummy_assignment);
  });

  return (
    <Row className="assignments-preview">
      {assignments.map((assignment) => (
        <AssignmentBox
          title={assignment.title}
          assigned_to={assignment.assigned_to}
          due_by={assignment.due_by}
        />
      ))}
    </Row>
  );
};

export default AssignmentPreview;
