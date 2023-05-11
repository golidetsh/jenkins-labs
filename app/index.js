const express = require('express');
const app = express();
const home = require('./routes/home')
const logger = require('./middleware/logger');
const morgan = require('morgan');
const facebook = require('./routes/facebook');
var swStats = require('swagger-stats');
const promClient = require('prom-client');

promClient.collectDefaultMetrics();
app.use(swStats.getMiddleware());
const histogram = new promClient.Histogram({
  name: 'response_duration_seconds',
  help: 'The duration in seconds between the response to a request',
  labelNames: ['status_code', 'method', 'path'],
  buckets: [0.02, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10],
});
// histogram.zero({ method: 'GET' });
// histogram.zero({ method: 'POST' });
histogram.observe(10); 
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