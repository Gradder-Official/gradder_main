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
    students: [string],
    description: string,
    schedule_time: string,
    schedule_days: string,
    syllabus: [string]
}