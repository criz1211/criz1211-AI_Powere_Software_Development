import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import CreateTask from './pages/CreateTask';

const App = () => {
    return (
        <Router>
            <Navbar />
            <main style={{ padding: '1rem' }}>
                <Switch>
                    <Route exact path="/" component={Home} />
                    <Route path="/create" component={CreateTask} />
                </Switch>
            </main>
        </Router>
    );
};

export default App;