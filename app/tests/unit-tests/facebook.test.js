const request = require('supertest');
const { posts } = require('../../helpers/helper');
let server;

describe('/api/posts', () => {

    beforeEach(() => { server = require('../../index'); })
    afterEach(async () => { server.close();}) 

  describe('GET /', ()=> {
    it('should return all posts', async () =>{
       //returns a promise so we add await
      const res = await request(server).get('/api/posts');  
      expect(res.status).toBe(200);
    });
  });

});