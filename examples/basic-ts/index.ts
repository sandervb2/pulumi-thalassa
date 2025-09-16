import * as thalassa from "@sandervb2/pulumi-thalassa";

const vpc = new thalassa.Vpc("vpc", {
    region: "nl-01",
    description: "Pulumi VPC",
    cidrs: ["10.5.0.0/16"],
});

export const sampleAttribute = vpc.id;
