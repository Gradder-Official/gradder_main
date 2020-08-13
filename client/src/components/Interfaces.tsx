export interface student {
    userName: string,
    userType: string;
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

export interface course {
    name: string
    daysOfWeek: string
    startTime: string
}
