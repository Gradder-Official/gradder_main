import React, { FunctionComponent, useState } from 'react';
import { useHistory } from "react-router-dom";
import { useForm } from "react-hook-form";
import { Form, Button } from 'react-bootstrap';
import { LoginFormInputs } from '../components/Interfaces'
import createBrowserHistory from 'history/createBrowserHistory';
import BlueLogo from '../assets/images/blue-logo.png'
import "../assets/styles/login.css"

const LoginBox: FunctionComponent = () => {

    const { register, handleSubmit, errors } = useForm<LoginFormInputs>();
    const [requestErrors, setRequestErrors] = useState<string>();
    const history = createBrowserHistory({ forceRefresh: true });

    const onSubmit = (data: LoginFormInputs) => {

        // Send form data to API
        fetch('/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        })
            .then(async response => {
                const res = await response.json();
                console.log(res)

                // Check for error response
                if (!response.ok) {
                    const error = (res && res.message) || response.status;
                    return Promise.reject(error);
                } else {

                    sessionStorage.setItem("userName", res['user_info']['userName'])
                    sessionStorage.setItem("userType", res['user_info']['userType'])
                    sessionStorage.setItem("loggedIn", res['user_info']['loggedIn'])
                    sessionStorage.setItem("dob", res['user_info']['dob'])
                    console.log("Fetched data from login API")

                    history.push("/dashboard");
                }
            })
        .catch(error => {
            // Return errors
            console.error('There was an error!', error);
            setRequestErrors("Sorry, there was a problem logging in.")
        });
    };

    return (
        <div className="login-container">
            <img src={BlueLogo} alt="Gradder" className="mobile-login-logo" />
            <h1>Sign In</h1>

            <Form onSubmit={handleSubmit(onSubmit)}>
                <Form.Group controlId="formBasicEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control
                        name="email"
                        type="email"
                        placeholder="Enter email"
                        ref={register({ required: true })}
                    />
                    {errors.email && errors.email.type === "required" && (
                        <div className="error">Please enter your email.</div>
                    )}
                </Form.Group>
                <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                        name="password"
                        type="password"
                        placeholder="Password"
                        ref={register({ required: true })}
                    />
                    {errors.password && errors.password.type === "required" && (
                        <div className="error">Please enter your password.</div>
                    )}
                </Form.Group>
                <Form.Group controlId="formBasicCheckbox">
                    <Form.Check
                        name="remember_me"
                        type="checkbox"
                        label="Remember me?"
                        defaultChecked
                        ref={register}
                    />
                </Form.Group>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>

            <div className="responseError">{requestErrors}</div>

        </div>
    );
};

export default LoginBox;
