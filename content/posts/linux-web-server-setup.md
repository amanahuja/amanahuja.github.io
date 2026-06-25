---
title: "Linux web server setup"
date: 2011-03-03
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - code
  - coding
  - install
  - linode
  - linux
  - ubuntu
  - wordpress
categories:
  - experiments
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2011/03/03/linux-web-server-setup/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: March 3, 2011.*

---

*Another* server. I timed myself this time around, just for the hell of it.

I created an account with [Linode](http://www.linode.com) and deployed Ubuntu 10.10. I then SSH'd to the brand new server using Putty.
 `login as: root
root@13.25.20.14's password:
Linux bananaserve 2.6.32.16-linode28 #1 SMP Sun Jul 25 21:32:42 UTC 2010 i686 GNU/Linux
Ubuntu 10.10
Welcome to Ubuntu!
* Documentation: https://help.ubuntu.com/`

A fresh server gives me a great feeling.

I added the (eventual) FQDN to /etc/hosts. The DNS changes will come later, but I want to do this before installing Apache. Then:
 `# echo "bananaserve" > /etc/hostname
# apt-get update
# apt-get upgrade
# apt-get install apache2 apache2-doc apache2-utils
# apt-get install libapache2-mod-php5 php5 php-pear php5-xcache
# apt-get install python-mysqldb`

Now Apache web server has been installed. Since I'm more familiar with Apache on CentOS than on Ubuntu, I poked around the configuration files, which are in /etc/apache2/. Similiarly, the virtual host config files are not in /etc/httpd/conf.d, they're in /etc/apache2/sites-enabled. **[Update: actually, in sites-available. See Liam's comment below.]**

I pointed the Virtual host configuration to a new directory that'll serve as webroot in /var/www/bananaserve. Then I started Apache.
`# /etc/init.d/apache2 restart
* Restarting web server apache2 Action 'start' failed.
The Apache error log may have more information.
[fail]`

Whoops. But as I started to go to see what was wrong, I realized I had not created the parent directory for the log files themselves, which Apache requires.
`# mkdir /etc/apache2/logs/
# /etc/init.d/apache2 restart
* Restarting web server apache2 ... waiting
[ OK ]`

Success. I opened up the IP address and saw Apache's default placeholder page ("The web server software is running but no content has been added, yet.").

I happened to be at webroot, so I fetched the Word Press files I'll need soon.
 `# cd /var/www/bananaserve/
# wget http://wordpress.org/latest.tar.gz
# tar xvfz latest.tar.gz
# mv wordpress/* .
# rm -rf wordpress/`

Of course, Wordpress won't work with a database. So I need MySql first.
 `# apt-get install mysql-server
# mysql_secure_installation`

And a database for wordpress:
 `# mysql -u root -p
Enter password:
Welcome to the MySQL monitor. Commands end with ; or \g.
Your MySQL connection id is 45
Server version: 5.1.49-1ubuntu8.1 (Ubuntu)
mysql> create database wp_bananaserve;
Query OK, 1 row affected (0.00 sec)
mysql> grant all on wp_bananaserve.* to 'bananaserve' identified by '5g#7$!9';
Query OK, 0 rows affected (0.00 sec)
mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)
mysql> quit
Bye
# /etc/init.d/apache2 restart
* Restarting web server apache2 ... waiting [ OK ]`

I then jumped over to the IP address and saw followed the on-screen directions for the Word Press 5-minute install.

All set? Well, almost. I need to create a user for the developer that'll be uploading the Word Press site tonight to the server. I don't want to give him root access.
 `# adduser xyzuser --no-create-home [various prompts]
# chown -R xyzuser:xyzuser /var/www/bananaserve/`

I then Emailed him his instructions to access webroot via FTP. All done!

**Total time: 1 hour 5 minutes.** Longer than I expected; I think I wasted some time poking around Apache configuration files. I also tested FTP access using Filezilla and uploaded a Word Press plugin (wordpress-importer) to make sure everything was working smoothly. I created a Word Press administrator user for the developer as well, and spent some extra time wordsmithing the Email to him with instructions and the credentials he'll need.

It's nice to work with offshore teams. By the time I get to work tomorrow, the site he's made will be up and running, ready for me to look at.
