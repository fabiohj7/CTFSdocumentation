# Password Craking

## Cracking 1 (Easy)

After obtaining a few plaintext passwords, it appears that they overlap
with the passwords from the rockyou breach.

5 hashes are given:

- 8a96446a5afb4ab69a2d15091771e39
- ec5f0b1826389df8622133014e88afde
- 32e5f63b189b78dccf0b97ac41f0d228
- 2233287f476ba63323e60addca1f6b64
- 6539bbb84fe2de2628fc5e4f2a31f23a

---

For this challenge I was a little lost, I never done password cracking so
it's time to research.

I found out that there are two very popular tools "Jack The Ripper" and
"Hashcat", this 2 tools are password cracking tools.

Turning on my kali machine to use the rockyou wordlist I started playing
with hashcat first.

But first, I figured out the type of hash I was dealing with.

`hash-identifier [hash]`

Gave me the answer.
We are dealing with a MD5 hash. So I used hashcar tools to start figuring out
the passwords.

Reading some documentation I saw that to use hashcat with a word list you type
the following:

`hashcat -m 0 -a 0 md5.txt /usr/share/wordlists/rockyou.txt`

This gave me the flag!

`-m` is a flag the type of hash
`0` is the code for MD5.
`-a` is a flag for attack.
`0` is the type of attack, in this case a dictionary attack

We use `-a 1` for a combinator attack.
This means that it will try different combinations of words from our wordlist.

Or `-a 3` for a Mask Attack.
This is a similar attack to the dictionary attack, but is more specific.
Brute-force approaches, this might take a long time, but if we have info
on the password this could be really useful.

## Cracking 2 (Medium)

After obtaining a few plaintext passowrds, it appears that they are all in the
same format. "SKY-HQNT-" followed by 4 digits. Can you crack them?

5 Hashes were given:

- 71b816fe0b7b763d889ecc227eab400a
- 674291170dffcf620bda2a604a6820ea
- 06f03267f31077d2c4b5c728472070ae
- d866f4b3b34b598375149fb7661113ab
- d9053951a8d1c15254b46ec9fc974a6b

---

For this challenge it took a lot longer to figure out how to get the passwords.
To start, I tried the approach from last time, using hashcat. It didn't work,
so I decided to learn about John The Ripper, after trying to use it too, it didn't
work.

The first part of the password was given, so that is some information of the password,
we just need to know what the last 4 numbers are.

The brute-force idea sounds pretty good now, so we go back to hashcat.
To use it in this specific attack we use the following syntax:

`hashcat -m 0 -a 3 crack.txt 'SKY-HQNT-?d?d?d?d`

`?d` will run different combinations of numbers until it gets the hash.

## Cracking 3 (Medium)

After obtaining a few plaintext passwords, it appears that they are based on Pokemon.

- a532443f3e04a9e00295a8cd2a75e080
- 54c10b9736b70e75c6e505f340b6e2f1
- b8a24794813a47521b4be55747e0665a
- 83b020b0a7b3c353e1c11b1647b53cda
- 999cae1e22fe69d89d6f56e3050f18cb

---

All these hashes are MD5. From here it was easy to figure out what to do next, I went
and downloaded a Pokemon wordlist from the internet, used hashcat

`hashcat -m 0 -a 0 [txt file] [pokemon wordlist]`

The flag was obtained.

## Cracking 4 (Medium)

Our analysts have obtained windows password dumps storing hacker passwords. Can you crack them?

- 21259DD63B980471AAD3B435B51404EE:1E43E37B818AB5EDB066EB58CCDC1823
- 11CB3F697332AE4C4A3B108F3FA6CB6D:13B29964CC2480B4EF454C59562E675C
- 65711C079DC4CD3CC2265B23734E0DAC:47F747C5190DC0F0B921AA4A07F06285
- FBBDA33FC12E83FB0C240E84A183686E:DDE9DC6E34E2E6E11EF9E51C6B27ED96
- 21C4E7C2EFE8E8D1C00B70065ED76AA7:A7A0F9AFD4A78F531A1CF4C42E531BBF
- E85B4B634711A266AAD3B435B51404EE:FD134459FE4D3A6DB4034C4E52403F16
- BA756FB317B622DBAAD3B435B51404EE:C8405270B10B13AE8A24612BB853567A
- 199C926FA387EAB7AAD3B435B51404EE:F196F77BF8BB15781BA8364C649C5FD4
- FE4AACAAAD7D986AAAD3B435B51404EE:3928E16F614E2316CA51C336FA5B3011
- 3613F7EC15407F56AAD3B435B51404EE:C82E164316183AA3AF3EA6BAA642A237

---

This challenge took a little more time, trying to figure out what type of hash these are, by using
hash-identifier it give me a wrong type, but after researching I found out that the windows password
types are NTLM, so I used an online tool that would unhash all these passwords

[Hash decrypter](hashes.com/en/decrypt/hash)

This website gave me all the flags I needed.

## Cracking 5 (Medium)

It appears that the passwords are based off of Law and Order: SVU episoded and end in 2 digits.

- 21259DD63B980471AAD3B435B51404EE:1E43E37B818AB5EDB066EB58CCDC1823
- 11CB3F697332AE4C4A3B108F3FA6CB6D:13B29964CC2480B4EF454C59562E675C
- 65711C079DC4CD3CC2265B23734E0DAC:47F747C5190DC0F0B921AA4A07F06285
- FBBDA33FC12E83FB0C240E84A183686E:DDE9DC6E34E2E6E11EF9E51C6B27ED96
- 21C4E7C2EFE8E8D1C00B70065ED76AA7:A7A0F9AFD4A78F531A1CF4C42E531BBF
- E85B4B634711A266AAD3B435B51404EE:FD134459FE4D3A6DB4034C4E52403F16
- BA756FB317B622DBAAD3B435B51404EE:C8405270B10B13AE8A24612BB853567A
- 199C926FA387EAB7AAD3B435B51404EE:F196F77BF8BB15781BA8364C649C5FD4
- FE4AACAAAD7D986AAAD3B435B51404EE:3928E16F614E2316CA51C336FA5B3011
- 3613F7EC15407F56AAD3B435B51404EE:C82E164316183AA3AF3EA6BAA642A237

---

After all the research I've done for this challenge I was able to gather some information on what
tools to use, and how to use them.

For this flag I used hashcat again. After downloading a wordlist from the internet I entered the
following command:

`hashcat -m 0 -a 6 [text file] [wordlist] ?d?d`

`-a 6` is a hybrid attack that lets you use a dictionary and a mask attack at the same time.
?d?d lets you brute force numbers at the end of the word list that it looks for.
