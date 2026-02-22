Race condition on vulnerable password reset token generation + CSRF <br />

.env's content should be: <br />
ADMIN_PASSWORD=... <br />
FLAG=... <br />

The token generation alg is based on a secret key + current timestamp. As a result, they can clash. If the attacker's hash clashes with the admin, the attacker can reset the admin's password