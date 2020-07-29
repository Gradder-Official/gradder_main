import React, { FunctionComponent } from 'react';
import { student } from "../components/Interfaces";
import StudentSidebar from '../components/StudentSidebar';
import "../assets/styles/dashboard.css"

const StudentDash:FunctionComponent<student> = ({ userName }) => {
  return (
    <React.Fragment>

      <StudentSidebar/>

      <div className="dash-content" id="student-overview">

        <div className="student-dash-flex-row">
          <div className="dash-container statistics">
            <h5>Statistics</h5>
          </div>
          <div className="dash-container profile">
            <h5>Student profile</h5>
            <h5>Hello, { userName }</h5>
            {/*<img src="https://www.iambetter.org/wp-content/uploads/2020/04/Albert_Einstein_1024x1024.jpg" alt="Profile" className="profile-pic" />
            Dummy image, will ultimately be replaced */}
          </div>
        </div>

        <div className="student-dash-flex-row">
          <div className="dash-container timetable">
            <h5>Timetable</h5>
          </div>
          <div className="student-dash-flex-col">
            <div className="dash-container homework">
              <h5>Homework</h5>
            </div>
            <div className="dash-container grades">
              <h5>Grades</h5>
            </div>
          </div>
        </div>

      </div>

    </React.Fragment>
  );
};

export default StudentDash;