# idonethis-spectator
Spectator mode for iDoneThis.

## depracated; incompatible with iDoneThis 2.0

This simple webapp will allow you to share what you've contributed to your iDoneThis team in the past day and past week with someone outside of your team.

## quick install instructions
check out the repository.

create a config.py at the root (untracked via .gitignore).
add the following values to it:

```
token = "<your api token goes here>"
team = "<your team short name goes here>"
user = "<your username goes here>"
```

### cautions and suggestions
it is recommended to create a virtualenv to run the app in, please read this documentation to learn more:
<http://docs.python-guide.org/en/latest/dev/virtualenvs/>

for production use it's important to do a proper web server setup and not just run the built in dev server; here's a great guide on digitalocean.com to get you started:
<https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps>

### finishing the install and testing
install the requirements (preferably in a virtualenv):
`pip install -r requirements.txt`

run the app to make sure everything is working properly:
`python spectator.py`

take it for a spin in your browser:
<http://127.0.0.1:5000>
