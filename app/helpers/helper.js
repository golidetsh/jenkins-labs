const express = require('express');

posts = [
    { id: 1, title: "AI", content: "Top 10 AI tools", published: "true", rating: 1},
    { id: 2, title: "NodeJS", content: "NODEJS in action", published: "true", rating: 4 },
    { id: 3, title: "React", content: "Making of React the documentary", published: "true", rating: 5}
]

function findPost(id) {
    var arr = posts;
    const found = arr.find(c => c.id === id);
    if (found); 
    return found;
  };

module.exports.posts = posts;

module.exports = {
    findPost : findPost
 };