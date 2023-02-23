const express = require('express');
const { posts, findPost } = require('../helpers/helper');
const router = express();



router.get('/api/posts', (req, res) => {
   res.send(posts);
});


router.get('/api/posts/:id', (req, res) => {
     const post = findPost(parseInt(req.params.id));
     if(!post) return res.status(404).send(`Post with id ${req.params.id} was not found`);
  
     res.send(post);
   });
  

module.exports = router;

