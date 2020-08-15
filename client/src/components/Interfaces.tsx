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
    weight?: number,
    id?: string
}

export interface LoginFormInputs {
    email: string,
    password: string,
    remember_me: boolean
};

export interface UpdateSyllabusInputs {
    syllabus_name: string,
    syllabus_file: Blob | string,
    description: string
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

<<<<<<< HEAD
export interface Submission {
    date_submitted: string,
    content: string,
    filenames: string[],
    student_id: string,
    grade?: number,
    id?: string,
}

=======
>>>>>>> feat: :sparkles: Display students and course info for Teachers
export interface studentInfo {
    email: string,
    first_name: string,
    last_name: string,
    password: string,
    courses: [],
    assignments: []
<<<<<<< HEAD
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
=======
>>>>>>> feat: :sparkles: Display students and course info for Teachers
}