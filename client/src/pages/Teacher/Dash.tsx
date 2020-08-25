import React, { FunctionComponent, useState, useEffect } from "react";
import { teacher, studentInfo, student, course } from "../../components/Interfaces";
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

  const blankCourse: course = {
    "id": "",
    "name": "",
    "assignments": {},
    "students": [{
      "email": "",
      "first_name": "",
      "last_name": "",
      "password": "",
      "courses": [],
      "assignments": []
    }],
    "description": "",
    "schedule_time": "",
    "schedule_days": "",
    "syllabus": [""],
    "course_analytics": {}
  }

  const [courses, setCourses] = useState<Array<course>>([blankCourse]);

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
        setCourses(response['data']['courses']);
      }
      )
  }, []);

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
            {myStudents[0] !== undefined &&
              myStudents[0]["first_name"] !== "" &&
              myStudents.map((student) => (
                <MyStudent
                  email={student.email}
                  first_name={student.first_name}
                  last_name={student.last_name}
                  password={student.password}
                  courses={student.courses}
                  assignments={student.assignments} />
              ))}
            {myStudents[0] === undefined &&
              <p className="no-students">No students</p>
            }
          </div>
          <div className="dash-flex-col">
            <div className="dash-container courses">
              <h5>Courses</h5>
              <div className="courses-wrapper">
                {courses.map((course) => (
                  <div className="teacher-dash-courses-container">
                    <h1>{course.name}</h1>
                    <h3>{course.description}</h3>
                    <p>Schedule days: {course.schedule_days}</p>
                  </div>
                ))}
              </div>
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
