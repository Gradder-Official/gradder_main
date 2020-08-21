import React, { useState, ChangeEvent } from 'react';
import { Form, Modal, Button } from "react-bootstrap";
import "../assets/styles/manage-courses.css";
import { UpdateSyllabusInputs } from './Interfaces';
import { useForm } from "react-hook-form";


function UpdateSyllabus(courseId: any) {

    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const { register, handleSubmit } = useForm<UpdateSyllabusInputs>();

    const updateCourse = (data: UpdateSyllabusInputs) => {

        const updateCourseAPI = "/api/teacher/course/" + courseId["courseId"]

        const sendData = new FormData();
        sendData.append('syllabus_name', data.syllabus_name);
        sendData.append('syllabus_file', data.syllabus_file);
        sendData.append('description', data.description);
        console.log(data)

        fetch(updateCourseAPI, {
            method: 'POST',
            body: sendData,
        })
            .then(async response => {
                const res = await response.json();
                // Check for error response
                if (!response.ok) {
                    const error = (res && res.message) || response.status;
                    return Promise.reject(error);
                }
            })
            .catch(error => {
                // Return errors
                console.error('There was an error!', error);
            });

        handleClose();
    }

    return (
        <>
            <Button className="update-syllabus-btn" onClick={handleShow}>
                Update Syllabus
            </Button>

            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Update syllabus</Modal.Title>
                </Modal.Header>
                <Modal.Body>

                    <Form onSubmit={handleSubmit(updateCourse)} className="update-syllabus-form">
                        <label>
                            Syllabus name:
                            <input type="text" name="syllabus_name" ref={register} />
                        </label>
                        <label>
                            Upload file:
                            <input accept="image/*,.pdf,.doc,.docx,.xls,.xlsx"
                                type="file" name="syllabus_file"
                                ref={register}
                            />
                        </label>
                        <label>
                            Description:
                            <input type="text" name="description" ref={register} />
                        </label>
                        <Button variant="primary" type="submit">
                            Submit
                        </Button>
                    </Form>

                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>
        </>
    );
}

export default UpdateSyllabus