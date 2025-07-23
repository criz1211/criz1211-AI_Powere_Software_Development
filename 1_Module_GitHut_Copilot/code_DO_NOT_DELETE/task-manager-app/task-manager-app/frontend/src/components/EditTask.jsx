import { useEffect, useState } from 'react';

function EditTask({ taskId, onSuccess }) {
  const [form, setForm] = useState({
    title: '',
    description: '',
    dueDate: '',
    status: 'pending',
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch(`/api/tasks/${taskId}`)
      .then(res => res.json())
      .then(data => {
        setForm({
          title: data.title || '',
          description: data.description || '',
          dueDate: data.dueDate ? data.dueDate.slice(0, 10) : '',
          status: data.status || 'pending',
        });
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [taskId]);

  const handleChange = e => {
    const { name, value } = e.target;
    setForm(f => ({ ...f, [name]: value }));
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const res = await fetch(`/api/tasks/${taskId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      });
      if (!res.ok) throw new Error('Failed to update task');
      if (onSuccess) onSuccess();
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  if (loading) return <div>Loading...</div>;

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Title: <input name="title" value={form.title} onChange={handleChange} required /></label>
      </div>
      <div>
        <label>Description: <input name="description" value={form.description} onChange={handleChange} /></label>
      </div>
      <div>
        <label>Due Date: <input name="dueDate" type="date" value={form.dueDate} onChange={handleChange} /></label>
      </div>
      <div>
        <label>Status:
          <select name="status" value={form.status} onChange={handleChange}>
            <option value="pending">Pending</option>
            <option value="in-progress">In Progress</option>
            <option value="completed">Completed</option>
          </select>
        </label>
      </div>
      <button type="submit" disabled={loading}>Update Task</button>
      {error && <div style={{color: 'red'}}>{error}</div>}
    </form>
  );
}

export default EditTask;
