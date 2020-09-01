import React, { FunctionComponent, useState, useEffect } from "react";
import { ResponsiveBar } from "@nivo/bar";
import "../assets/styles/dashboard.css";
import "../assets/styles/analytics.css";
import { AssignmentChart } from "./Interfaces";

const AssignmentScoreChart: FunctionComponent<AssignmentChart> = ({ assignment_history }) => {

    let assignmentScoreData = []

    // Calculate average score for each assignment
    for (var x in assignment_history) {

        let assignment = assignment_history[x]
        let name = assignment["assignment_name"]

        let allAssignmentScores = []

        for (var y in assignment["assignment_scores"]) {
            allAssignmentScores.push(assignment["assignment_scores"][y]["score"])
        }
        let assignmentAverage = allAssignmentScores.reduce((a, b) => (a + b)) / allAssignmentScores.length;

        assignmentScoreData.push({ "assignment_name": name, "assignment_average": assignmentAverage })
    }

    return (
        <div className="assignment-average dash-container">
            <h3>Average score for each assignment</h3>
            <ResponsiveBar
                data={assignmentScoreData}
                indexBy="assignment_name"
                keys={['assignment_average']}
                margin={{ top: 0, right: 50, bottom: 100, left: 100 }}
                padding={0.5}
                layout="horizontal"
                colors={"rgb(90,115,226)"}
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
                    legend: 'Assignments',
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

export default AssignmentScoreChart;
