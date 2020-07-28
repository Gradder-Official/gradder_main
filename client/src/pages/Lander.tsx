// NPM Imports
import React, { useEffect, useState, FunctionComponent } from 'react';
import { Container } from 'reactstrap';
import { motion } from 'framer-motion';
import axios from 'axios';

interface testAPIRes {
  hello: string;
}

const Lander: FunctionComponent = () => {
  const [apiRes, setApiRes] = useState<testAPIRes>({
    hello: '',
  });

  useEffect(() => {
    axios
      .get('/api')
      .then((res: any) => res.data)
      .then((res: any) => setApiRes(res));
  }, []);

  return (
    <Container>
      <motion.div initial={{ opacity: 0, y: -200 }} animate={{ opacity: 1, y: 0 }}>
        <h2>AI-driven School Dashboard</h2>
        <h1>Your Smart School Diary</h1>
        <p>The first transparent all-in-one school management system.</p>
        <p>API says: hello: {apiRes.hello}</p>
      </motion.div>
    </Container>
  );
};

export default Lander;
