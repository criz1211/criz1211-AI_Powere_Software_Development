import axios from 'axios';

const API_URL = 'http://localhost:5000/api/tasks';

export const getTasks = async () => {
    const response = await axios.get(API_URL);
    return response.data;
};

export const createTask = async (task) => {
    const response = await axios.post(API_URL, task);
    return response.data;
};

export const updateTask = async (taskId, updatedTask) => {
    const response = await axios.put(`${API_URL}/${taskId}`, updatedTask);
    return response.data;
};

export const deleteTask = async (taskId) => {
    const response = await axios.delete(`${API_URL}/${taskId}`);
    return response.data;
};