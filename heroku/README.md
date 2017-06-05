# Heroku Notes
Notes on using heroku

## Install
Mac
```
brew install heroku
```
Debian / Ubuntu
```
sudo apt-get install software-properties-common # debian only
sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install heroku
```


## Usage
Navigate to folder and create new Heroku app
```
heroku create
```
Deploy to Heroku
```
git push heroku master
```
Scale Dynos
```
heroku scale web=1
```
Open Heroku app home page
```
heroku open
```
Link a folder with an existing heroku app
```
heroku git:remote -a <app_name>
```
Deploy heroku locally...will host api at localhost:5000
```
heroku local
```

## Remove Remote Branch
If branch name is "staging"
```
git remote rm staging
```
