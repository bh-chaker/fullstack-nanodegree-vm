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

* Create a Google App, you can follow this video from [Authentication & Authorization: OAuth](https://www.youtube.com/watch?v=8aGoty0VXgw), a [Udacity](https://www.udacity.com/) course. After this step you should have a valid client_secrets.json file in the catalog directory (next to project.py file)

 **IMPORTANT: When adding the Authorized JavaScript Origin, make sure to use the correct port from [here](https://github.com/bh-chaker/fullstack-nanodegree-vm/blob/master/vagrant/catalog/project.py#L177). Feel free to change the port if the current port is already used in your system.**

* You should have a valid client_secret.json in y

* Setup and populate the databasee:

 python database_setup.py
 
 python database_populate.py
 
* Start the server:

 python project.py
 
* Access the app on http://localhost:8000

 The port used can be found [here](https://github.com/bh-chaker/fullstack-nanodegree-vm/blob/master/vagrant/catalog/project.py#L177).
