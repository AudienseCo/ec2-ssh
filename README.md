## ec2-ssh

Socialbro's port of ec2-ssh with some improvements

The original code can be found here https://github.com/Instagram/ec2-ssh

It now supports:
 - Connection trough internal ip addresses (usefull when you have a VPN and want to connect trough the internal IPs)
 - Automatically checks multipple zones (if it can't find any host on us-east-1, it will automatically check eu-west-1, then sa-east-1 and so on...)
 - If there's more than 1 host with the same name, it will open a cssh connection to all of them. Really usefull when using AutoScale.

### Installation

```
git clone https://github.com/SocialBro/ec2-ssh
sudo python setup.py install
sudo apt-get install cssh #(Required if you want to stablish multiple connections)

```

### Usage

```
$ ec2-ssh server01
Checking region us-east-1
Checking region eu-west-1
Connecting to ubuntu@ec2-XX-XX-XX-XX.eu-west-1.compute.amazonaws.com.
server01:~$ 
```

```
$ ec2-ssh -i server01
Checking region us-east-1
Connecting to ubuntu@10.XXX.XX.XX.
server01:~$ 
```

```
$ ec2-host
server01 ec2-5X-YYY-ZZZ-GG.compute-1.amazonaws.com 10.1.2.3
server02 ec2-5X-YYY-ZZZ-GH.compute-1.amazonaws.com 10.1.2.4
server03 ec2-5X-YYY-ZZZ-GI.compute-1.amazonaws.com 10.1.2.5
server04 ec2-5X-YYY-ZZZ-GJ.compute-1.amazonaws.com 10.1.2.6
```
