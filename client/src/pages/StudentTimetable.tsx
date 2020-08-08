import React, { FunctionComponent, useEffect, useState } from 'react';
import { assignment, course } from "../components/Interfaces";
import StudentSidebar from '../components/StudentSidebar';
import FullCalendar from '@fullcalendar/react';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import "../assets/styles/dashboard.css";
import "../assets/styles/timetable.css";

const StudentTimetable: FunctionComponent = () => {

    const [assignmentList, setAssignmentList] = useState<Array<assignment>>([
        {title: "", assigned_to: "", due_by: ""}
    ]);

    const [classList, setClassList] = useState<Array<course>>([
        {name: "", daysOfWeek: "", startTime: ""}
    ]);

    useEffect(() => {

        fetch('/api/student/assignment-schedule').
        then(res => res.json()).then(response => {
            setAssignmentList(response['data']['events']);
            console.log(response['data']['events'])
        })

        fetch('/api/student/class-schedule').
        then(res => res.json()).then(response => {
            setClassList(response['data']['class_schedule']);
            console.log(response['data']['class_schedule'])
        })

    }, []);

    return (
        <React.Fragment>

            <StudentSidebar />

            <div className="dash-content" id="student-timetable">
                <div className="month-calendar">
                    <h1>Timetable</h1>
                    <FullCalendar
                        plugins={[dayGridPlugin]}
                        initialView="dayGridMonth"
                        height="75vh"
                        events={assignmentList}
                    />
                </div>
                <div className="time-grid-calendar">
                    <FullCalendar
                        plugins={[timeGridPlugin]}
                        initialView='timeGrid'
                        dayCount={3}
                        height="90vh"
                        nowIndicator={true}
                        slotMinTime="07:00:00"
                        events={classList}
                    />
                </div>
            </div>

        </React.Fragment>
    );
};

export default StudentTimetable;