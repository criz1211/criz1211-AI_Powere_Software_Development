# Task Manager App - Backend

This is the backend part of the Task Manager application built with Node.js, Express, and MongoDB.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [License](#license)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the backend directory:
   ```
   cd task-manager-app/backend
   ```

3. Install the dependencies:
   ```
   npm install
   ```

4. Set up your MongoDB database and update the connection string in `src/config/db.js`.

## Usage

To start the server, run:
```
npm start
```

The server will run on `http://localhost:5000` by default.

## API Endpoints

- `POST /tasks` - Create a new task
- `GET /tasks` - Retrieve all tasks
- `PUT /tasks/:id` - Update a task by ID
- `DELETE /tasks/:id` - Delete a task by ID

## Technologies Used

- Node.js
- Express
- MongoDB
- Mongoose

## License

This project is licensed under the MIT License.