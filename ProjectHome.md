## A multiplatform PyQt-based news agregator ##

**NEW:** 0.2.13 is out!

[![](http://farm4.static.flickr.com/3312/3276879022_2e9d81d0c0.jpg)](http://www.flickr.com/photos/ralsina/3276879022/)

This version is working very nicely for me. However:

  * It's completely untested on operating systems beyond Linux

  * Database upgrades are disabled, so there is a chance it won't work with your existing database. This is beyond my control right now. Read everything, make a backup of ~/.urssus and cross your fingers.

  * Qt 4.5 is when the embedded browser is going to be nice (when flash works!)

### IMPORTANT ###

You need PyQt 4.4.0 or later, because uRSSus requires WebKit.

**Help wanted on non-linux platforms!**

### Features ###

  * Google reader subscription import

  * Twitter support

  * Multiple views (normal/widescreen/river-of-news(combined))

  * Google News support (type a subject, get a permanent news feed about it)