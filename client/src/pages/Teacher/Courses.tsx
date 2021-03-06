import React, { FunctionComponent, useState, useEffect } from "react";
import { teacher, course } from "../../components/Interfaces";
import { useForm } from "react-hook-form";
import "../../assets/styles/dashboard.css";
import "../../assets/styles/manage-courses.css";
import TeacherSidebar from "../../components/TeacherSidebar";
import { Form, ButtonGroup, Button } from "react-bootstrap";
import UpdateSyllabus from "../../components/UpdateSyllabus";

const TeacherCourses: FunctionComponent<teacher> = ({ userName, userType, loggedIn, dob }) => {

    const blankCourse: course = {
        "id": "",
        "name": "",
        "assignments": {},
        "students": [{
            "email": "",
            "first_name": "",
            "last_name": "",
            "password": "",
            "courses": [],
            "assignments": []
        }],
        "description": "",
        "schedule_time": "",
        "schedule_days": "",
        "syllabus": [""],
        "course_analytics": {}
    }

    const [courses, setCourses] = useState<Array<course>>([blankCourse]);

    useEffect(() => {
        fetch('/api/teacher/courses')
            .then(res => res.json()).then(response => {
                setCourses(response['data']['courses']);
            }
        )
    }, []);

    const [displayCourse, setDisplayCourse] = useState<course>(blankCourse)

    function showCourseInfo(chosenCourse: course) {
        setDisplayCourse({
            "id": chosenCourse.id,
            "name": chosenCourse.name,
            "assignments": chosenCourse.assignments,
            "students": chosenCourse.students,
            "description": chosenCourse.description,
            "schedule_time": chosenCourse.schedule_time,
            "schedule_days": chosenCourse.schedule_days,
            "syllabus": chosenCourse.syllabus,
            "course_analytics": chosenCourse.course_analytics
        })
    }

    return (
        <React.Fragment>
            <TeacherSidebar />

            <div className="dash-content dash-flex-col" id="teacher-view">

                <div className="class-navbar">
                    <h1>Courses</h1>
                    <div className="btn-navbar">
                        {courses.map((course) => (
                            <Button onClick={() => showCourseInfo(course)}>{course.name}</Button>
                        ))}
                    </div>
                </div>

                <div className="dash-flex-row" id="classes-container">
                    <div className="dash-container" id="students-container">
                        <h3>Students</h3>
                        <table className="students-table">
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>Email</th>
                                </tr>
                            </thead>
                            <tbody>
                                {displayCourse.students.map((student) => (
                                    <tr>
                                        <td>{student.first_name} {student.last_name}</td>
                                        <td><a href="mailto:">{student.email}</a></td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                    <div className="dash-container" id="courses-container">
                        <h3>Class Info</h3>
                        <p><b>Course Name: </b>{displayCourse.name}</p>
                        <p><b>ID: </b>{displayCourse.id}</p>
                        <p><b>Schedule days: </b>{displayCourse.schedule_days}</p>
                        <p><b>Schedule time: </b>{displayCourse.schedule_time}</p>
                        <p>Current syllabus: {displayCourse.syllabus}</p>
                        <UpdateSyllabus courseId={displayCourse.id} />
                    </div>
                </div>
            </div>

        </React.Fragment>
    );
};

export default TeacherCourses;
