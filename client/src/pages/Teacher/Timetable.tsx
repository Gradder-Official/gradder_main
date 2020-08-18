import React, { FunctionComponent, useEffect, useState } from "react";
import StudentSidebar from "../../components/TeacherSidebar";
import FullCalendar from "@fullcalendar/react";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import ReactModal from 'react-modal';
import { useForm } from "react-hook-form";
import "../../assets/styles/dashboard.css";
import "../../assets/styles/timetable.css";
import "../../assets/styles/modal.css";

const TeacherTimetable: FunctionComponent = () => {
  interface Events {
    title: string;
    start: string;
    end: string;
    backgroundColor: string;
    url: string;
  }

  const [eventList, setEventList] = useState<Array<Events>>([
    {
      title: "Example",
      start: "2020-08-08",
      end: "2020-08-20",
      backgroundColor: "blue",
      url: "",
    },
  ]);

  const [requestErrors, setRequestErrors] = useState<string>();

  const { register, handleSubmit, errors } = useForm();
  const onSubmit = (data:Events) => {

    console.log(data);
    // Send form data to API

    fetch('/api/teacher/calendar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    })
    .then(async response => {
        console.log(JSON.stringify(data))
        const res = await response.json();
        setEventList(res.events)
        console.log(eventList)
        // Check for error response
        if (!response.ok) {
            const error = (res && res.message) || response.status;
            return Promise.reject(error);
        }
    })
    .catch(error => {
        // Return errors
        console.error('There was an error!', error);
        setRequestErrors("Sorry, there was problem with creating an event!")
    }); }

  
  // Fetches from mock APIs but not from /assignment-schedule
  // Returns HTTP instead?
  useEffect(() => {
    fetch("/api/teacher/calendar")
      .then((res) => res.json())
      .then((data) => {
        setEventList(data.events);
        console.log(data.events);
      });
  }, []);

  const [modalIsOpen,setIsOpen] = React.useState(false);
  function openModal() {
    setIsOpen(true);
  }
 
  function afterOpenModal() {
    // references are now sync'd and can be accessed.
  }
 
  function closeModal(){
    setIsOpen(false);
  }

  return (
    <React.Fragment>
      <StudentSidebar />

      <div className="dash-content" id="student-timetable">
        <div className="month-calendar">
          <h1>Timetable</h1>
          <button onClick={openModal}>Open Modal</button>
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
            initialView="timeGrid"
            dayCount={3}
            height="90vh"
            nowIndicator={true}
            slotMinTime="07:00:00"
            events={eventList}
          />
        </div>

        <ReactModal
          isOpen={modalIsOpen}
          onAfterOpen={afterOpenModal}
          onRequestClose={closeModal}
          contentLabel="Example Modal"
          closeTimeoutMS={500}
          className="Modal"
          overlayClassName="Overlay"
        >  <button className="closebutton" onClick={closeModal}>&times;</button>
            <div className="eventForm">
          
        <form onSubmit={handleSubmit(onSubmit)}>

            <div>
          <label>
            Event Name:
            </label>
            {errors.eventName && <span>This field is required</span>}
            <input
              name="title"
              ref={register({ required: true })}
            />
            </div>
         
            <div>
          <label>
            Start Time:
            </label>
            {errors.startTime && <span>This field is required</span>}
            <input
              name="start"
              ref={register({ required: true })}
            />
            </div>
        
            <div>
        <label>
            End Time:
            </label>
            {errors.endTime && <span>This field is required</span>}
            <input
              name="end"
              ref={register({ required: true })}
            />
            </div>

            <div>
          <label>
            Color:
            </label>
            {errors.eventColor && <span>This field is required</span>}
            <select name="backgroundColor"  ref={register({ required: true })}>
              <option value="red">Red</option>
              <option value="orange">Orange</option>
              <option value="yellow">Yellow</option>
              <option value="green">Green</option>
              <option value="blue">Blue</option>
              <option value="purple">Purple</option>
              <option value="pink">Pink</option>
            </select>
            </div>
         
            <div>
          <label>
            URL (Optional):
            <input name="url" ref={register({ required: false })} />
          </label>
          </div>
          <input className="submit-button" type="submit" />
        </form>
        </div>
        </ReactModal>

      </div>
    </React.Fragment>
  );
};

export default TeacherTimetable;
