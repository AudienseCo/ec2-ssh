ec2-ssh
=======

Socialbro's port of ec2-ssh with some improvements

The original code could be found here https://github.com/Instagram/ec2-ssh

It now supports:
 - Connection trough internal ip addresses (usefull when you have a VPN and want to connect trough the internal IPs)
 - Automatically checks multipple zones (if can't find any host on us-east-1, it will automatically check eu-west-1)
