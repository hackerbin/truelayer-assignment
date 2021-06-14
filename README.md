# True layer Auth and Bank/Card Data Fetch

## Setup instruction

1. Create virtualenv
2. Install all the requirements from requirements.txt -> `pip install -r requirements`
3. Copy config/.env.example to config/.env and update the variable with proper values. Contact developer if you need help
4. Create a folder name `"log"`
5. Run migration command -> `./manage.py migrate`
6. Run the project -> `./manage.py runserver`


## Server commands
1. gunicorn service is running as system daemon
2. `sudo systemctl restart/status/start/stop tla`
3. here `tla` is my service name. 
4. You can find the service file in `/etc/systemd/system/tla.service`

Have fun, Happy coding!