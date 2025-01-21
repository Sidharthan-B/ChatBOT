import React, { useState } from 'react';
import axios from 'axios';

const ReminderForm = () => {
    const [message, setMessage] = useState('');
    const [time, setTime] = useState('');

    const handleSetReminder = async () => {
        try {
            const res = await axios.post('http://localhost:8000/reminder/', { message, time });
            alert(res.data.status);
        } catch (error) {
            console.error("Error:", error);
        }
    };

    return (
        <div>
            <input type="text" placeholder="Reminder message" onChange={(e) => setMessage(e.target.value)} />
            <input type="datetime-local" onChange={(e) => setTime(e.target.value)} />
            <button onClick={handleSetReminder}>Set Reminder</button>
        </div>
    );
};

export default ReminderForm;
