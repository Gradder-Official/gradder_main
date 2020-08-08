import React, { FunctionComponent, useEffect, useState } from "react";
import { assignment, student } from "../components/Interfaces";
import "../assets/styles/assignments.css";
import AssignmentBox from "../components/AssignmentBox";

const AssignmentPreview: FunctionComponent = () => {
<<<<<<< HEAD
=======
  const [assignments, setAssignments] = useState<Array<assignment>>([
    {
      title: "",
      assigned_to: "",
      due_by: "",
    }
  ]);
>>>>>>> b2e902edf28d949455a32921eb70a7f3c1d368e0

  const [assignments, setAssignments] = useState<Array<assignment>>([
    {
      title: "Dummy Assignment",
      assigned_to: "History",
      due_by: "Fri, 02 Feb 1996 03:04:05 GMT",
    }
  ]);

  useEffect(() => {
    fetch('/api/student/assignments').
      then(res => res.json()).then(response => {
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
        />
      ))}
    </div>
  );
};

export default AssignmentPreview;
