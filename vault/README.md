# Vault
Storing secrets securely and conveniently. Similar to Heroku config but doesn't require using Heroku.

## Why Care?
Stjepan Hadjić [frames the problem perfectly](https://infinum.co/the-capsized-eight/hiding-secrets-in-vault):

>Every application needs configuration data like database passwords, AWS access keys, and social app IDs before it can run. What's the easiest way to do it? Hardcode those values, push them to Git and everyone who has a copy of the source code can run the application. The only problem is, you don't want the whole world to know your usernames and passwords. They need to be kept secret. They need to be kept safe.

>Point III. of the 12-factor methodology calls for a strict separation of configuration from code.

>This means removing your database configuration and similar files from version control and copying them directly to your server and CI. That, I don't need to tell you, is a tedious job. Additionally, this approach is highly prone to errors and makes it harder to collaborate with other developers. You and all your collaborators need to remember to update configuration files everywhere.

>Having multiple environments (such as production, staging, and acceptance) with different configuration files makes this even more difficult.

>Heroku solved this problem through its config setup. All configuration files can be set with heroku config:set independently for each environment.

>If you have your own servers like us, Heroku's strategy of using environment variables won't work as easily. This is where Vault comes into play. We use HashiCorp's Vault to store and retrieve our secrets.

