const request = require('supertest');
const express = require('express');
const mongoose = require('mongoose');
const { MongoMemoryServer } = require('mongodb-memory-server');
const Task = require('../models/Task');
const taskController = require('./taskController');

let app;
let mongod;

beforeAll(async () => {
  mongod = await MongoMemoryServer.create();
  const uri = mongod.getUri();
  await mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });

  app = express();
  app.use(express.json());
  app.get('/tasks', taskController.getTasks);
  app.post('/tasks', taskController.createTask);
  app.put('/tasks/:id', taskController.updateTask);
  app.delete('/tasks/:id', taskController.deleteTask);
});

afterAll(async () => {
  await mongoose.disconnect();
  await mongod.stop();
});

afterEach(async () => {
  await Task.deleteMany();
});

test('createTask: should create a new task', async () => {
  const res = await request(app)
    .post('/tasks')
    .send({ title: 'Test Task', status: 'pending' });
  expect(res.statusCode).toBe(201);
  expect(res.body.title).toBe('Test Task');
});

test('getTasks: should return all tasks', async () => {
  await Task.create({ title: 'Task 1', status: 'pending' });
  await Task.create({ title: 'Task 2', status: 'completed' });
  const res = await request(app).get('/tasks');
  expect(res.statusCode).toBe(200);
  expect(res.body.length).toBe(2);
});

test('updateTask: should update a task', async () => {
  const task = await Task.create({ title: 'Old Title', status: 'pending' });
  const res = await request(app)
    .put(`/tasks/${task._id}`)
    .send({ title: 'New Title' });
  expect(res.statusCode).toBe(200);
  expect(res.body.title).toBe('New Title');
});

test('deleteTask: should delete a task', async () => {
  const task = await Task.create({ title: 'To Delete', status: 'pending' });
  const res = await request(app).delete(`/tasks/${task._id}`);
  expect(res.statusCode).toBe(200);
  expect(res.body.message).toBe('Task deleted');
});
