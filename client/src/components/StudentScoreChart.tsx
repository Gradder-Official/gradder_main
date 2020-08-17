import React, { FunctionComponent, useState, useEffect } from "react";
import { ResponsiveBar } from "@nivo/bar";
import "../assets/styles/dashboard.css";
import "../assets/styles/analytics.css";
import { AssignmentChart } from "./Interfaces";

const StudentScoreChart: FunctionComponent<AssignmentChart> = ({ assignment_history }) => {

    let studentScoreData: Array<{}> = []

    // Get list of students with assignments
    let studentNameList: Array<string> = []
    for (var x in assignment_history) {
        for (var y in assignment_history[x]["assignment_scores"]) {
            let name = assignment_history[x]["assignment_scores"][y]["student"]
            if (studentNameList.includes(name) === false) {
                studentNameList.push(name)
            }
        }
    }

    // Find average score for each student
    for (var studentNumber in studentNameList) {

        let listedStudentName = studentNameList[studentNumber]
        let totalStudentScore = 0
        let no_assignments = 0

        for (var x in assignment_history) {
            no_assignments += 1;
            let assignmentScores = assignment_history[x]["assignment_scores"]
            for (var y in assignmentScores) {
                let name = assignmentScores[y]["student"]
                if (name === listedStudentName) {
                    totalStudentScore += assignmentScores[y]["score"];
                }
            }
        }

        let dictionaryEntry = {
            "student_name": listedStudentName,
            "average_score": totalStudentScore / no_assignments
        }
        console.log(dictionaryEntry)
        studentScoreData.push(dictionaryEntry)
    }

    console.log(studentScoreData)

    return (
        <div className="student-average dash-container">
            <h3>Average score for each student</h3>
            <ResponsiveBar
                data={studentScoreData}
                indexBy="student_name"
                keys={['average_score']}
                margin={{ top: 0, right: 50, bottom: 100, left: 100 }}
                padding={0.5}
                layout="horizontal"
                colors={"rgb(81, 153, 240)"}
                borderColor={{ from: 'color', modifiers: [['darker', 1.6]] }}
                axisTop={null}
                axisRight={null}
                axisBottom={{
                    tickSize: 5,
                    tickPadding: 10,
                    tickRotation: 0,
                    legend: 'Scores',
                    legendPosition: 'middle',
                    legendOffset: 40
                }}
                axisLeft={{
                    tickSize: 5,
                    tickPadding: 10,
                    tickRotation: 0,
                    legend: 'Students',
                    legendPosition: 'middle',
                    legendOffset: -80
                }}
                labelSkipWidth={12}
                labelSkipHeight={12}
                labelTextColor={{ from: 'color', modifiers: [['darker', 1.6]] }}
                legends={[]}
                animate={true}
                motionStiffness={90}
                motionDamping={15}
            />
        </div>
    );
};

export default StudentScoreChart;
