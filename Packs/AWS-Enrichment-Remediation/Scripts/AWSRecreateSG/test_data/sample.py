SG_INFO = [
    {
        "Type": 1,
        "Contents": [
            {
                "Description": "sldkjdlskfjs",
                "GroupId": "sg-00000000000000001",
                "GroupName": "demo-sg",
                "IpPermissions": [
                    {
                        "FromPort": 0,
                        "IpProtocol": "tcp",
                        "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                        "Ipv6Ranges": [],
                        "PrefixListIds": [],
                        "ToPort": 65535,
                        "UserIdGroupPairs": [],
                    },
                    {
                        "FromPort": 22,
                        "IpProtocol": "tcp",
                        "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                        "Ipv6Ranges": [],
                        "PrefixListIds": [],
                        "ToPort": 22,
                        "UserIdGroupPairs": [],
                    },
                ],
                "IpPermissionsEgress": [
                    {
                        "FromPort": 0,
                        "IpProtocol": "tcp",
                        "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                        "Ipv6Ranges": [],
                        "PrefixListIds": [],
                        "ToPort": 65535,
                        "UserIdGroupPairs": [],
                    }
                ],
                "OwnerId": "717007404259",
                "Region": "us-east-1",
                "VpcId": "vpc-061c242911e464170",
            }
        ],
        "HumanReadable": "### AWS EC2 SecurityGroups\n|Description|GroupId|GroupName|OwnerId|Region|VpcId|\n|---|---|---|---|---|---|\n| sldkjdlskfjs | sg-0408c2745d3d13b15 | demo-sg | 717007404259 | us-east-1 | vpc-061c242911e464170 |\n",
        "ImportantEntryContext": "None",
    }
]
INSTANCE_INFO = [
    {
        "Metadata": {"instance": "AWS - EC2"},
        "Type": 1,
        "Contents": [
            {
                "NetworkInterfaces": [
                    {
                        "Association": {"PublicIp": "1.1.1.1"},
                        "Groups": [{"GroupId": "sg-00000000000000000", "GroupName": "sg-name"}],
                        "NetworkInterfaceId": "eni-00000000000000000",
                    }
                ]
            }
        ],
    }
]
NEW_SG = [{"Type": 1, "Contents": {"GroupId": "sg-00000000000000001"}}]
