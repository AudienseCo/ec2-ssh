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
sudo apt-get install clusterssh #(Required if you want to stablish multiple connections)

```

### Usage

#### Connecting to an instance on eu-west-1 using it's external IP
```
$ ec2-ssh server01
Checking region us-east-1
Checking region eu-west-1
Connecting to ubuntu@ec2-XX-XX-XX-XX.eu-west-1.compute.amazonaws.com.
server01:~$ 
```

#### Connecting to an instance on us-east-1 on it's internal IP
```
$ ec2-ssh -i server01
Checking region us-east-1
Connecting to ubuntu@10.XXX.XX.XX.
server01:~$ 
```

#### List all instances on us-east-1 (ec2-host uses us-east-1 by default) 
```
$ ec2-host
server01 ec2-5X-YYY-ZZZ-GG.compute-1.amazonaws.com 10.1.2.3
server02 ec2-5X-YYY-ZZZ-GH.compute-1.amazonaws.com 10.1.2.4
server03 ec2-5X-YYY-ZZZ-GI.compute-1.amazonaws.com 10.1.2.5
server04 ec2-5X-YYY-ZZZ-GJ.compute-1.amazonaws.com 10.1.2.6
```
#### Connec to the private address of a group of instances that have the same tag name (i.e. Instances that belong to an Auto Scaling Group)
```
$ ec2-ssh -i my-as-group
Checking region us-east-1
There's more than 1 host with that name...
Opening to: ubuntu@10.XXX.YYY.ZZ1 ubuntu@10.XXX.YYY.ZZ2 ubuntu@10.XXX.YYY.ZZ3
```



#### Connec to the public address of a group of instances that have the same tag name (i.e. Instances that belong to an Auto Scaling Group)
```
$ ec2-ssh my-as-group
Checking region us-east-1
There's more than 1 host with that name...
Opening to: ubuntu@54.XXX.YYY.ZZ1.compute-1.amazonaws.com ubuntu@54.XXX.YYY.ZZ2.compute-1.amazonaws.com ubuntu@54.XXX.YYY.ZZ3.compute-1.amazonaws.com
```

#### Connect to a server that's inside a network without external access trough a gateway host.
```
$ec2-ssh -i -g gateway02.yourdomain.com my-as-group
Checking region us-east-1
There's more than 1 host with that name...
creating tmp config file
Opening to: ubuntu@10.0.0.175 ubuntu@10.0.1.129 ubuntu@10.0.1.213
```
That will create a connection to gateway02 and then a connection to each of the servers. Now you can leave port 22 open only for gateway hosts. It should also connect to VPC hosts



## That could save you some typing...
On your ~/.bashrc add the following alias (modify acording your setup)
```
alias c='ec2-ssh -i'
alias cg='ec2-ssh -i -g gateway01.yourdomain.com'
alias cs='ec2-ssh -i -g gateway02.yourdomain.com'
alias ci='ec2-ssh'
```
and now, the following command will create an SSH connection to ALL hosts with tag_name=my-as-group trough a gateway on gateway01.yourdomain.com
```
cg my-as-group
```
