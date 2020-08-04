import React, { FunctionComponent } from 'react';
import { student } from "../components/Interfaces";
import StudentSidebar from '../components/StudentSidebar';
import FullCalendar from '@fullcalendar/react';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import "../assets/styles/dashboard.css";
import "../assets/styles/timetable.css";

const StudentTimetable: FunctionComponent<student> = ({ userName }) => {

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
                    />
                </div>
                <div className="time-grid-calendar">
                    <FullCalendar
                        plugins={[timeGridPlugin]}
                        initialView='timeGrid'
                        dayCount={3}
                        height="90vh"
                        allDaySlot={false}
                        nowIndicator={true}
                        slotMinTime="07:00:00"
                        // Get events from JSON
                        events={[{ title: 'event 1', date:'2020-08-02'}]}
                    />
                </div>
            </div>

        </React.Fragment>
    );
};

export default StudentTimetable;