# sample code

* sample code of talk "Automate the Boring Stuff with Slackbot (ver. 2)"

## create a venv

```bash
$ python3.10 -m venv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
```

## run app.py

```bash
(env) $ export SLACK_APP_TOKEN=<YOUR-APP-TOKEN>
(env) $ export SLACK_BOT_TOKEN=<YOUR-BOT-TOKEN>
(env) $ python app.py
⚡️ Bolt app is running!
```

## description of scripts

* app.py: simple bot app
* app-extend.py: extend bot(mention, regeular expression, handle event, emoji reaction)
* app-calc.py: `calc()` function
* plusplus_model.py: model code
* app-plusplus.py: `plusplus()` function
* app-jira.py: `jira_search()` function
* app-sheet.py: `create_issues()` function(data acquisition from sheets only)
* app-sheet2.py: `create_issues()` function(create Jira issues)
* app-admin.py: `user_list()` and `insert_user()` function
* app-admin2.py: `user_list()` and `insert_user()` function with admin confirmation
* app-deepl.py: `translate()` function
* quickstart.py: get credentials for google account

