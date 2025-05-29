# Coderator Discord Bot

## About Coderator

Coderator is a Discord bot designed to generate images based on messages in a selected channel. Powered by the integrated Gemini engine, the bot transforms text into stunning visuals using your Gemini API key.

### Requirements

To use Coderator, ensure the following environment variables are set:
- **BOT_TOKEN**: The token for your Discord bot.
- **GEMINI_TOKEN**: Your API key for Gemini.
- **DATABASE_USER**: The username for accessing the database.
- **DATABASE_PASSWORD**: The password for the database user.
- **DATABASE_HOST**: The hostname of your database server.
- **DATABASE_PORT**: The port number for your database server.
- **DATABASE_NAME**: The name of your database.

Without these variables, the bot will not function properly. Additionally, you can modify the database driver in `config.py` to suit your specific requirements.

### Features

- Seamless integration with Discord channels.
- High-quality image generation using Gemini.
- Easy setup and configuration.
- Database support for storing and managing bot data.

Start creating visuals directly in your Discord server with Coderator today!