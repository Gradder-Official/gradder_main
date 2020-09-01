import React, { FunctionComponent } from 'react';
import { teacher } from "../components/Interfaces";
import TeacherSidebar from '../components/TeacherSidebar';
import FullCalendar from '@fullcalendar/react';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import "../assets/styles/dashboard.css";
import "../assets/styles/timetable.css";

const TeacherTimetable: FunctionComponent<teacher> = ({ userName }) => {

    return (
        <React.Fragment>

            <TeacherSidebar />

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

export default TeacherTimetable;