// NPM Imports
import React from "react";
import { Switch, BrowserRouter as Router, Route } from "react-router-dom";

// Components
import Lander from "./components/Lander";

// Stylesheets
import "bootstrap/dist/css/bootstrap.min.css";

const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Lander} />
      </Switch>
    </Router>
  );
};

export default App;
