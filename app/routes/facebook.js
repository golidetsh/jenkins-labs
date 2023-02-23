const express = require('express');
const { posts } = require('../helpers/helper');
const router = express();



router.get('/api/posts', (req, res) => {
   res.send(posts);
});


module.exports = router;

