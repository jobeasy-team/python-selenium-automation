# Set the base image for this Dockerfile to the official selenium/standalone-chrome image,
# which contains a standalone Selenium server and Chrome browser.
FROM selenium/standalone-chrome

# Change the user to root (gives admin privileges)
USER root

# The WORKDIR instruction in a Dockerfile sets the working directory.
# This means that any file operations or commands that are executed in the container
# will be relative to the directory specified by the WORKDIR instruction.
# Any subsequent RUN, CMD, COPY, etc. instructions
# will be executed in the //usr/src/13-python-selenium-automation directory.
WORKDIR /usr/src/13-python-selenium-automation

# Install python3-pip package
RUN apt-get -y update
RUN apt-get -y install -y software-properties-common
RUN apt-get -y install python3-pip

# Download Allure commandline from GitHub and install it
RUN curl -o allure-2.14.0.tgz -Ls https://github.com/allure-framework/allure2/releases/download/2.14.0/allure-2.14.0.tgz
RUN tar -zxvf allure-2.14.0.tgz -C /opt/
RUN ln -s /opt/allure-2.14.0/bin/allure /usr/bin/allure
# Verify Allure installed
RUN allure --version

# Copy all the files from the current directory (the directory containing the Dockerfile)
# to the working directory inside the container.
COPY . .

# chmod +x command makes the run_selenium_tests.sh file executable
# (it changes the permission of a file)
RUN chmod +x ./run_selenium_tests.sh

# CMD command specifies the command to run when a container is started,
# which in this case is ./run_selenium_tests.sh.
CMD ["./run_selenium_tests.sh"]
