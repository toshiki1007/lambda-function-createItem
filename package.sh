#!/bin/bash
aws cloudformation package --template-file template.yaml --s3-bucket msa-sam-repository --output-template-file packaged-template.yaml