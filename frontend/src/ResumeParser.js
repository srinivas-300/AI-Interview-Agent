import React, { useEffect, useState } from "react";

function ResumeParser() {
  const [response, setResponse] = useState("Loading...");

  useEffect(() => {
    fetch("http://localhost:8000/resume-parser")
      .then((res) => res.json())
      .then((data) => setResponse(data.message))
      .catch((err) => setResponse("Error fetching data."));
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "2rem" }}>
      <h1>Admin - Resume Parser</h1>
      <p>{response}</p>
    </div>
  );
}

export default ResumeParser;
