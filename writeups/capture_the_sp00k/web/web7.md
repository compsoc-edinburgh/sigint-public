# Web 7 Challenge

## Topics Covered

Robots.txt files

## Tools

* None

## Method

The challenge text and website content "BEEP BOOP" should be a hint about robots. This should remind you to check the robots.txt file which are commonly found on web servers to kindly ask indexing engines not to look at files or directories. 

This file was located at "http://ctf.sigint.mx/robots.txt". Inside is the contents 

```
User-agent: *
Disallow: /adminlogin/
```

Looking inside the /adminlogin/ directory grants you the flag "sigint>c0m3_0v3r_n_l1st3n_t0_my_m1x_tap3".
