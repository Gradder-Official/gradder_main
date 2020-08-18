import { ReactNode } from "react";

export interface Props {
    children: ReactNode;
}

export interface student {
    userName: string,
    userType: string;
    loggedIn: boolean;
    dob: string;
}

export interface teacher {
    userName: string,
    userType: string,
    loggedIn: boolean;
    dob: string;
}

export interface assignment {
    title: string,
    date_assigned?: string,
    assigned_by?: string,
    assigned_to: string,
    due_by: string,
    content?: string,
    filenames?: string[],
    estimated_time?: string,
    submissions?: string[],
    id?: string
}

export interface LoginFormInputs {
    email: string,
    password: string,
    remember_me: boolean
};

export interface course {
    id: string,
    name: string,
    assignments: {},
    students: [studentInfo],
    description: string,
    schedule_time: string,
    schedule_days: string,
    syllabus: [string]
}

export interface studentInfo {
    email: string,
    first_name: string,
    last_name: string,
    password: string,
    courses: [],
    assignments: []
}

export interface AssignmentChart {
    "assignment_history": {
        "assignment_name": string,
        "assignment_scores": { "student": string, "score": number }[]
    }[]
}

export interface Events {
    title: string;
    start: string;
    end: string;
    color: string;
    url: string;
}