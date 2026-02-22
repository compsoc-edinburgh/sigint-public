import * as puppeteer from "puppeteer"

async function sleep(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

export async function visit_page(UUID: string, path: string) {
    console.log("Bot visiting: " + path)

    const browser = await puppeteer.launch({
        executablePath: '/usr/bin/chromium-browser',
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-accelerated-2d-canvas',
            '--no-first-run',
            '--no-zygote',
            '--disable-gpu'
        ]
    });

    await browser.setCookie({ // impersonate requester to avoid UUID issues
        name: 'UUID',
        value: UUID,
        domain: "ctf.sigint.mx",
        path: '/',
        sameParty: false,
        expires: -1,
        httpOnly: false,
        secure: false,
        sourceScheme: 'NonSecure',
    });

    await browser.setCookie({
        name: 'flag',
        value: (process.env["FLAG"] || 'SIGINT{dummy-flag}'),
        domain: "ctf.sigint.mx",
        path: '/',
        sameParty: false,
        expires: -1,
        httpOnly: false,
        secure: false,
        sourceScheme: 'NonSecure',
    });

    const page = await browser.newPage();
    try {
    await page.goto("http://ctf.sigint.mx/new-socials/" + path);
    await page.setViewport({width: 1080, height: 1024});
    await sleep(1000);
    } catch {
        console.log("Error visiting page");
    }

    
}
