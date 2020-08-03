import React, { FunctionComponent, useEffect, useState } from "react";
import { assignment, student } from "../components/Interfaces";
import "../assets/styles/assignments.css";
import AssignmentBox from "../components/AssignmentBox";

const AssignmentPreview: FunctionComponent = () => {
  const [assignments, setAssignments] = useState<Array<assignment>>([]);

  // TODO: get assignments by user ID
  useEffect(() => {
    fetch("/api/assignments").then((response) =>
      response.json().then((info) => {
        setAssignments(info.data);
      })
    );
  }, []);

  // DUMMY ASSIGNMENT
  const dummy_assignment = [
    {
      title: "Assignment 1",
      assigned_to: "History",
      due_by: "Fri, 02 Feb 1996 03:04:05 GMT",
    },
  ];
  // eslint-disable-next-line
  useEffect(() => {
    setAssignments(dummy_assignment);
  });

  return (
    <div className="assignments-preview">
      {assignments.map((assignment) => (
        <AssignmentBox
          title={assignment.title}
          assigned_to={assignment.assigned_to}
          due_by={assignment.due_by}
        />
      ))}
    </div>
  );
};

export default AssignmentPreview;
