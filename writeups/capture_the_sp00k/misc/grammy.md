# Grammy Loves her Forwards Challenge

## Topics Covered

* SMTP
* Base64 files

## Tools


* [Base 64 Decoder](https://www.base64decode.org/) 

## Method

This is an SMTP message transcript, the flag is an attachment to an email. In SMTP conversations the binary data is Base64 encoded, and that's the case here with a png image.

Using the tool above you can set the output to file, and download the image. Inside is the flag value:

"sigint>f0rwards_fr0m_gr4nny"
