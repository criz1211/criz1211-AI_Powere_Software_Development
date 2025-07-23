import { render, screen, waitFor } from '@testing-library/react';
import TaskList from './TaskList';

beforeEach(() => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () => Promise.resolve([
        { _id: '1', title: 'Task 1', description: 'Desc 1', status: 'pending', dueDate: '2024-06-01T00:00:00Z' },
        { _id: '2', title: 'Task 2', description: 'Desc 2', status: 'completed', dueDate: null },
      ]),
    })
  );
});

afterEach(() => {
  jest.resetAllMocks();
});

test('renders loading then tasks table', async () => {
  render(<TaskList />);
  expect(screen.getByText(/loading/i)).toBeInTheDocument();
  await waitFor(() => expect(screen.getByText('Task 1')).toBeInTheDocument());
  expect(screen.getByText('Task 2')).toBeInTheDocument();
  expect(screen.getAllByRole('row')).toHaveLength(3); // header + 2 tasks
});
