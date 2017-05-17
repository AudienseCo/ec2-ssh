=======
ec2-ssh
=======

A pair of command line utilities for finding and SSH-ing into your Amazon EC2
instances by tag (such as 'Name').

Forked from YPlan https://github.com/YPlan/ec2-ssh/

Installation
------------

From pip:

.. code-block:: bash

    pip install ec2-ssh

Usage
-----

.. code-block:: bash

    # ec2-ssh

    % ec2-ssh nginx2
    # equivalent to
    # ssh ubuntu@ec2-123-45-67-89.compute-1.amazonaws.com

    % ec2-ssh root@appserver
    % ec2-ssh deploy@nginx2 sudo restart nginx

    # Specifying the user with an environment variable
    % EC2_SSH_USER=deploy ec2-ssh nginx2

    # ec2-host

    # w/o arg: prints all active instances
    % ec2-host
    ec2-123-45-67-89.compute-1.amazonaws.com
    ec2-132-45-67-89.compute-1.amazonaws.com
    ec2-231-45-67-89.compute-1.amazonaws.com

    # w/ arg
    % ec2-host backend
    ec2-132-45-67-89.compute-1.amazonaws.com
    ec2-132-45-67-90.compute-1.amazonaws.com

    # w/ tag arg too
    % ec2-host -t environment production
    ec2-132-45-67-90.compute-1.amazonaws.com
    ec2-111-45-67-90.compute-1.amazonaws.com


To use internal ips instead of public dns put this env vars in your shell
profile.

.. code-block:: bash

   export EC2_SSH_USER=$USER
   export EC2_HOST_TAG='Name'
   export EC2_SSH_INTERNAL_IP=True
