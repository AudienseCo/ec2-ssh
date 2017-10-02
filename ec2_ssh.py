from __future__ import print_function

import argparse
import os
import random
import sys

import boto3

parser = argparse.ArgumentParser(
    description="""
    SSH into an ec2 host where <tag-value> matches a tag which defaults to
    'Name' or environment variable EC2_HOST_TAG. In the case there is more than
    one such instance, one will be chosen at random. 'username' defaults to
    ubuntu.  A small bashrc file is added over ssh to give a nice prompt. Any
    extra arguments at the end are passed to ssh directly.
    """
)
parser.add_argument('-t', '--tag', type=str,
                    default=os.getenv('EC2_HOST_TAG', 'Name'),
                    help="Tag to match, defaults to 'Name'")
parser.add_argument('-u', '--user', type=str,
                    default=os.getenv('EC2_SSH_USER', 'ubuntu'),
                    help="Which user to connect with, defaults to 'ubuntu'")
parser.add_argument('-i', '--internal', action='store_true',
                    default=os.getenv('EC2_SSH_INTERNAL_IP', False),
                    help="Select the internal IP instead of the public one")
parser.add_argument('value', help="The value for the tag to match")



def main():
    args, unparsed = parser.parse_known_args()

    if '@' in args.value:
        username, value = args.value.split('@', 1)
    else:
        username = args.user
        value = args.value

    host_name = get_host_name(args.tag, value, args.internal)

    if not host_name:
        print("ec2-ssh: no hosts matched", file=sys.stderr)
        sys.exit(1)

    command = [
        'ssh',
        '-t', '-t',
        username + '@' + host_name,
    ]
    if unparsed:
        command.extend(unparsed)

    print("ec2-ssh connecting to {}".format(host_name), file=sys.stderr)
    sys.stdout.flush()
    os.execlp(*command)


def get_dns_tag(is_internal):
    return 'PrivateIpAddress' if is_internal else 'PublicAddressName'


def get_host_name(tag, value, dns_type):

    for host in get_dns_names(tag, value, get_dns_tag(dns_type)):
        return host


def ec2_host_parser():
    parser = argparse.ArgumentParser(
        description="Output ec2 public host names for active hosts in random "
                    "order, optionally match a tag which defaults to 'Name' "
                    "or environment variable EC2_HOST_TAG."
    )
    parser.add_argument('value', type=str, nargs='?',
                        help='the value the tag should equal')
    parser.add_argument('-t', '--tag', type=str,
                        default=os.getenv('EC2_HOST_TAG', 'Name'),
                        help='which tag to search')
    parser.add_argument('-i', '--internal', action='store_true',
                        default=os.getenv('EC2_SSH_INTERNAL_IP', False),
                        help="Select the internal DNS instead of the public "
                             "one")
    return parser


def host():
    args = ec2_host_parser().parse_args()
    instances = get_dns_names(args.tag, args.value, get_dns_tag(args.internal))
    random.shuffle(instances)
    for instance in instances:
        print(instance)


def get_dns_names(tag, value, dns_type):
    conn = boto3.client('ec2')

    filters = [{
        'Name': 'instance-state-name',
        'Values': ['running']
    }]
    if value:
        filters.append({
            'Name': 'tag:' + tag,
            'Values': [value]
        })

    data = conn.describe_instances(Filters=filters)

    dns_names = []
    for reservation in data['Reservations']:
        for instance in reservation['Instances']:
            if instance[dns_type]:
                dns_names.append(instance[dns_type])
    return dns_names


if __name__ == '__main__':
    main()
