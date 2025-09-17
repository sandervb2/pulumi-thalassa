import pulumi
import pulumi_thalassa as thalassa

vpc = thalassa.Vpc("vpc",
    name="vpc-vpc",
    region="nl-01",
    cidrs=[
        "10.0.0.0/16",
        "10.2.0.0/16",
        "10.3.0.0/16",
    ],
    labels={
        "environment": "production",
        "project": "vpc-project",
        "owner": "team-a",
    })
# Create a subnet within the VPC
vpc_subnet = thalassa.Subnet("subnet",
    name="vpc-subnet",
    description="vpc subnet for documentation",
    vpc_id=vpc.id,
    cidr="10.0.1.0/24")
pulumi.export("vpcId", vpc.id)
pulumi.export("subnetId", vpc_subnet.id)

