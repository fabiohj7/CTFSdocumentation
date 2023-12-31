# Documentation for OSINT challenge NCL 23

## OSINT Challenge.

### Meta (easy)

Challenge is to get an image's meta data.

<img src="Meta.jpg" alt="image" width="300" height="250"/>

6 questions given to about information of the metadata of the picture.

---

The way I solved this was using:

`exiftool Meta.jpg`

This is a tool I downloaded to my mac using

`brew install exiftool`

The tool outputs complete information about the image.
The answers of the question were all in the output.

## Lookup (easy)

Answer the questions about DNS

3 questions were given.

---

To solve this question one must google the question.
All the answers were reachable through a simple google search.

**What type of DNS record holds the DNSSEC public signing key?**

DNSSEC is described in RFC 4034.
The information related to the record can be found in Section 2.

**What type of DNS record is used to map hostnames to IPv6 addresses?**
The DNS Extension to Support IPv6 is described in RFC 3596.
The information related to the record can be found in section 2.

**What type of DNS record is used to delegate a DNS zone?**
The DNS record to delegate a DNS zone is described in RFC 1035.
Answer this challenge requires reading the specification to understand what it means to delegate a DNS zone in order to identify that the DNS record type that is needed to delegate a DNS zone is the one that indicates an authoritative name server.

## Threat intel (easy)

Challenge is to reasearch common security vulnerabilities.

6 questions were given

---

To solve this quesiton one simple google search was needed to get the answer.

**What is the CVE of the original POODLE attack?**
CVE-2014-3566.

**What version of VSFTPD contained the smiley face backdoor?**
The answer to this question can be found on Wikipedia.

**What was the first 1.0.1 version of OpenSSL that was NOT vulnerable to heartbleed?**
The answer to this question can be found on Wikipedia.

**What was the original RFC number that described Telnet?**
The answer to this question can be found on Wikipedia.

**How large (in bytes) was the SQL Slammer worm?**
The answer to this question can be found on Wikipedia.

**Samy is my…**
The answer to this question can be found on Wikipedia.

## HTTP Headers (easy)

Solve 3 question about HTTP headers

---

One more time our this problem can be solved with simple google searches.

## SSL (Medium)

Solve 3 questions about CyberSkyline SSL certificate

---

To find most of these answers you need to go to the lock next to the URL
search bar. Then you click on the lock logo >> connection is secure >>
certificate is valid.

From there you can get all the asnwers.

## Barcode (Medium)

Given a barcode, find the flag in it.

<img src="Barcode.gif" alt="Barcode"/>

---

Once the image was downloaded, I looked for a barcode scanner tool on google.
I uploaded the image and scanned it.

The tool used is the following:
https://cmbdn.cognex.com/free-barcode-scanner

The barcode format was a _Code 39_ format.

I was able to get the flag by scanning the barcode and getting the output.
