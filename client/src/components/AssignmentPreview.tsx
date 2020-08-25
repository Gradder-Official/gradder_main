import React, { FunctionComponent, useEffect, useState } from "react";
import { assignment } from "../components/Interfaces";
import "../assets/styles/assignments.css";
import AssignmentBox from "../components/AssignmentBox";
import 'bootstrap/dist/css/bootstrap.min.css';
import Row from 'react-bootstrap/Row';

const AssignmentPreview: FunctionComponent = () => {

  const [assignments, setAssignments] = useState<Array<assignment>>([
    {
<<<<<<< HEAD
<<<<<<< HEAD
      title: "Dummy Assignment",
      assigned_to: "History",
=======
      title: "Assignment 1",
      assigned_to: "Math",
>>>>>>> 4021de8ba5042d7eeb0233b8e41cc91d4b19a4d5
      due_by: "Fri, 02 Feb 1996 03:04:05 GMT",
      id: "fcb1f1bcd4cde0c0b34a80bc21ffda68"
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
=======
      title: "",
      assigned_to: "",
      due_by: "",
    }
  ]);
>>>>>>> dev

  useEffect(() => {
    fetch('/api/student/assignments')
      .then(res => res.json()).then(response => {
        setAssignments(response['data']['assignments']);
      }
    )
  }, []);
  
  return (
    <Row className="assignments-preview">
      {assignments.map((assignment) => (
        <AssignmentBox
          title={assignment.title}
          assigned_to={assignment.assigned_to}
          due_by={assignment.due_by}
          id={assignment.id}
        />
      ))}
    </Row>
  );
};

export default AssignmentPreview;
