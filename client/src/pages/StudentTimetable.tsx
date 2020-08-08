import React, { FunctionComponent, useEffect, useState } from 'react';
<<<<<<< HEAD
import { assignment, course } from "../components/Interfaces";
=======
import { student } from "../components/Interfaces";
>>>>>>> b2e902edf28d949455a32921eb70a7f3c1d368e0
import StudentSidebar from '../components/StudentSidebar';
import FullCalendar from '@fullcalendar/react';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import "../assets/styles/dashboard.css";
import "../assets/styles/timetable.css";

const StudentTimetable: FunctionComponent = () => {

<<<<<<< HEAD
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

=======
    interface Events {
        title: string
        date: string
    }

    const [eventList, setEventList] = useState<Array<Events>>([
        {title: "Example", date: "2020-08-08"}
    ]);

    // Fetches from mock APIs but not from /assignment-schedule
    // Returns HTTP instead?
    useEffect(() => {
        fetch('/api/assignment-schedule').
        then(res => res.json()).then(data => {
            setEventList(data.events);
            console.log(data.events)
        })
>>>>>>> b2e902edf28d949455a32921eb70a7f3c1d368e0
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
<<<<<<< HEAD
                        events={assignmentList}
=======
                        events={eventList}
>>>>>>> b2e902edf28d949455a32921eb70a7f3c1d368e0
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
<<<<<<< HEAD
                        events={classList}
=======
                        events={eventList}
>>>>>>> b2e902edf28d949455a32921eb70a7f3c1d368e0
                    />
                </div>
            </div>

        </React.Fragment>
    );
};

export default StudentTimetable;