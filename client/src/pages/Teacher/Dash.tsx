import React, { FunctionComponent, useState } from "react";
import { teacher } from "../../components/Interfaces";
import StudentSidebar from "../../components/StudentSidebar";
import "../../assets/styles/dashboard.css";
import "../../assets/styles/assignments.css";
import AssignmentPreview from "../../components/AssignmentPreview";
import DashProfile from "../../components/DashProfile";
import StudentDash from "../Student/Dash";
import TeacherSidebar from "../../components/TeacherSidebar";

const TeacherDash: FunctionComponent<teacher> = ({ userName, userType, loggedIn, dob }) => {

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
