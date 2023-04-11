#OpenAIBot Telegram Chatbot
 - This is a simple Telegram chatbot that uses the OpenAI API to generate responses to user messages. It is based on the Python package aiogram.

##Prerequisites
>Python 3.7 or higher
>A Telegram bot token. You can get one by talking to the BotFather on Telegram.
>An OpenAI API key. You can get one from the OpenAI website.
##Setup
Clone this repository and cd into it:

```
git clone https://github.com/AbdulrahmanTohamy/OpenAIBot.git
cd OpenAIBot
```
Install the Python dependencies:

```
pip install -r requirements.txt
```
Set the environment variables:
```
export TELEGRAM_BOT_TOKEN=<your_telegram_bot_token>
export OPENAI_API_KEY=<your_openai_api_key>
```
Run the bot:
```
python bot.py
```
Usage
Start a conversation with your bot on Telegram.
Send a message to the bot and wait for a response.
Deployment
This chatbot can be deployed on a cloud service provider such as Heroku, Google Cloud Platform, or AWS. You will need to create an account and follow their instructions to deploy the app.

Alternatively, you can use a service like pythonanywhere to deploy the bot without needing to create an account.

Deploying on pythonanywhere
Create a new account on pythonanywhere.com.
Click on the "Consoles" tab and open a new Bash console.
Clone this repository:
```
git clone https://github.com/AbdulrahmanTohamy/OpenAIBot.git
cd OpenAIBot
```
Install the dependencies:
```
pip3.8 install -r requirements.txt
```
Set the environment variables:
```
echo "export TELEGRAM_BOT_TOKEN=<your_telegram_bot_token>" >> ~/.bashrc
echo "export OPENAI_API_KEY=<your_openai_api_key>" >> ~/.bashrc
```
Reload the bashrc file:
```
source ~/.bashrc
```
Run the bot:
```
python3.8 bot.py
```
Click on the "Web" tab and then on the "Add a new web app" button.
Choose "Manual configuration" and follow the instructions to set up the web app.
Once the web app is set up, click on the "Reload" button to start the bot.
Credits
This code was created by @th3tommy.
The @aiogram Python package was created by @Alex Root.
The OpenAI API was created by @OpenAI.
