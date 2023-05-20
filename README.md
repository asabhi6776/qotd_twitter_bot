# Python Quote of the Day Bot for Twitter

This is a Python-based bot that fetches a random quote from an API and posts it on Twitter. It also sends notifications to a Discord webhook in case of any errors or failures.

## Usage

1. **Install Dependencies:**

    Make sure you have the necessary libraries installed. You can install them using pip:

    ```shell
    pip install -r requirements.txt
     ```

2. **Obtain Twitter API Credentials:**

    To use the Twitter API, you need to have valid API credentials. If you don't have them, you can create a Twitter Developer account and create a new app to obtain the credentials.
    Replace the placeholder values in the code with your actual Twitter API credentials:
    ```env python
    YOUR_CONSUMER_KEY
    YOUR_CONSUMER_SECRET
    YOUR_ACCESS_TOKEN
    YOUR_ACCESS_TOKEN_SECRET
    ```
3. **Set up Discord Webhook:**
    Create a Discord server and obtain the webhook URL to send notifications.
    Replace YOUR_DISCORD_WEBHOOK_URL in the code with your actual Discord webhook URL.
    Run the Code:

    Save the code to a Python file, such as qotd.py.

    Open a terminal or command prompt and navigate to the directory containing the Python file.

4. **Run the code using the Python interpreter:**
    ```shell
        python qotd.py
    ```
## Result:

    - The code will fetch a random quote from the "quotable.io" API.
    - If a quote is successfully fetched, it will be posted on your Twitter account.
    - If there is an error while tweeting, a notification will be sent to the configured Discord webhook indicating the failure.
    - If the quote cannot be fetched from the API, a notification will be sent to Discord indicating the failure.

**Note:** Make sure you have a stable internet connection and valid API credentials to successfully tweet and send notifications. Monitor the console output for any error messages or status updates.