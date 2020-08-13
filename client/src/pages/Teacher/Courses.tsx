import React, { FunctionComponent, useState, useEffect } from "react";
import { teacher, course } from "../../components/Interfaces";
import { useForm } from "react-hook-form";
import "../../assets/styles/dashboard.css";
import "../../assets/styles/assignments.css";
import TeacherSidebar from "../../components/TeacherSidebar";
import { Form, ButtonGroup, Button } from "react-bootstrap";

const TeacherCourses: FunctionComponent<teacher> = ({ userName, userType, loggedIn, dob }) => {

    const blankCourse: course = {
        "id": "",
        "name": "",
        "assignments": {},
        "students": [""],
        "description": "",
        "schedule_time": "",
        "schedule_days": "",
        "syllabus": [""]
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
            "syllabus": chosenCourse.syllabus
        })

        console.log(chosenCourse, displayCourse)
    }

    return (
        <React.Fragment>
            <TeacherSidebar />

            <div className="dash-content">

                <ButtonGroup className="class-navbar">
                    {courses.map((course) => (
                        <Button onClick={() => showCourseInfo(course)}>{course.name}</Button>
                    ))}
                </ButtonGroup>

                <div className="container row" id="classes-container">
                    <div className="jumbotron container" id="students-container">
                        <h3>Students</h3>
                        <table id="students-table" className="hover">
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>Email</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Student name</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div className="jumbotron container" id="className-info-container">
                        <h3>Class Info</h3>
                        <p><b>Name:</b>{displayCourse.name}</p>
                        <p><b>ID:</b>{displayCourse.id}</p>
                        <p><b>Schedule days:</b>{displayCourse.schedule_days}</p>
                        <p><b>Schedule time:</b>{displayCourse.schedule_time}</p>
                        <Form>
                            Current syllabus: {displayCourse.syllabus}
                            Upload new syllabus
                            Submit
                        </Form>
                    </div>
                </div>
            </div>

        </React.Fragment>
    );
};

export default TeacherCourses;
