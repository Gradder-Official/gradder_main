import React, { useState } from 'react';
import { Form, Modal, Button } from "react-bootstrap";
import "../assets/styles/manage-courses.css";
import { UpdateSyllabusInputs } from './Interfaces';
import { useForm } from "react-hook-form";
import { BsFileEarmarkPlus } from "react-icons/bs";
import { IconContext } from "react-icons";

const UpdateSyllabus = (courseId: any) => {

    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const { register, handleSubmit } = useForm<UpdateSyllabusInputs>();
    const [selectedFile, setSelectedFile] = useState<string | Blob>('');

    const uploadFile = (event: { target: any; }) => {
        setSelectedFile(event.target.files[0])
        console.log(typeof (event.target.files[0]))
    }

    const updateCourse = (data: UpdateSyllabusInputs) => {

        const updateCourseAPI = "/api/teacher/course/" + courseId["courseId"]

        const sendData = new FormData();
        sendData.append('syllabus_name', data["syllabus_name"]);
        sendData.append('syllabus_file', selectedFile);
        sendData.append('description', data["description"]);

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
            <IconContext.Provider value={{ color: "white", style: { verticalAlign: 'middle' }, size: "1.5em"}}>
                <Button className="update-syllabus-btn" onClick={handleShow}>
                    <BsFileEarmarkPlus /> Update Syllabus
                </Button>
            </IconContext.Provider>

            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Update syllabus</Modal.Title>
                </Modal.Header>
                <Modal.Body>

                    <Form onSubmit={handleSubmit(updateCourse)} className="update-syllabus-form" encType="multipart/form-data">
                        <label>
                            Syllabus name:
                            <input type="text" name="syllabus_name" ref={register} />
                        </label>
                        <label>
                            Upload file:
                            <input
                                type="file" name="syllabus_file"
                                ref={register}
                                onChange={uploadFile}
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
            </Modal>
        </>
    );
}

export default UpdateSyllabus
