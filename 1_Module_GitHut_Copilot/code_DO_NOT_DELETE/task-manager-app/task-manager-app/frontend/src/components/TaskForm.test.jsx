import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import TaskForm from './TaskForm';

beforeEach(() => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      ok: true,
      json: () => Promise.resolve({}),
    })
  );
});

afterEach(() => {
  jest.resetAllMocks();
});

test('shows error if title is empty', async () => {
  render(<TaskForm />);
  fireEvent.click(screen.getByText(/create task/i));
  expect(await screen.findByText(/title is required/i)).toBeInTheDocument();
});

test('submits form with valid data', async () => {
  const onSuccess = jest.fn();
  render(<TaskForm onSuccess={onSuccess} />);
  fireEvent.change(screen.getByLabelText(/title/i), { target: { value: 'My Task', name: 'title' } });
  fireEvent.click(screen.getByText(/create task/i));
  await waitFor(() => expect(onSuccess).toHaveBeenCalled());
});
