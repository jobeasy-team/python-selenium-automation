#!/usr/bin/env bash

# Set the BASE_DIR variable to the current working directory
# (this is how you set variables in shell)
BASE_DIR=$(pwd)
# Create allure-test-results folder for allure files
mkdir -p $BASE_DIR/allure-test-results

# Install all dependencies from requirements.txt
pip3 install --no-cache-dir -r requirements.txt

# Run the tests:
behave -f allure_behave.formatter:AllureFormatter -o results/ features/tests/bestsellers.feature

# This line sets the EXIT_CODE variable to the exit status of the previous command.
EXIT_CODE=$?

# Generate allure report:
allure generate -c ./results/ -o $BASE_DIR/allure-test-results
sleep 10 # wait for report to generate

# Compress allure report to allure-results.tgz file
cd $BASE_DIR/allure-test-results && tar czvf $BASE_DIR/allure-test-results/allure-results.tgz *

# Send allure-results.tgz to the cloud
# This is OPTIONAL! You'll need to set up your cloud storage first,
# for example via google: https://stackoverflow.com/a/75541409/7746992
#curl -X POST -T $BASE_DIR/allure-test-results/allure-results.tgz \
#    -H "Authorization: Bearer YOUR_TOKEN" \
#    -H "Content-Type: application/json" \
#    "https://storage.googleapis.com/upload/storage/v1/b/lana-storage/o?uploadType=media&name=allure-results.tgz"

# Exit the script with the exit status of the previous command
exit $EXIT_CODE
