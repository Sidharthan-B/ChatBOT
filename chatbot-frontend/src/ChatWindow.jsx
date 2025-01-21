import React, { useState } from 'react';
import axios from 'axios';

const ChatWindow = () => {
    const [query, setQuery] = useState('');
    const [response, setResponse] = useState('');

    const handleQuery = async () => {
        try {
            const res = await axios.post('http://localhost:8000/query/', { user_query: query });
            setResponse(res.data.response);
        } catch (error) {
            console.error("Error:", error);
        }
    };

    return (
        <div>
            <textarea onChange={(e) => setQuery(e.target.value)} value={query} />
            <button onClick={handleQuery}>Ask</button>
            <div>{response}</div>
        </div>
    );
};

export default ChatWindow;
