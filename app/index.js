const express = require('express');
const app = express();
const home = require('./routes/home')
const logger = require('./middleware/logger');
const morgan = require('morgan');
const facebook = require('./routes/facebook');
var swStats = require('swagger-stats');


app.use(swStats.getMiddleware());
app.use(home);
app.use(facebook);
app.use(logger);


if (app.get('env')  === 'development'){
    app.use(morgan('tiny'));
    console.log('Morgan enabled ...');
  }

  const port = process.env.PORT || 3000;
  const server = app.listen(port, () => console.log(`Listening at port ${port}`));

  module.exports = server;