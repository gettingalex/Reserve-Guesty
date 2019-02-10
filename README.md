# Availability and Reservation Tool based on Guesty

## About

This tool extracts the listing from Guesty and displays them in a dropdown menu with a datepicker, in order for the user to check the availability. If the unit is available for all the selected period, the users can then make a payment via Stripe. However, if the unit is not available for the entire selected period, a flash message will be returned under the availability form.

*Please note that the code to automatically post the new reservation to Guesty is not included.\

## Features

* Check dates availability of listing on Guesty
* Calculate price of stay for the selected listing based on Guesty pricing
* Stripe payment integration for available bookings

## Running the Availability and Reservation Tool

1. Install [Vagrant](https://www.vagrantup.com) and [VirtualBox](https://www.virtualbox.org)
2. Download/Clone the repository with the Vagrant VM file [Reserve-francais](https://github.com/gettingalex/Reserve-francais)
3. Launch Vagrant in the terminal with command 
```
vagrant up
```

4. Run the virtual machine with 
```
vagrant ssh
```

5. Then navigate to the shared directory
```
cd /vagrant

6. Run the application:
```
python project.py\
```

7. In the browser, open [http://localhost:5000/](http://localhost:5000/) and use the interface to navigate the web app


## Tech/Framework used:

* [Python](https://www.python.org)
* HTML
* [Bootstap](https://getbootstrap.com)
* [Flask](http://flask.pocoo.org)
* [JSON](http://www.json.org)
* [Stripe API](https://stripe.com/docs/api)
* [Guesty API](https://guestyorg.github.io/guesty-api/)
* [VirtualBox](https://www.virtualbox.org)
* [Vagrant](https://www.vagrantup.com)
