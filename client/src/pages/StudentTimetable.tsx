import React, { FunctionComponent, useEffect, useState } from 'react';
import { assignment, course, student } from "../components/Interfaces";
import StudentSidebar from '../components/StudentSidebar';
import FullCalendar from '@fullcalendar/react';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import "../assets/styles/dashboard.css";
import "../assets/styles/timetable.css";

const StudentTimetable: FunctionComponent = () => {

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
                        events={eventList}
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
                        events={eventList}
                    />
                </div>
            </div>

        </React.Fragment>
    );
};

export default StudentTimetable;