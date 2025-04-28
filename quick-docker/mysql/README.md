# Docker Compose Setup

## The Docker Compose file will

* Run a MySQL container with a specified root password.
* Map port 3306 on the host to 3306 in the container.
* Include a custom MySQL configuration to allow external connections.
* Run an initialization script to grant root@% privileges.

## Supporting Files

You’ll need two additional files in the same directory as docker-compose.yml:

1. MySQL Configuration File (my.cnf): This ensures MySQL binds to 0.0.0.0 to allow external connections.
2. Initialization Script (mysql-init.sql): This grants root@% privileges to allow connections from any host.
