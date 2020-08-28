import React, { FunctionComponent, useState } from "react"
import { Link } from "react-router-dom"
import { student, teacher } from "./Interfaces"
import createBrowserHistory from 'history/createBrowserHistory';

const DashProfile: FunctionComponent<student | teacher> = ({ userName }) => {

  const [logoutMessage, setLogoutMessage] = useState<string>();
  const history = createBrowserHistory({ forceRefresh: true });

  const logout = () => {

    fetch('/api/auth/logout')
      .then(res => res.json()).then(response => {
        setLogoutMessage(response['flashes']);
        console.log(logoutMessage)
      })

    history.push("/auth/logout");

  }

  // Get current time in hours:minutes
  const [hour, minute] = new Date().toLocaleTimeString().slice(0, 7).split(":");
  const curTime = hour + ":" + minute;

  // Get day, month, date
  const options = { weekday: "long", month: "long", day: "numeric" };
  const curDate = new Date().toLocaleDateString(undefined, options);

  return (
    <div style={{backgroundColor: "rgb(90, 115, 226)"}} className="dash-container profile">
      <div className="profile-details">
        <h2>Hello, {userName}</h2>
        <img
          src="https://www.iambetter.org/wp-content/uploads/2020/04/Albert_Einstein_1024x1024.jpg"
          alt="Profile"
          className="profile-pic"
          style={{backgroundColor: "rgb(76, 102, 212)"}}
        />
      </div>
      <div className="profile-time">
        <Link to="/" onClick={logout}>
          <i className="material-icons-outlined">exit_to_app</i>
        </Link>
        <Link to="/dashboard">
          <i className="material-icons-outlined">mail</i>
        </Link>
        <h1>{curTime}</h1>
        <p>{curDate}</p>
      </div>
    </div>
  )
}

export default DashProfile