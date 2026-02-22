import { IncomingMessage, ServerResponse } from 'http';
import * as filesystem from './filesystem';
import * as bot from './bot'
import * as fs from 'fs';
import * as path from 'path';


export const rawFile = (filePath: string, type: string): (req: IncomingMessage, res: ServerResponse) => void => {
    return (req: IncomingMessage, res: ServerResponse) => {
        res.writeHead(200, { 'Content-Type': type});
        res.end(filesystem.loadFile(filePath));
    };
}

function handleNewPost(req: IncomingMessage, res: ServerResponse, params: URLSearchParams, UUID: string) {
    const pTitle = params.get('title');
    const pContent = params.get('content');
    if (pTitle && pContent && pTitle.trim() !== '' && pContent.trim() !== '') {
        if (pTitle.length > 100 || pContent.length > 1000) {
            res.writeHead(400, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Title or content too long' }));
            return;
        }

        const newPost = {
            id: filesystem.userPostCount(UUID),
            title: pTitle,
            content: pContent,
            date: new Date().toISOString()
        };
        console.log("New post created:", newPost);
        if (filesystem.savePost(UUID, newPost)) {
            res.writeHead(201, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify(newPost));
        } else {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Failed to save post' }));
        }
    }
    else {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Missing title or content' }));
    }
}

function handleSpecificPost(req: IncomingMessage, res: ServerResponse, params: URLSearchParams, UUID: string) {
    const postId = params.get('id');
    if (postId) {
        const post = filesystem.getPost(UUID, postId);
        if (post) {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify(post));
        } else {
            res.writeHead(404, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Post not found' }));
        }
    } else {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Missing post ID' }));
    }
}

function handlePosts(req: IncomingMessage, res: ServerResponse, UUID: string) {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    const posts = filesystem.getAllPosts(UUID);
    console.log("Returning posts for UUID:", UUID, "Posts count:", posts.length);
    res.end(JSON.stringify(posts));
}

export function api (req: IncomingMessage, res: ServerResponse, UUID: string) {
    const {resource, params, url}  = ((url: string) => {
        const decoded_url = new URL(url, `http://${req.headers.host}`);
        const resource = decoded_url.pathname.split("/").pop();
        const params = new URLSearchParams(decoded_url.search);
        return { resource, params, url: decoded_url };
    })(req.url || '');

    

    console.log("Request for API:'" + resource + "' with params: '" + params.toString() + "' uuid: '" + UUID + "'");

    if (resource === 'posts') {
        handlePosts(req, res, UUID);
    } else if (resource === 'new-post') {
        handleNewPost(req, res, params, UUID);
    } else if (resource === 'post') {
        handleSpecificPost(req, res, params, UUID);
    } else if (resource === 'report') {
        const id = parseInt(params.get('id') || '9999999999999999999', 10);
        if (isNaN(id) || id < 0) {
            res.writeHead(400, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Invalid post ID' }));
            return;
        }
        if (filesystem.getPost(UUID, id.toString()) === null) {
            return;
        }
        res.writeHead(200);
        res.end();
        bot.visit_page(UUID, `post?id=${id}`);
    } else {
        res.writeHead(404, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ message: 'API endpoint not found' }));
    }

}