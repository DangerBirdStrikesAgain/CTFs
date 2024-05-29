# HINTS AND TRICKS FOR KALI LINUX

_Last updated: 29/05/2024_

This page is a collection of tricks and some helpful "how to" bits for Linux, specifically Kali Linux. It follows from my previous page about Kali Linux (TODO: LINK HERE).



## So you want to install a program? 
I use the Tor Browser as an example here! We will walk through which ditribution to download, how to check the signature, \

Looking for the linux distribution \
File type 


## Checking the signature of a program
Checking the signature of a file is _important_. This ensures that the file you have downloaded has not changed since it was 'signed' by the creator. However, it will not prevent initially malicious code from being downloaded. 

We will use GnuPG (GNU Privacy Guard) to verify the signaure. You can verify that it is installed by typing the following into your terminal: 

```console
$ gpg --version
```

This should have an output starting similar to this 

```console
gpg (GnuPG) 2.2.40
libgcrypt 1.10.3
Copyright (C) 2022 g10 Code GmbH
```

## Signing a file you have
Wow this is scope creep 