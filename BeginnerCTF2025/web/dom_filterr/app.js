const express = require('express');
const crypto = require("crypto");
const createDOMPurify = require('dompurify');
const { JSDOM } = require('jsdom');
const ejs = require('ejs');
// const { bot_visit } = require("./bot.js");

const timeout = 3000;
const app = express();
let connections = {};

var corsOptions = {
        origin: 'https://mini.sigint.mx/'

}

app.use(cors(corsOptions));

app.use(express.urlencoded({ extended: false }));

// load cookies
app.use((req, res, next) => {
    const { headers: { cookie } } = req;
    if (cookie) {
        const values = cookie.split(';').reduce((res, item) => {
            const data = item.trim().split('=');
            return { ...res, [data[0]]: decodeURIComponent(data[1]) };
        }, {});
        req.cookies = values;
    }
    else req.cookies = {};
    next();
});

app.use((req, res, next) => {
    const sessionId = req.cookies.sessionId;

    if (sessionId) {
        if (!connections[sessionId]) {
            connections[sessionId] = { lastConnection: Date.now() - timeout, lastTicket: "" };
        }
        next();
    }
    else {
        uuid = crypto.randomUUID();  // let user imidiately retry with new session
        connections[uuid] = { lastConnection: Date.now() - timeout, lastTicket: "" };
        res.cookie("sessionId", uuid);
        res.redirect("./");
        console.log("New session created: " + uuid);
    }
});


app.route('/view').get((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');

    lastTicket = connections[req.cookies.sessionId];
    if (lastTicket.lastTicket === "") {
        res.end(`
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; background: #f9f9f9; }
                    h1 { color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }
                    a { color: #007bff; text-decoration: none; }
                    a:hover { text-decoration: underline; }
                </style>
            </head>
            <body>
                No ticket submitted yet. <a href='./'>Go back</a>
            </body>
            </html>
        `);
        return;
    }


    const window = new JSDOM('').window;

    const DOMPurify = createDOMPurify(window);

    let filteredTicket = DOMPurify.sanitize(lastTicket.lastTicket, {
        SAFE_FOR_TEMPLATES: false,
    });

    filteredTicket = filteredTicket.replace("&lt;%", "<%");
    filteredTicket = filteredTicket.replace("%&gt;", "%>");

    console.log(filteredTicket);
    const html = ejs.render(
        `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; background: #f9f9f9; }
                h1 { color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }
                .ticket-box { border: 1px solid #ccc; padding: 15px; background: #f5f5f5; border-radius: 4px; margin: 20px 0; }
                input { width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
                a { color: #007bff; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <h1>Admin Panel</h1>
            <p>Reviewing Last Ticket:</p>
            <div class="ticket-box">
                <p><strong>Ticket Content:</strong></p>
                <input type="text" value="${filteredTicket}" />
            </div>
            <a href="./">Back</a>
        </body>
        </html>
    `
    )


    res.end(html);
    return;
});

app.route('/submit').get((req, res) => { res.redirect("./"); })
app.route('/submit').post((req, res) => {
    let ticketBody = req.body.message

    let error = (() => {
        if (!ticketBody)
            return "No message provided. <a href='./'>Go back</a>";
        if (ticketBody.length > 500)
            return "Message too long. <a href='./'>Go back</a>";
        if (Date.now() - connections[req.cookies.sessionId].lastConnection < timeout)
            return "Please wait before submitting another ticket. <a href='./'>Go back</a>";
        return null;
    })();

    if (error !== null) {
        res.statusCode = 400;
        res.end(error);
        return;
    }

    connections[req.cookies.sessionId].lastTicket = ticketBody;
    connections[req.cookies.sessionId].lastConnection = Date.now();
    console.log(req.cookies.sessionId + " submitted a ticket");
    res.redirect("./view");
});


app.route('/').get((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    res.end(`
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; background: #f9f9f9; }
                h1 { color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }
                textarea { padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-family: Arial; }
                button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
                button:hover { background: #0056b3; }
                small { color: #666; }
            </style>
        </head>
        <body>
            <h1>Support Portal</h1>
            <p>Submit your issue below. An admin will review your ticket shortly.</p>
            <form action="./submit" method="POST">
                <textarea name="message" placeholder="Describe your issue..." style="width: 100%; height: 150px;"></textarea><br><br>
                <button type="submit">Submit Ticket to Admin</button>
            </form>
            <p><small>Note: The admin views your ticket in a special panel.</small></p>
        </body>
        </html>
    `);
});


app.listen(3000,
    () => { console.log(`Server running on port: 3000`) }
);
