const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

app.post('/calculate', (req, res) => {
  const { num1, num2, operation } = req.body;

  if (typeof num1 !== 'number' || typeof num2 !== 'number' || typeof operation !== 'string') {
    return res.status(400).json({ error: 'Invalid input. num1 and num2 must be numbers, operation must be a string.' });
  }

  let result;
  switch (operation) {
    case 'add':
      result = num1 + num2;
      break;
    case 'subtract':
      result = num1 - num2;
      break;
    case 'multiply':
      result = num1 * num2;
      break;
    case 'divide':
      if (num2 === 0) {
        return res.status(400).json({ error: 'Division by zero.' });
      }
      result = num1 / num2;
      break;
    default:
      return res.status(400).json({ error: 'Invalid operation. Use add, subtract, multiply, or divide.' });
  }

  res.json({ result });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
}); 