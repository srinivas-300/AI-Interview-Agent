import React, { useEffect, useState } from "react";

function AdminHome() {
  const [view, setView] = useState(null);
  const [response, setResponse] = useState("");
  const [jd, setJd] = useState("");
  const [resume, setResume] = useState("");
  const [resultId, setResultId] = useState("");

  const fetchInterviewDetails = () => {
    fetch("http://localhost:8000/interview_details")
      .then((res) => res.json())
      .then((data) => setResponse(data))
      .catch((err) => setResponse("Error fetching interview details."));
  };

  const handleInterviewSetup = async (e) => {
    e.preventDefault();
    setResponse(""); // Clear old data
    try {
      const res = await fetch("http://localhost:8000/interview_setup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ jd, resume }),
      });
      const data = await res.json();
      setResponse(data);
    } catch (err) {
      setResponse("Error submitting interview setup.");
    }
  };

  const handleInterviewResult = async (e) => {
    e.preventDefault();
    setResponse(""); // Clear old data
    try {
      const res = await fetch("http://localhost:8000/interview_result", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: resultId }),
      });
      const data = await res.json();
      setResponse(data);
    } catch (err) {
      setResponse("Error fetching interview result.");
    }
  };

  return (
    <div style={{ padding: "2rem", maxWidth: 800, margin: "auto" }}>
      <h1 style={{ textAlign: "center" }}>Admin Dashboard</h1>

      <div style={{ marginBottom: "1rem", textAlign: "center" }}>
        <button
          onClick={() => {
            setView("setup");
            setResponse("");
          }}
          style={{ margin: "0 0.5rem" }}
        >
          Interview Setup
        </button>

        <button
          onClick={() => {
            setView("details");
            setResponse("");
            fetchInterviewDetails();
          }}
          style={{ margin: "0 0.5rem" }}
        >
          Interview Details
        </button>

        <button
          onClick={() => {
            setView("result");
            setResponse("");
          }}
          style={{ margin: "0 0.5rem" }}
        >
          Interview Result
        </button>
      </div>

      {view === "setup" && (
        <form onSubmit={handleInterviewSetup} style={{ marginBottom: "1rem" }}>
          <h3>Interview Setup</h3>
          <input
            type="text"
            placeholder="Job Description (JD)"
            value={jd}
            onChange={(e) => setJd(e.target.value)}
            style={{ width: "100%", padding: "0.5rem", marginBottom: "0.5rem" }}
          />
          <input
            type="text"
            placeholder="Resume"
            value={resume}
            onChange={(e) => setResume(e.target.value)}
            style={{ width: "100%", padding: "0.5rem", marginBottom: "0.5rem" }}
          />
          <button type="submit">Submit</button>
        </form>
      )}

      {view === "result" && (
        <form onSubmit={handleInterviewResult} style={{ marginBottom: "1rem" }}>
          <h3>Interview Result</h3>
          <input
            type="text"
            placeholder="Enter User ID"
            value={resultId}
            onChange={(e) => setResultId(e.target.value)}
            style={{ width: "100%", padding: "0.5rem", marginBottom: "0.5rem" }}
          />
          <button type="submit">Get Result</button>
        </form>
      )}

      {response && (
        <div style={{ marginTop: "1rem", textAlign: "left" }}>
          <h4>Response:</h4>
          <pre
            style={{
              backgroundColor: "#f5f5f5",
              padding: "1rem",
              borderRadius: "6px",
              overflowX: "auto",
              maxHeight: "400px",
            }}
          >
            {typeof response === "string"
              ? response
              : JSON.stringify(response, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}

export default AdminHome;
