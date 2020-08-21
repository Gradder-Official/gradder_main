import React, { FunctionComponent, useState, useEffect } from "react";
import { teacher, course } from "../../components/Interfaces";
import TeacherSidebar from "../../components/TeacherSidebar";
import { ButtonGroup, Button } from "react-bootstrap";
import "../../assets/styles/dashboard.css";
import "../../assets/styles/analytics.css";
import AssignmentScoreChart from "../../components/AssignmentScoreChart";
import StudentScoreChart from "../../components/StudentScoreChart";

const TeacherAnalytics: FunctionComponent<teacher> = ({ userName, userType, loggedIn, dob }) => {

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

    // TO DO: Link up once grading functionality is finished

    const sampleAnalyticsData = {
        "total_average": 82,
        "starting_average": 74,
        "no_students": 2,
        "assignment_history": [
            {
                "assignment_name": "Essay 1",
                "assignment_scores": [
                    { "student": "Student 1", "score": 84 },
                    { "student": "Student 2", "score": 80 }
                ]
            },
            {
                "assignment_name": "Essay 2",
                "assignment_scores": [
                    { "student": "Student 1", "score": 55 },
                    { "student": "Student 2", "score": 83 }
                ]
            },
            {
                "assignment_name": "Essay 3",
                "assignment_scores": [
                    { "student": "Student 1", "score": 99 },
                    { "student": "Student 2", "score": 78 }
                ]
            }
        ]
    }

    const [analyticsData, setAnalyticsData] = useState(sampleAnalyticsData)

    function showCourseInfo(chosenCourse: course) {
        fetch('/api/teacher/courses')
            .then(res => res.json()).then(response => {
                setAnalyticsData(response['data']['course_analytics']);
            }
        )
    }

    return (
        <React.Fragment>
            <TeacherSidebar />

            <div className="dash-content dash-flex-col">

                <div className="class-navbar">
                    <h1>Analytics</h1>
                    <ButtonGroup>
                        {courses.map((course) => (
                            <Button onClick={() => showCourseInfo(course)}>{course.name}</Button>
                        ))}
                    </ButtonGroup>
                </div>

                <div className="dash-flex-col" id="analytics">
                    <div className="analytics-averages dash-flex-row">
                        <div className="dash-container">
                            <h3>Students</h3>
                            <h1>{analyticsData["no_students"]}</h1>
                        </div>
                        <div className="dash-container">
                            <h3>Overall average</h3>
                            <h1>{analyticsData["total_average"]}</h1>
                        </div>
                        <div className="dash-container">
                            <h3>Starting average</h3>
                            <h1>{analyticsData["starting_average"]}</h1>
                        </div>
                    </div>
                    <div className="analytics-charts dash-flex-row">
                        <AssignmentScoreChart assignment_history={analyticsData["assignment_history"]} />
                        <StudentScoreChart assignment_history={analyticsData["assignment_history"]} />
                    </div>
                </div>
            </div>

        </React.Fragment>
    );
};

export default TeacherAnalytics;
