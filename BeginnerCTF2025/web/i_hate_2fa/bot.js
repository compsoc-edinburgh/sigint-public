const puppeteer = require('puppeteer');
const crypto = require('crypto');

const ADMIN_PASSWORD = crypto.randomBytes(64).toString('hex');

async function adminBot(targetUrl) {
    const browser = await puppeteer.launch({
        headless: "new",
        args: ['--no-sandbox']
    });
    const page = await browser.newPage();
    page.on('console', msg => {
        console.log(`[BROWSER CONSOLE] ${msg.type().toUpperCase()}: ${msg.text()}`);
    });
    page.on('pageerror', err => {
        console.log(`[BROWSER PAGE ERROR] ${err.toString()}`);
    });

    page.on('requestfailed', request => {
        console.log(`[BROWSER REQ FAIL] ${request.url()} - ${request.failure().errorText}`);
    });

    try {
        console.log("Admin is logging in...");
        console.log("password:", ADMIN_PASSWORD);
        await page.goto('http://localhost:3000/login', { waitUntil: 'networkidle0' });
        await page.type('input[name="username"]', 'admin');
        await page.type('input[name="password"]', ADMIN_PASSWORD);
        await Promise.all([
            page.click('button[type="submit"]'),
            page.waitForNavigation({ waitUntil: 'networkidle0' }),
        ]);

        console.log(`Admin visiting reported status: ${targetUrl}`);
        await page.goto(targetUrl, { waitUntil: 'domcontentloaded', timeout: 10000 });

        // Admin stays on page to allow JS/form submissions
        await new Promise(resolve => setTimeout(resolve, 5000));

    } catch (e) {
        console.error("Bot encountered an error:", e.message);
    } finally {
        await browser.close();
        console.log("Admin session ended.");
    }
}

function visitStatus(targetUrl) {
    // spawn a background task to visit the page
    setImmediate(() => {
        adminBot(targetUrl).catch(err => console.error("Bot visit error:", err));
    });
}

module.exports = { adminBot, visitStatus, ADMIN_PASSWORD };
