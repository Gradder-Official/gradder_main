import React, { FunctionComponent } from 'react';
import { Link } from "react-router-dom";
import { teacher } from "../components/Interfaces";
import TeacherSidebar from '../components/TeacherSidebar';
import "../assets/styles/profile.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


const TeacherProfile: FunctionComponent<teacher> = ({ userName, dob }) => {
    var ageCalculator = require('age-calculator');
    let { AgeFromDateString, AgeFromDate } = require('age-calculator');
    let ageFromString = new AgeFromDateString(dob).age;
    // Get current time in hours:minutes
    const [hour, minute] = new Date().toLocaleTimeString().slice(0, 7).split(":")
    const curTime = hour + ":" + minute

    // Get day, month, date
    const options = { weekday: 'long', month: 'long', day: 'numeric' };
    const curDate = new Date().toLocaleDateString(undefined, options)

    return (
        <React.Fragment>
            <TeacherSidebar />
            <div className="dash-content" id="student-overview">
                {/*This is the mobile approach using React-Boostrap*/}
                <Container fluid className="d-block d-lg-none">
                    <Row className="profile-header-small profileDetails-small" xs={12}>
                        <Col className="profile-small" xs={12}>
                            <div className="profile-details">
                                <p className="h3">Welcome, <br></br>{userName}!</p>
                            </div>
                        </Col>
                        <Col xs={12} className="profile-second-row">
                            <div className="profile-time-small text-left text-white">
                                <Row className="ml-n3">
                                    <Link to="/">
                                        <i className="text-left -mr-2 material-icons-outlined">exit_to_app</i>
                                    </Link>
                                    <Link to="/dashboard">
                                        <i className="text-left material-icons-outlined">mail</i>
                                    </Link>
                                </Row>
                                <p className="h1">{curTime}</p>
                                <p>{curDate}</p>
                            </div>
                        </Col>
                    </Row>
                    <Row xs={12}>
                        <img src="https://www.iambetter.org/wp-content/uploads/2020/04/Albert_Einstein_1024x1024.jpg" alt="Profile" id="profile-pic-small" className="d-none d-lg-block profile-pic" />
                    </Row>
                    <Row xs={12}>
                        <div className="dash-container-small">
                            <h5>Date of Birth</h5>
                            <p>{dob}</p>
                        </div>
                        <div className="dash-container-small">
                            <h5>Age</h5>
                            <p>{ageFromString}</p>
                        </div>
                    </Row>
                    <Row xs={12}>
                        <div className="dash-container timetable">
                            <h5>Change Password</h5>
                        </div>
                    </Row>
                </Container>

                {/*This is the desktop/large screen version*/}
                <div className="student-dash-flex-row d-none d-lg-flex">
                    <div className="student-dash-flex-col">
                        <div className="dash-container profile">
                            <div className="profile-details">
                                <h6>Welcome!</h6>
                                <h2>{userName}</h2>

                            </div>
                            <div className="profile-time">
                                <Col xs={12}>
                                    <Link to="/">
                                        <i className="material-icons-outlined">exit_to_app</i>
                                    </Link>
                                    <Link to="/dashboard">
                                        <i className="material-icons-outlined">mail</i>
                                    </Link>
                                </Col>
                                <div className="mr-2">
                                <h1>{curTime}</h1>
                                <p>{curDate}</p>
                            </div>
                            </div>
                        </div>
                        <div className="dash-container timetable">
                            <h5>Change Password</h5>
                        </div>
                    </div>
                    <div className="column">
                        <img src="https://www.iambetter.org/wp-content/uploads/2020/04/Albert_Einstein_1024x1024.jpg" alt="Profile" className="profile-pic" />
                        <div className="dash-container-small">
                            <h5>Age</h5>
                            <p>{ageFromString}</p>
                        </div>
                        <div className="dash-container-small">
                            <h5>Date of Birth</h5>
                            <p>{dob}</p>
                        </div>
                    </div>
                </div>

            </div>

        </React.Fragment >
    );
};

export default TeacherProfile;
