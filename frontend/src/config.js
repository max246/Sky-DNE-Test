const dev = {
    //api: "http://localhost/api/",
    api : 'http://localhost:5050/'
};



const config = dev;
export default {
    // Add common config values here
    MAX_ATTACHMENT_SIZE: 5000000,
    ...config,
};
