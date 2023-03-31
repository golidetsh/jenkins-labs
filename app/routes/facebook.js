const express = require('express');
const router = express();
const { findPost } = require('../helpers/helper');



router.get('/api/posts', (req, res) => {
   res.send(posts);
});


router.get('/api/posts/:id', (req, res) => {
     const post = findPost(parseInt(req.params.id));
     if(!post) return res.status(404).send(`Post with id ${req.params.id} was not found`);
  
     res.send(post);
   });
 
   
   router.post('/api/posts', (req, res) => {
    const title = req.body.title;
    if(!title || title.length < 5 ) {
        res.status(400).send('Title is required and should be 5 characters minimum');
        return;
    } 
      const post = {
          id: posts.length +1,
          title: req.body.title,
          content: req.body.content,
          published: req.body.published,
          rating: req.body.rating
      };
      posts.push(post);
      res.send(post);
    });

module.exports = router;

