require('./df_api');
const express = require('express')

const app = express();

app.use(express.urlencoded({
    extended: true
}));
app.use(express.json())

const PORT = process.env.PORT || 5000;

app.get('/', (req, res) => {
    res.send(`Hello World.!`);
});

app.post('/dialogflow', async (req, res) => {
    let languageCode = req.body.languageCode;
    let queryText = req.body.queryText;
    let sessionId = req.body.sessionId;

    let responseData = await detectIntent(languageCode, queryText, sessionId);
    console.log(responseData)

    res.send(responseData.response);
    return


});

app.listen(PORT, () => {
    console.log(`Server is up and running at ${PORT}`);
});