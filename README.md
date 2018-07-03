# tuesday



### Database configurations
    sudo su - postgres

    psql-> CREATE DATABASE mili;
    psql-> CREATE USER mili_user WITH PASSWORD 'root';
    psql-> GRANT ALL PRIVILEGES ON DATABASE mili TO mili_user;


### Install requirements
    cd /var/www/tuesday
    pip install -r requirements.txt