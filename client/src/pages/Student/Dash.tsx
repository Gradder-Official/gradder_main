import React, { FunctionComponent, useState } from "react";
import { student } from "../../components/Interfaces";
import StudentSidebar from "../../components/StudentSidebar";
import "../../assets/styles/dashboard.css";
import "../../assets/styles/assignments.css";
import AssignmentPreview from "../../components/AssignmentPreview";
import DashProfile from "../../components/DashProfile";

const StudentDash: FunctionComponent<student> = ({ userName, userType, loggedIn, dob }) => {

  // Get current time in hours:minutes
  const [hour, minute] = new Date().toLocaleTimeString().slice(0, 7).split(":");
  const curTime = hour + ":" + minute;

  // Get day, month, date
  const options = { weekday: "long", month: "long", day: "numeric" };
  const curDate = new Date().toLocaleDateString(undefined, options);

  return (
    <React.Fragment>
      <StudentSidebar />

      <div className="dash-content" id="student-overview">
        <div className="student-dash-flex-row">
          <div className="dash-container statistics">
            <h5>Statistics</h5>
          </div>

          <DashProfile userName={userName} userType={userType} loggedIn={loggedIn} dob={dob} />

        </div>

        <div className="dash-flex-row">
          <div className="dash-container timetable">
            <h5>Timetable</h5>
          </div>
          <div className="dash-flex-col">
            <div className="dash-container assignments">
              <h5>Upcoming Assignments</h5>
              <AssignmentPreview />
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
