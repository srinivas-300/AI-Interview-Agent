import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Home from "./Home";
import FormPage from "./FormPage";
import Complete from "./Complete";
import InterviewAgent from "./InterviewAgent";
import ResumeParser from "./ResumeParser";
import EndPage from "./EndPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/home" replace />} />
        <Route path="/home" element={<Home />} />
        <Route path="/form" element={<FormPage />} />
        <Route path="/complete" element={<Complete />} />
        <Route path="/interview" element={<InterviewAgent />} />
        <Route path="/resume-parser" element={<ResumeParser />} />
        <Route path="/end" element={<EndPage />} />
      </Routes>
    </Router>
  );
}

export default App;
