import React, { useEffect, useState } from 'react';

const TaskList = ({ reload }) => {
    const [tasks, setTasks] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchTasks = async () => {
            setLoading(true);
            const url = '/api/tasks';
            try {
                const response = await fetch(url);
                const data = await response.json();
                setTasks(Array.isArray(data) ? data : []);
            } catch (error) {
                console.error('Error fetching tasks:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchTasks();
    }, [reload]);

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h2>Task List</h2>
            <table>
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Description</th>
                        <th>Status</th>
                        <th>Due Date</th>
                    </tr>
                </thead>
                <tbody>
                    {tasks.length === 0 ? (
                        <tr>
                            <td colSpan={4} style={{ textAlign: 'center' }}>No tasks found</td>
                        </tr>
                    ) : (
                        tasks.map(task => (
                            <tr key={task._id}>
                                <td>{task.title}</td>
                                <td>{task.description}</td>
                                <td>{task.status}</td>
                                <td>{task.dueDate ? new Date(task.dueDate).toLocaleDateString() : ''}</td>
                            </tr>
                        ))
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default TaskList;