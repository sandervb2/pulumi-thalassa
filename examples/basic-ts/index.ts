import * as thalassa from "@pulumi/thalassa";

const vpc = new thalassa.Vpc("vpc", {
    region: "nl-01",
    description: "Pulumi VPC",
    cidrs: ["10.5.0.0/16"],
});

export const sampleAttribute = (vpc as any).id;
