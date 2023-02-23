const express = require('express');
const app = express();
const home = require('./routes/home')
const logger = require('./middleware/logger');
const morgan = require('morgan');
const facebook = require('./routes/facebook');

app.use(home);
app.use(facebook);
app.use(logger);


if (app.get('env')  === 'development'){
    app.use(morgan('tiny'));
    console.log('Morgan enabled ...');
  }


app.listen(3000, () => console.log ('Listening on port 3000 ...'));