import { useState } from 'react';

function TaskForm({ onSuccess }) {
  const [form, setForm] = useState({
    title: '',
    description: '',
    dueDate: '',
    status: 'pending',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [fieldErrors, setFieldErrors] = useState({});

  const validate = () => {
    const errors = {};
    if (!form.title.trim()) errors.title = 'Title is required';
    return errors;
  };

  const handleChange = e => {
    const { name, value } = e.target;
    setForm(f => ({ ...f, [name]: value }));
    setFieldErrors(fe => ({ ...fe, [name]: undefined }));
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setError('');
    const errors = validate();
    setFieldErrors(errors);
    if (Object.keys(errors).length) return;

    setLoading(true);
    try {
      const payload = {
        ...form,
        dueDate: form.dueDate ? new Date(form.dueDate).toISOString() : undefined,
      };
      console.log('Submitting task:', payload); // Debug print
      const res = await fetch('/api/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      console.log('POST /api/tasks response status:', res.status); // Debug print
      const data = await res.json();
      console.log('POST /api/tasks response data:', data); // Debug print
      if (!res.ok) {
        throw new Error(data.error || 'Failed to create task');
      }
      setForm({ title: '', description: '', dueDate: '', status: 'pending' });
      if (onSuccess) onSuccess();
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>
          Title:
          <input name="title" value={form.title} onChange={handleChange} required />
        </label>
        {fieldErrors.title && <div style={{color: 'red'}}>{fieldErrors.title}</div>}
      </div>
      <div>
        <label>
          Description:
          <input name="description" value={form.description} onChange={handleChange} />
        </label>
      </div>
      <div>
        <label>
          Due Date:
          <input name="dueDate" type="date" value={form.dueDate} onChange={handleChange} />
        </label>
      </div>
      <div>
        <label>
          Status:
          <select name="status" value={form.status} onChange={handleChange}>
            <option value="pending">Pending</option>
            <option value="in-progress">In Progress</option>
            <option value="completed">Completed</option>
          </select>
        </label>
      </div>
      <button type="submit" disabled={loading}>Create Task</button>
      {error && <div style={{color: 'red'}}>{error}</div>}
    </form>
  );
}

export default TaskForm;
