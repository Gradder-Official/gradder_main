import React, { FunctionComponent, useEffect, useState } from "react";
import { assignment, student } from "../components/Interfaces";
import "../assets/styles/assignments.css";
import AssignmentBox from "../components/AssignmentBox";

const AssignmentPreview: FunctionComponent = () => {

  const [assignments, setAssignments] = useState<Array<assignment>>([
    {
      title: "",
      assigned_to: "",
      due_by: "",
    }
  ]);

  // TODO: get assignments by user ID
  useEffect(() => {
    fetch("/api/student/assignments").then((response) =>
      response.json().then((info) => {
        setAssignments(info.data);
      })
    );
  }, []);

  useEffect(() => {
    fetch('/api/student/assignments')
      .then(res => res.json()).then(response => {
        setAssignments(response['data']['assignments']);
      }
    )
  }, []);
  
  return (
    <div className="assignments-preview">
      {assignments.map((assignment) => (
        <AssignmentBox
          title={assignment.title}
          assigned_to={assignment.assigned_to}
          due_by={assignment.due_by}
          id={assignment.id}
        />
      ))}
    </div>
  );
};

export default AssignmentPreview;
