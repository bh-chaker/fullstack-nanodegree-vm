Full Stack Nanodegree VM
=============

#Catalog App
##Overview
The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system.
In this example, the categories are the best European Football Leagues and the items are Football teams.
##Installation
* Clone or download the repository to your machine
* Navigate to vagrant folder:

 cd to fullstack-nanodegree-vm/vagrant
 
* Start the vagrant VM and login via ssh:

 vagrant up  `--> You need to be patient at this step. There is a lot to install when running pg_config.sh`
 
 vagrant ssh
 
* Withing the VM, navigate to /vagrant/catalog:

 cd /vagrant/catalog

* Setup and populate the databasee:

 python database_setup.py
 
 python database_populate.py
 
* Start the server:

 python project.py
 
* Access the app on http://localhost:8000
