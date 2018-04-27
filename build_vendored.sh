#!/bin/bash

mkdir vendored
cd "./venv/lib/python3.6/site-packages/"
zip -r9q magpie.zip .
cp --parents magpie.zip ../../../../vendored/
rm -rf magpie.zip