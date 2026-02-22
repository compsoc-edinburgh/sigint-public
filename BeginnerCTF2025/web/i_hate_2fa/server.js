const express = require('express');
const session = require('express-session');
const crypto = require("crypto");
const { visitStatus, ADMIN_PASSWORD } = require('./bot');
const app = express();
const SECRET_KEY = crypto.randomBytes(32).toString('hex');
const CSRF_SECRET = crypto.randomBytes(32).toString('hex');

app.set('view engine', 'ejs');

app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use(session({
    secret: 'a key',
    resave: false,
    saveUninitialized: false,
    cookie: {
        httpOnly: true,
        sameSite: "strict",
        secure: false,
    }
}));

const users = [
    {
        username: 'admin',
        password: ADMIN_PASSWORD, 
        email: 'admin@example.com',
        resetToken: null
    },
    {
        username: 'attacker',
        password: 'attacker',
        email: 'attacker@example.com',
        resetToken: null
    }
];

const statuses = {}; // username -> { content, createdAt }

const generateCSRFToken = () => {
    return crypto.randomBytes(32).toString('hex');
};

const validateCSRFToken = (token, sessionToken) => {
    return token && sessionToken && token === sessionToken;
};

const redirectLogin = (req, res, next) => {
    if (!req.session.userId) {
        res.redirect('/login');
    } else {
        next();
    }
};

app.get('/', (req, res) => {
    if (req.session.userId) {
        return res.redirect('/dashboard');
    }
    res.redirect('/login');
});

app.get('/login', (req, res) => {
    res.render("login");
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;
    console.log("Login attempt:", username);
    const user = users.find(u => u.username === username && u.password === password);

    if (user) {
        req.session.userId = user.username;
        return res.redirect('/');
    }
    res.redirect('/login');
});

app.get('/dashboard', redirectLogin, (req, res) => {
    if (req.session.userId === 'admin') {
        const adminView = {
            isAdmin: true,
            username: 'admin',
            flag: process.env.FLAG,
        };
        return res.render("dashboard", adminView);
    }
    
    const csrfToken = generateCSRFToken();
    req.session.csrfToken = csrfToken;
    res.render("dashboard", { 
        user: req.session.userId,
        isAdmin: false,
        statuses,
        csrfToken
    });
});

app.get('/logout', (req, res) => {
    req.session.destroy(err => {
        res.clearCookie('connect.sid');
        res.redirect('/');
    });
});

app.post('/status', redirectLogin, (req, res) => {
    const { content, _csrf } = req.body;

    if (!validateCSRFToken(_csrf, req.session.csrfToken)) {
        return res.status(403).send("Invalid CSRF token");
    }

    if (!content) {
        return res.status(400).send("Status content required");
    }

    statuses[req.session.userId] = {
        content,
        createdAt: new Date().toISOString()
    };

    console.log(`Status updated by ${req.session.userId}`);
    
    req.session.csrfToken = generateCSRFToken();
    res.redirect('/dashboard');
});

app.post('/report-status', redirectLogin, (req, res) => {
    const { username } = req.body;

    if (!statuses[username]) {
        return res.status(404).send("Status not found");
    }

    const targetUrl = `http://localhost:3000/view-status/${username}`;

    
    console.log(`Status from ${username} reported by ${req.session.userId}`);
    
    visitStatus(targetUrl);
    
    res.redirect('/dashboard');
});

app.get('/view-status/:username', (req, res) => {
    const username = req.params.username;
    const status = statuses[username];
    
    if (!status) {
        return res.status(404).send("Status not found");
    }

    const csrfToken = generateCSRFToken();
    if (req.session) {
        req.session.csrfToken = csrfToken;
    }

    res.render("view-status", { username, status, csrfToken, userId: req.session?.userId });
});

app.post('/request-password-reset', (req, res) => {
    const { email, username } = req.body;

    if (!username || !email) {
        return res.status(400).send("Username and email required");
    }

    const user = users.find(u => u.username === username);

    if (!user || user.email !== email) {
        return res.status(403).send("Invalid username or email");
    }

    const time = Math.floor(Date.now() / 100).toString();
    const seed = SECRET_KEY + time;
    console.log(`Seed: ${seed}`);

    const token = crypto.createHash('sha256').update(seed).digest('hex');
    user.resetToken = token.toString();

    console.log(`Reset Link: http://localhost:3000/reset-password?token=${token}&username=${username}`);
    res.send(`Reset link generated! <a href="/reset-password?token=${token}&username=${username}">Reset Password</a>`);
});

app.get('/reset-password', (req, res) => {
    const { token, username } = req.query;
    const user = users.find(u => u.resetToken === token && u.username === username);

    if (!user) {
        return res.status(403).send("Invalid or expired token.");
    }

    res.render("reset", { token, username: user.username });
});

app.post('/reset-password', (req, res) => {
    const { token, newPassword, username } = req.body;
    const user = users.find(u => u.resetToken === token && u.username === username);

    if (user) {
        user.password = newPassword;
        user.resetToken = null;
        console.log(`Password reset for ${user.username}`);
        return res.redirect('/');
    }
    res.status(403).send("Error updating password.");
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
})
