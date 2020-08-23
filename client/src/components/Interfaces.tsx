export interface student {
    userName: string,
    userType: string;
    loggedIn: boolean;
    dob: string;
}

export interface assignment {
    title: string,
    date_assigned?: string,
    assigned_by?: number,
    assigned_to: string,
    due_by: string,
    content?: [string]
    filenames?: [string],
    estimated_time?: number,
    submissions?: [string],
    _id?: string
}

export interface LoginFormInputs {
    email: string,
    password: string,
};