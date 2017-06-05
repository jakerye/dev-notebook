# Heroku Postgres Notes

Here is a good entry point
- https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-the-add-on

Export database url to environment
```
export DATABASE_URL=`heroku config:get DATABASE_URL`
```
Note: should probably just add this line to virtualenv activate so always in local dev session
```
nano my_project_folder/my_project_name/bin/activate
```
Note: should also add this to *.env* file so var gets set in deployed heroku app
```
heroku config:get DATABASE_URL -s >> my_project_folder/.env
```
