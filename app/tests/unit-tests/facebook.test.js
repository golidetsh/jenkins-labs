const request = require('supertest');
const { posts } = require('../../helpers/helper');
let server;

describe('/api/posts', () => {

    beforeEach(() => { server = require('../../index'); })
    afterEach(async () => { server.close();}) 

  describe('GET /', ()=> {
    it('should return all posts', async () =>{
       //returns a promise so we add await
      const res = await request(server).get('/api/posts/');  
      expect(res.status).toBe(200);
    });
  });

  describe('GET /', ()=> {
    it('should return status 404 if invalid ID is passed', async () =>{
      const res = await request(server).get('/api/posts/99');  
      expect(res.status).toBe(404);
    });
  });

});