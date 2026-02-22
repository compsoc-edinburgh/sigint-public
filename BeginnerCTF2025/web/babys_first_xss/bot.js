const puppeteer = require('puppeteer');

const FLAG = process.env.FLAG || "mini{fake_flag}";
const PAGE_URL = "http://localhost:5000/";

function bot_visit(uuid) {
    // spawn a background thread to visit the page
    setImmediate(() => {
        __visit(uuid).catch(err => console.error("Bot visit error:", err));
    });
}

async function __visit(uuid) {
    try {
        const browser = await puppeteer.launch({headless: "new", args: ['--no-sandbox', '--disable-setuid-sandbox']});
        const page = await browser.newPage();
        
        await page.setCookie({name: "sessionId", value: uuid,  url: PAGE_URL, expires: -1, httpOnly: false, secure: false, sourceScheme: 'NonSecure',});
        await page.setCookie({name: "flag", value: FLAG,  url: PAGE_URL, expires: -1, httpOnly: false, secure: false, sourceScheme: 'NonSecure',});
        
        await page.goto(PAGE_URL + "view", {waitUntil: 'networkidle2', timeout: 3000}); // wait for the page to load
        await browser.close();
        console.log(`Bot visited /view with sessionId: ${uuid}`);
    } catch (err) {
        console.error(`Bot error for ${uuid}:`, err.message);
    }
}

module.exports = { bot_visit };
