import React, { useState } from 'react';
import TaskList from '../components/TaskList';
import TaskForm from '../components/TaskForm';

function Home() {
  const [reload, setReload] = useState(false);

  const handleTaskCreated = () => {
    setReload(r => !r);
  };

  return (
    <div>
      <h1>Tasks</h1>
      <TaskForm onSuccess={handleTaskCreated} />
      <TaskList reload={reload} />
    </div>
  );
}

export default Home;