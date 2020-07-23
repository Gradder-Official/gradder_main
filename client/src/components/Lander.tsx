// NPM Imports
import React, { useEffect, useState } from "react";
import { Container } from "reactstrap";
import { motion } from "framer-motion";
import axios from "axios";

const Lander = () => {
  const [apiRes, setApiRes] = useState({
    hello: "",
  });

  useEffect(() => {
    axios
      .get("/api")
      .then((res) => res.data)
      .then((res) => setApiRes(res));
  }, []);

  return (
    <Container>
      <motion.div
        initial={{ opacity: 0, y: -200 }}
        animate={{ opacity: 1, y: 0 }}
      >
        <h2>AI-driven School Dashboard</h2>
        <h1>Your Smart School Diary</h1>
        <p>The first transparent all-in-one school management system.</p>
        <p>API says: hello: {apiRes.hello}</p>
      </motion.div>
    </Container>
  );
};

export default Lander;
