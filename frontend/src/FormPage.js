// src/FormPage.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function FormPage() {
  const [name, setName] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch('http://localhost:8000/form', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ name }),
    });
    navigate('/complete');
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '2rem' }}>
      <h1>Form Page</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter your name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <br /><br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default FormPage;
