## ec2-ssh

Socialbro's port of ec2-ssh with some improvements

The original code could be found here https://github.com/Instagram/ec2-ssh

It now supports:
 - Connection trough internal ip addresses (usefull when you have a VPN and want to connect trough the internal IPs)
 - Automatically checks multipple zones (if can't find any host on us-east-1, it will automatically check eu-west-1)

### Installation

```
git clone https://github.com/Instagram/ec2-ssh.git
sudo python setup.py install
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
