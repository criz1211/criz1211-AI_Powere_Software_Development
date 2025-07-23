const mongoose = require('mongoose');

const TaskSchema = new mongoose.Schema({
  title: { type: String, required: [true, 'Title is required'] },
  description: String,
  status: {
    type: String,
    enum: {
      values: ['pending', 'in-progress', 'completed'],
      message: 'Status must be pending, in-progress, or completed'
    },
    default: 'pending'
  },
  dueDate: Date,
}, { timestamps: true });

module.exports = mongoose.model('Task', TaskSchema);
