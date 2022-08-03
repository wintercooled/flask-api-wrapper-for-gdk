// Make a directory to run the file from and move into it:
//mkdir nodejs-call-flask-gdk-wrapper
//cd nodejs-call-flask-gdk-wrapper

// Initliaze npm:
//npm init --yes
//npm install request --save

// Move this file into that folder and run the example:
//node example_client_nodejs.js

const request = require('request');

// We will call one endpoint in this example, the example endpoint that checks
// that the authorization is working. You can then add the other endpoints using
// this as a template. Remember to change the authorization tokens in your
// version of the API and then amend them here accordingly!
api_test_endpoint = "http://127.0.0.1:5000/api/v1/example_auth";

let options = {
    url: api_test_endpoint,
    method: "get",  
    headers:
    { 
     "content-type": "application/json",
     "Authorization": "9becbfcf-7eca-4d58-baa1-855c3034dbfe",
    }
};

request(options, (error, response, body) => {
    if (error) {
        console.error('An error occurred: ', error);
    } else {
        json = JSON.parse(body);
        console.log(json);
    }
});

// You should see the following JSON returned:
//{ example_key: 'example_value' }

