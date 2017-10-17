# Catalog Project
This is a store catalog application where only logged in users can create products and added them to categories. Login authentication is provided by a Google sign-in button. Visitors to the application can view the catalog but cannot make any changes.

## Installation
This project requires a Postgresql database. Create a database in vagrant by entering the command for Postgresql

'''
psql
'''

Then in the Postgresql terminal create the 'storeproducts' database:

'''
CREATE DATABASE storeproducts;
'''

Quit the Postgresql command prompts with '\q'.

## Run the virtual machine!

Using the terminal, change directory to catalog (**cd catalog**), then type **vagrant up** to launch your virtual machine.

## Running the Catalog Project App
Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type **exit** at the shell prompt.  To turn the virtual machine off (without deleting anything), type **vagrant halt**. If you do this, you'll need to run **vagrant up** again before you can log into it.


Now that you have Vagrant up and running type **vagrant ssh** to log into your VM.  change to the /vagrant directory by typing **cd /vagrant**. This will take you to the shared folder between your virtual machine and host machine.


In vagrant, navigate to the catalog folder: /vagrant/catalog

Type **python database_setup.py** to initialize the database.

Type **python database_populate.py** to populate the database with categories and products.

Type **python application.py** to run the Flask web server. In your browser visit **http://localhost:8000** to view the catalog project app.  You should be able to view, add, edit, and delete products and categories.
