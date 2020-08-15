import React, { FunctionComponent, useState, useEffect } from "react";
import { teacher, studentInfo, student } from "../../components/Interfaces";
import "../../assets/styles/dashboard.css";
import "../../assets/styles/assignments.css";
import DashProfile from "../../components/DashProfile";
import TeacherSidebar from "../../components/TeacherSidebar";
import MyStudent from "../../components/myStudent";
import { Dictionary } from "@fullcalendar/react";

const TeacherDash: FunctionComponent<teacher> = ({ userName, userType, loggedIn, dob }) => {

  const [myStudents, setMyStudents] = useState<Array<studentInfo>>([
    {
      "email": "",
      "first_name": "",
      "last_name": "",
      "password": "",
      "courses": [],
      "assignments": []
    }
  ]);

  useEffect(() => {
    fetch('/api/teacher/courses')
      .then(res => res.json()).then(response => {
        let studentInfoList: Array<studentInfo> = []
        response['data']['courses'].map((course: Dictionary) => {
          course.students.map((student: studentInfo) => {
            studentInfoList.push(student)
          })
        })
        setMyStudents(studentInfoList)
      }
      )
  }, []);

  console.log(myStudents)

  return (
    <React.Fragment>
      <TeacherSidebar />

      <div className="dash-content" id="teacher-overview">
        <div className="dash-flex-row">
          <div className="dash-container statistics">
            <h5>Class Statistics</h5>
          </div>

          <DashProfile userName={userName} userType={userType} loggedIn={loggedIn} dob={dob} />
        </div>

        <div className="dash-flex-row">
          <div className="dash-container timetable">
            <h5>Students</h5>
            {myStudents.map((student) => (
              <MyStudent 
                email={student.email} 
                first_name={student.first_name}
                last_name={student.last_name}
                password={student.password}
                courses={student.courses}
                assignments={student.assignments}/>
            ))}
          </div>
          <div className="dash-flex-col">
            <div className="dash-container assignments">
              <h5>Course Plans</h5>
            </div>
            <div className="dash-container grades">
              <h5>Assignments</h5>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
};

export default TeacherDash;
