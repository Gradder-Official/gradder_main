import React, { FunctionComponent } from 'react';
import { Link } from "react-router-dom";
import { student } from "../../components/Interfaces";
import StudentSidebar from '../../components/StudentSidebar';
import "../../assets/styles/profile.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


const StudentProfile: FunctionComponent<student> = ({ userName, dob }) => {
    let { AgeFromDateString } = require('age-calculator');
    let ageFromString = new AgeFromDateString(dob).age;
    // Get current time in hours:minutes
    const [hour, minute] = new Date().toLocaleTimeString().slice(0, 7).split(":")
    const curTime = hour + ":" + minute

    // Get day, month, date
    const options = { weekday: 'long', month: 'long', day: 'numeric' };
    const curDate = new Date().toLocaleDateString(undefined, options)

    return (
        <React.Fragment>

            <StudentSidebar />

            {/*This is the mobile approach using React-Boostrap*/}
            <div className="dash-content" id="student-overview">
<<<<<<< HEAD
                <Container>
                    <Row className="justify-content-md-center mobile-profile">
                        <Col className="profileDetails" xs={12} sm={8}>
                            <div className="dash-container profile">
                                <div className="profile-details">
                                    <h6>Welcome!</h6>
                                    <h2>{userName}</h2>

                                </div>
                                <div className="profile-time">
                                    <Link to="/">
                                        <i className="material-icons-outlined">exit_to_app</i>
                                    </Link>
                                    <Link to="/dashboard">
                                        <i className="material-icons-outlined">mail</i>
                                    </Link>
                                    <h1>{curTime}</h1>
                                    <p>{curDate}</p>
                                </div>
                            </div>
                        </Col>
                        <Col xs={12} sm={8}>
                            <img src="https://www.iambetter.org/wp-content/uploads/2020/04/Albert_Einstein_1024x1024.jpg" alt="Profile" className="profile-pic" />
                        </Col>
                        <Col xs={12} sm={8}>
                            <div className="dash-container-small">
                                <h5>Age</h5>
                                <p>{ageFromString}</p>
=======
                {/*This is the mobile approach using React-Boostrap*/}
                <Container fluid className="d-block d-lg-none">
                    {/*</Container><Row className="justify-content-md-center" */}
                    <Row className="dash-container-small profileDetails-small" xs={12}>
                        <Col className="profile-small" xs={12}>
                            <div className="profile-details">
                                <p className="h3">Welcome, <br></br>{userName}!</p>
>>>>>>> 4021de8ba5042d7eeb0233b8e41cc91d4b19a4d5
                            </div>
                       </Col>
                        <Col xs={12} className="profile-second-row">
                            <div className="profile-time-small text-left text-white">
                                <Link to="/">
                                    <i className="text-left -mr-2 material-icons-outlined">exit_to_app</i>
                                </Link>
                                <Link to="/dashboard">
                                    <i className="text-left material-icons-outlined">mail</i>
                                </Link>
                                <p className="h1">{curTime}</p>
                                <p>{curDate}</p>
                            </div>
                        </Col>
                    </Row>
                    <Row xs={12}>
                        <img src="https://www.iambetter.org/wp-content/uploads/2020/04/Albert_Einstein_1024x1024.jpg" alt="Profile" id="profile-pic-small" className="profile-pic" />
                    </Row>
                    <Row xs={12}>
                        <div className="dash-container-small">
                            <h5>Date of Birth</h5>
                            <p>{dob}</p>
                        </div>
                    </Row>
                    <Row xs={12}>
                        <div className="dash-container timetable">
                            <h5>Change Password</h5>
                        </div>
                    </Row>
                    {/* </Row> */}
                </Container>

                {/*This is the desktop/large screen version*/}

<<<<<<< HEAD
                
                
                <div className="student-dash-flex-row desktop-profile">
=======


                <div className="student-dash-flex-row d-none d-lg-flex">
>>>>>>> 4021de8ba5042d7eeb0233b8e41cc91d4b19a4d5
                    <div className="student-dash-flex-col">
                        <div className="dash-container profile">
                            <div className="profile-details">
                                <h6>Welcome!</h6>
                                <h2>{userName}</h2>

                            </div>
                            <div className="profile-time">
                                <Link to="/">
                                    <i className="material-icons-outlined">exit_to_app</i>
                                </Link>
                                <Link to="/dashboard">
                                    <i className="material-icons-outlined">mail</i>
                                </Link>
                                <h1>{curTime}</h1>
                                <p>{curDate}</p>
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
<<<<<<< HEAD
                
=======
>>>>>>> 4021de8ba5042d7eeb0233b8e41cc91d4b19a4d5

            </div>
        </React.Fragment >
    );
};

export default StudentProfile;