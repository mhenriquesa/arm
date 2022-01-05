const axios = require('axios');
const fs = require('fs');

const { Client, Location, List, Buttons } = require('whatsapp-web.js');

const SESSION_FILE_PATH = './session.json';
let sessionCfg;
if (fs.existsSync(SESSION_FILE_PATH)) {
    sessionCfg = require(SESSION_FILE_PATH);
}

const client = new Client({ puppeteer: { headless: false }, session: sessionCfg });

client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.initialize();

client.on('message', message => {
    axios.post('http://192.168.0.43:5000/dialogflow', {
        languageCode: 'pt-BR',
        queryText: message.body,
        sessionId: message.from
    })
    .then(res => {
        client.sendMessage(message.from, res.data)
    })
    .catch(error => {
        console.error(error)
    })
});
// message.reply(res.data);

