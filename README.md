# Random Emotion Generator

This is a small web app that generates a random emotion from a prefactored
list that appear on the "wheel of feelings". It then displays that emotion as
well as the wheel to show the context of that specific emotion.

#### Tech

Uses zappa to deploy to a lambda with an API Gateway wrapped around it.
Developed using this tutorial: https://towardsdatascience.com/deploy-a-python-api-on-aws-c8227b3799f0

To deploy:

```
export AWS_DEFAULT_PROFILE=zappa
zappa deploy dev
```

Is created from a simple flask app in app.py with all logic for the app
contained within. To run locally:

```
flask run
```

-ZWM 2022
