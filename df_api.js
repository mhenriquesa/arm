const dialogflow = require('@google-cloud/dialogflow');
require('dotenv').config();

// JSON that you got from GoogleCloud when open account service
const CREDENTIALS = JSON.parse(process.env.CREDENTIALS);

// Your google dialogflow project-id
const PROJECTID = CREDENTIALS.project_id;

const CONFIGURATION = {
    credentials: {
        private_key: CREDENTIALS['private_key'],
        client_email: CREDENTIALS['client_email']
    }
}

const sessionClient = new dialogflow.SessionsClient(CONFIGURATION);

module.exports = detectIntent = async (languageCode, queryText, sessionId) => {

    let sessionPath = sessionClient.projectAgentSessionPath(PROJECTID, sessionId);

    // The text query request.
    let request = {
        session: sessionPath,
        queryInput: {
            text: {
                text: queryText,
                languageCode: languageCode,
            },
        },
    };

    const responses = await sessionClient.detectIntent(request);
    console.log(responses);
    const result = responses[0].queryResult;
    console.log(result);

    return {
        response: result.fulfillmentText
    };
}

