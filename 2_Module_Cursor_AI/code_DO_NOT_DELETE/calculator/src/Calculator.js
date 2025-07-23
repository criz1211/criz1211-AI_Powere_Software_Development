import React, { useState } from 'react';

const API_BASE = 'http://localhost:5050';

const Calculator = () => {
  const [displayValue, setDisplayValue] = useState('0');
  const [num1, setNum1] = useState(null);
  const [operation, setOperation] = useState(null);
  const [waitingForNum2, setWaitingForNum2] = useState(false);

  const handleButtonClick = (value) => {
    if (/[0-9]/.test(value)) {
      if (waitingForNum2) {
        setDisplayValue(value);
        setWaitingForNum2(false);
      } else {
        setDisplayValue((prev) => (prev === '0' ? value : prev + value));
      }
    } else if (value === '.') {
      const parts = displayValue.split(/([+\-*/])/);
      const lastPart = parts[parts.length - 1];
      if (!lastPart.includes('.')) {
        setDisplayValue(displayValue + value);
      }
    } else if (['+', '-', '*', '/'].includes(value)) {
      if (operation && !waitingForNum2) {
        // If an operation is already set, perform calculation first
        performCalculation(num1, operation, parseFloat(displayValue));
        setOperation(value);
        setWaitingForNum2(true);
        setNum1(parseFloat(displayValue));
      } else {
        setOperation(value);
        setNum1(parseFloat(displayValue));
        setWaitingForNum2(true);
      }
    } else if (value === '=') {
      if (operation && num1 !== null) {
        performCalculation(num1, operation, parseFloat(displayValue));
        setOperation(null);
        setNum1(null);
        setWaitingForNum2(false);
      }
    } else if (value === 'C') {
      setDisplayValue('0');
      setNum1(null);
      setOperation(null);
      setWaitingForNum2(false);
    }
  };

  const performCalculation = async (num1, operation, num2) => {
    const opWord = opToWord(operation);
    try {
      const response = await fetch(`${API_BASE}/${opWord}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ a: num1, b: num2 }),
      });
      const data = await response.json();
      if (!response.ok) {
        setDisplayValue('Err');
        return;
      }
      setDisplayValue(String(data.result));
    } catch (error) {
      setDisplayValue('Err');
    }
  };

  // Convert operator symbol to backend operation word
  const opToWord = (op) => {
    switch (op) {
      case '+': return 'add';
      case '-': return 'subtract';
      case '*': return 'multiply';
      case '/': return 'divide';
      default: return '';
    }
  };

  return (
    <div className="calculator">
      <div className="display">{displayValue}</div>
      <div className="button-grid">
        <button onClick={() => handleButtonClick('7')}>7</button>
        <button onClick={() => handleButtonClick('8')}>8</button>
        <button onClick={() => handleButtonClick('9')}>9</button>
        <button onClick={() => handleButtonClick('/')}>/</button>
        <button onClick={() => handleButtonClick('4')}>4</button>
        <button onClick={() => handleButtonClick('5')}>5</button>
        <button onClick={() => handleButtonClick('6')}>6</button>
        <button onClick={() => handleButtonClick('*')}>*</button>
        <button onClick={() => handleButtonClick('1')}>1</button>
        <button onClick={() => handleButtonClick('2')}>2</button>
        <button onClick={() => handleButtonClick('3')}>3</button>
        <button onClick={() => handleButtonClick('-')}>-</button>
        <button onClick={() => handleButtonClick('0')}>0</button>
        <button onClick={() => handleButtonClick('.')}>.</button>
        <button onClick={() => handleButtonClick('=')}>=</button>
        <button onClick={() => handleButtonClick('+')}>+</button>
        <button onClick={() => handleButtonClick('C')}>C</button>
      </div>
    </div>
  );
};

export default Calculator; 