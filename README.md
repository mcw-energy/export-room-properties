# export-room_properties

export honeybee room properties to excel

## Quickstart

Install dependencies:

```
> pip install -r requirements.txt
```

Start Streamlit

```
> streamlit run app.py

  You can now view your Streamlit app in your browser.

  Network URL: http://172.17.0.2:8501
  External URL: http://152.37.119.122:8501

```

Make changes to your app in the `app.py` file inside the "app" folder.

## Run inside Docker image locally (Optional)

You can run the app locally inside Docker to ensure the app will work fine after the deployment.

You need to install Docker on your machine in order to be able to run this command

```
> pollination-apps run app marentette --name "export-room_properties"
```

## Deploy to Pollination

```
> pollination-apps deploy app --name "export-room_properties" --public --api-token "Your api token from Pollination"
```



## Configure Github Actions

In order to configure github actions to deploy your app you will need to:

1. [Create](https://docs.github.com/en/get-started/quickstart/create-a-repo) a repository on Github
2. [Add](https://docs.github.com/en/actions/security-guides/encrypted-secrets) a secret called `POLLINATION_TOKEN` with your Pollination API key as the value
3. Create [a new release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) of your app on Github with a new tag

Github actions will then package and deploy your code to an app called [export-room_properties](https://app.pollination.cloud/marentette/applications/export-room_properties)




