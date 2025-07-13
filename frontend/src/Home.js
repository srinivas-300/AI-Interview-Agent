import React from "react";
import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  return (
    <div style={{ textAlign: "center", marginTop: "2rem" }}>
      <h1>Welcome</h1>
      <button onClick={() => navigate("/interview")}>Candidate</button>
      <br /><br />
      <button onClick={() => navigate("/admin_home")}>Admin</button>
    </div>
  );
}

export default Home;
