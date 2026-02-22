import * as fs from 'fs';
import * as path from 'path';

export function loadFile(filePath: string): string {
    const fullPath = path.join(__dirname, filePath);
    if (fs.existsSync(fullPath)) {
        return fs.readFileSync(fullPath, 'utf-8');
    }
    return '<file not found>';
}

export function createUser(UUID: string): boolean {
    const userDir = path.join(__dirname, 'posts', UUID);
    if (!fs.existsSync(userDir)) {
        fs.mkdirSync(userDir, { recursive: true });
        return true;
    }
    return false;
}

export function userPostCount(UUID: string): number {
    const userDir = path.join(__dirname, 'posts', UUID);
    if (fs.existsSync(userDir)) {
        return fs.readdirSync(userDir).length;
    }
    return 0;
}

export function getPost(UUID: string, postId: string): any {
    const filePath = path.join(__dirname, 'posts', `${UUID}`, `${postId}.json`);
    if (fs.existsSync(filePath)) {
        return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    }
    return null;
}

export function savePost(UUID: string, post: any): boolean {
    const filePath = path.join(__dirname, 'posts', `${UUID}`, `${post.id}.json`);
    try {
        fs.writeFileSync(filePath, JSON.stringify(post, null, 0));
        return true;
    } catch (error) {
        console.error('Error saving post:', error);
        return false;
    }
} 

export function getAllPosts(UUID: string) {
    let posts = []
    for (let i = 0; i < userPostCount(UUID); i++) {
        const post = getPost(UUID, i.toString());
        if (post) {
            posts.push(post);
        }
    }
    return posts;
}