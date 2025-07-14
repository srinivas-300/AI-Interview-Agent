import React, { useEffect, useState } from "react";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

function AdminHome() {
  const [view, setView] = useState(null);
  const [response, setResponse] = useState("");

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [role, setRole] = useState("");
  const [jd, setJd] = useState("");
  const [resume, setResume] = useState("");

  const [resultId, setResultId] = useState("");

  const fetchInterviewDetails = () => {
    fetch(`${BACKEND_URL}/interview_details`)
      .then((res) => res.json())
      .then((data) => setResponse(data))
      .catch(() => setResponse("Error fetching interview details."));
  };

  const handleInterviewSetup = async (e) => {
    e.preventDefault();
    setResponse("");
    try {
      const res = await fetch(`${BACKEND_URL}/interview_setup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, role, jd, resume }),
      });
      const data = await res.json();
      setResponse(data);
    } catch {
      setResponse("Error submitting interview setup.");
    }
  };

  const handleInterviewResult = async (e) => {
    e.preventDefault();
    setResponse("");
    try {
      const res = await fetch(`${BACKEND_URL}/interview_result`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: resultId }),
      });
      const data = await res.json();
      setResponse(data);
    } catch {
      setResponse("Error fetching interview result.");
    }
  };

  return (
    <div style={{ padding: "2rem", maxWidth: 800, margin: "auto" }}>
      <h1 style={{ textAlign: "center" }}>Admin Dashboard</h1>

      <div style={{ marginBottom: "1rem", textAlign: "center" }}>
        <button onClick={() => { setView("setup"); setResponse(""); }} style={{ margin: "0 0.5rem" }}>
          Interview Setup
        </button>
        <button onClick={() => { setView("details"); setResponse(""); fetchInterviewDetails(); }} style={{ margin: "0 0.5rem" }}>
          Interview Details
        </button>
        <button onClick={() => { setView("result"); setResponse(""); }} style={{ margin: "0 0.5rem" }}>
          Interview Result
        </button>
      </div>

      {view === "setup" && (
        <form onSubmit={handleInterviewSetup} style={{ marginBottom: "1rem" }}>
          <h3>Interview Setup</h3>
          <input type="text" placeholder="Candidate Name" value={name} onChange={(e) => setName(e.target.value)} style={inputStyle} />
          <input type="email" placeholder="Candidate Email" value={email} onChange={(e) => setEmail(e.target.value)} style={inputStyle} />
          <input type="text" placeholder="Role" value={role} onChange={(e) => setRole(e.target.value)} style={inputStyle} />
          <input type="text" placeholder="Job Description (JD)" value={jd} onChange={(e) => setJd(e.target.value)} style={inputStyle} />
          <input type="text" placeholder="Resume" value={resume} onChange={(e) => setResume(e.target.value)} style={inputStyle} />
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
            style={inputStyle}
          />
          <button type="submit">Get Result</button>
        </form>
      )}

      {response && (
        <div style={{ marginTop: "1rem", textAlign: "left" }}>
          <h4>Response:</h4>
          {typeof response === "string" ? (
            <p>{response}</p>
          ) : Array.isArray(response) ? (
            <ul style={{ listStyle: "none", padding: 0 }}>
              {response.map((item, idx) => (
                <li
                  key={idx}
                  style={{
                    backgroundColor: "#f9f9f9",
                    padding: "1rem",
                    marginBottom: "1rem",
                    border: "1px solid #ddd",
                    borderRadius: "6px",
                  }}
                >
                  <p><strong>Name:</strong> {item.name}</p>
                  <p><strong>ID:</strong> {item._id}</p>
                  <p><strong>Role:</strong> {item.role}</p>
                  {item.timestamp && <p><strong>Timestamp:</strong> {item.timestamp}</p>}
                </li>
              ))}
            </ul>
          ) : typeof response === "object" ? (
            <div
              style={{
                backgroundColor: "#f9f9f9",
                padding: "1rem",
                border: "1px solid #ddd",
                borderRadius: "6px",
              }}
            >
              {Object.entries(response).map(([key, val], i) => (
                <p key={i}>
                  <strong>{key.replace(/_/g, " ").replace(/\b\w/g, l => l.toUpperCase())}:</strong> {val}
                </p>
              ))}
            </div>
          ) : null}
        </div>
      )}
    </div>
  );
}

const inputStyle = {
  width: "100%",
  padding: "0.5rem",
  marginBottom: "0.5rem",
};

export default AdminHome;
