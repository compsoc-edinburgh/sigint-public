import { IncomingMessage, ServerResponse } from 'http';
import * as http from 'http';
import * as fs from 'fs';
import * as path from 'path';

import * as handle from './handlers';
import { createUser } from './filesystem';

type Handler = (req: IncomingMessage, res: ServerResponse) => void;
export const GUIDS: string[] = [];

function parseCookies(cookieHeader: string): Record<string, string> {
    const cookies: Record<string, string> = {};
    cookieHeader.split(';').forEach(cookie => {
        const [name, value] = cookie.trim().split('=');
        cookies[name] = value;
    });
    return cookies;
}

function try_gen_new_UUID(req: IncomingMessage) {
    if (!req.headers.cookie) {
        return crypto.randomUUID()
    }
    let cookies = parseCookies(req.headers.cookie);
    if (!cookies.UUID) {
        return crypto.randomUUID();
    }
    if (!GUIDS.includes(cookies.UUID)) {
        return crypto.randomUUID();
    }
    return null;
}

const handlers: Record<string, Handler> = {
    '/': handle.rawFile('../src/home.html', 'text/html'),
    '/new-post': handle.rawFile('../src/new-post.html', 'text/html'),
    '/post': handle.rawFile('../src/specific-post.html', 'text/html'),
    '/style-1.css': handle.rawFile('../src/style-1.css', 'text/css'),
};

const postsDir = path.join(__dirname, 'posts');
if (!fs.existsSync(postsDir)) {
    fs.mkdirSync(postsDir, { recursive: true });
}

const server = http.createServer((req, res) => {
    let UUID: string | null = try_gen_new_UUID(req);
    if (UUID) {
        res.setHeader('Set-Cookie', `UUID=${UUID}; HttpOnly`);
        if (!createUser(UUID)) {
            return;
        }
        GUIDS.push(UUID);
        
    } else {
        let cookies = parseCookies(req.headers.cookie || '');
        UUID = cookies.UUID;
    }

    if (req.url?.startsWith('/api/')) {
        handle.api(req, res, UUID);
        return;
    }

    const url = new URL(req.url || '', `http://${req.headers.host}`);

    console.log("Received request for:", url.pathname);

    const handler = handlers[url.pathname || ''];
    if (handler) {
        handler(req, res);
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
});


const PORT = 3001;
const HOST = '0.0.0.0';
server.listen(PORT, HOST, () => {
    console.log(`Server running at http://${HOST}:${PORT}/`);
});