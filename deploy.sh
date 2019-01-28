#!/bin/bash
aws cloudformation deploy --template-file packaged-template.yaml --stack-name msa-stack-createItem --capabilities CAPABILITY_IAM