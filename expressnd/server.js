// import http from 'http';
// import { tasks } from './tasks.js';

//req = request, res = response

// const server = http.createServer((req, res) => { 
// if (req.url === '/tasks' &&req.method === 'GET') {
//     res.writeHead(200, {'Content-type': 'application/json'});
//     res.end(JSON.stringify(tasks));
// } else {
//     res.writeHead(404, {'Content-type': 'application/json'});
//     res.end(JSON.stringify({message: 'Not found'}));
// }
// });

// server.listen(3000)
// console.log('Server running on port 3000!!!');


// const server = express();

const express = require('express');
const inventory = require('./inventory.js')

const server = express();

server.use(express.json()); //this automates the parsing of JSON body

server.use(express.static('public')); //needed to connect to frontend

server.get('/inventory', (req, res) => {
    res.json(inventory);
});

server.post('/inventory', (req, res) => {
    const newItem = req.body;
    newItem.id = inventory.length + 1;
    inventory.push(newItem);
    res.json({message: 'Product added', item: newItem});
});

server.put('/inventory/:id', (req, res) => { //id is a parameter means that route is dynamic
    const id = Number(req.params.id); //params is an object that contains all the parameters in the route
    const item = inventory.find((item) => item.id === id)

    if (!item) {
        res.status(404).json({message: 'Item not found'});
    } else {
        Object.assign(item, req.body); //this updates the item with the new data from the request body
        res.json({message: 'item updated', item});
    }
});

server.delete('/inventory/:id', (req, res) => {
    const id = Number(req.params.id);
    const index = inventory.findIndex((item) => item.id === id );

    if (index === -1) {
        return res.status(404).json({message: 'Item not found'});
    }
    const deletedItem = inventory.splice(index, 1) [0]; 
    res.json({message: 'Item Deleted', item: deletedItem});
});

server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
