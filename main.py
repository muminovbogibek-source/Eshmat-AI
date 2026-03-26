{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/muminovbogibek-source/Eshmat-AI/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install python-telegram-bot"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vajoKN9RJC_w",
        "outputId": "425d40ae-3fce-49d1-c9d4-246bac0219ef"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting python-telegram-bot\n",
            "  Downloading python_telegram_bot-22.7-py3-none-any.whl.metadata (17 kB)\n",
            "Requirement already satisfied: httpx<0.29,>=0.27 in /usr/local/lib/python3.12/dist-packages (from python-telegram-bot) (0.28.1)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.12/dist-packages (from httpx<0.29,>=0.27->python-telegram-bot) (4.12.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.12/dist-packages (from httpx<0.29,>=0.27->python-telegram-bot) (2026.2.25)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.12/dist-packages (from httpx<0.29,>=0.27->python-telegram-bot) (1.0.9)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.12/dist-packages (from httpx<0.29,>=0.27->python-telegram-bot) (3.11)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.12/dist-packages (from httpcore==1.*->httpx<0.29,>=0.27->python-telegram-bot) (0.16.0)\n",
            "Requirement already satisfied: typing_extensions>=4.5 in /usr/local/lib/python3.12/dist-packages (from anyio->httpx<0.29,>=0.27->python-telegram-bot) (4.15.0)\n",
            "Downloading python_telegram_bot-22.7-py3-none-any.whl (745 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m745.4/745.4 kB\u001b[0m \u001b[31m16.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: python-telegram-bot\n",
            "Successfully installed python-telegram-bot-22.7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install nest_asyncio"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "74cfHim-J0Uw",
        "outputId": "cd80fe06-1260-4430-f879-30dac0d06a22"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: nest_asyncio in /usr/local/lib/python3.12/dist-packages (1.6.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3Rf5XfvDrR98",
        "outputId": "c42f5148-c8e4-4363-8d58-64fe359e65ef"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: google-generativeai in /usr/local/lib/python3.12/dist-packages (0.8.6)\n",
            "Requirement already satisfied: python-telegram-bot in /usr/local/lib/python3.12/dist-packages (22.7)\n",
            "Requirement already satisfied: google-ai-generativelanguage==0.6.15 in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (0.6.15)\n",
            "Requirement already satisfied: google-api-core in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (2.30.0)\n",
            "Requirement already satisfied: google-api-python-client in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (2.192.0)\n",
            "Requirement already satisfied: google-auth>=2.15.0 in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (2.47.0)\n",
            "Requirement already satisfied: protobuf in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (5.29.6)\n",
            "Requirement already satisfied: pydantic in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (2.12.3)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (4.67.3)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (4.15.0)\n",
            "Requirement already satisfied: proto-plus<2.0.0dev,>=1.22.3 in /usr/local/lib/python3.12/dist-packages (from google-ai-generativelanguage==0.6.15->google-generativeai) (1.27.1)\n",
            "Requirement already satisfied: httpx<0.29,>=0.27 in /usr/local/lib/python3.12/dist-packages (from python-telegram-bot) (0.28.1)\n",
            "Requirement already satisfied: googleapis-common-protos<2.0.0,>=1.56.3 in /usr/local/lib/python3.12/dist-packages (from google-api-core->google-generativeai) (1.73.0)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.20.0 in /usr/local/lib/python3.12/dist-packages (from google-api-core->google-generativeai) (2.32.4)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.12/dist-packages (from google-auth>=2.15.0->google-generativeai) (0.4.2)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.12/dist-packages (from google-auth>=2.15.0->google-generativeai) (4.9.1)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.12/dist-packages (from httpx<0.29,>=0.27->python-telegram-bot) (4.12.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.12/dist-packages (from httpx<0.29,>=0.27->python-telegram-bot) (2026.2.25)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.12/dist-packages (from httpx<0.29,>=0.27->python-telegram-bot) (1.0.9)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.12/dist-packages (from httpx<0.29,>=0.27->python-telegram-bot) (3.11)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.12/dist-packages (from httpcore==1.*->httpx<0.29,>=0.27->python-telegram-bot) (0.16.0)\n",
            "Requirement already satisfied: httplib2<1.0.0,>=0.19.0 in /usr/local/lib/python3.12/dist-packages (from google-api-python-client->google-generativeai) (0.31.2)\n",
            "Requirement already satisfied: google-auth-httplib2<1.0.0,>=0.2.0 in /usr/local/lib/python3.12/dist-packages (from google-api-python-client->google-generativeai) (0.3.0)\n",
            "Requirement already satisfied: uritemplate<5,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from google-api-python-client->google-generativeai) (4.2.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.12/dist-packages (from pydantic->google-generativeai) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.41.4 in /usr/local/lib/python3.12/dist-packages (from pydantic->google-generativeai) (2.41.4)\n",
            "Requirement already satisfied: typing-inspection>=0.4.2 in /usr/local/lib/python3.12/dist-packages (from pydantic->google-generativeai) (0.4.2)\n",
            "Requirement already satisfied: grpcio<2.0.0,>=1.33.2 in /usr/local/lib/python3.12/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai) (1.78.0)\n",
            "Requirement already satisfied: grpcio-status<2.0.0,>=1.33.2 in /usr/local/lib/python3.12/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai) (1.71.2)\n",
            "Requirement already satisfied: pyparsing<4,>=3.1 in /usr/local/lib/python3.12/dist-packages (from httplib2<1.0.0,>=0.19.0->google-api-python-client->google-generativeai) (3.3.2)\n",
            "Requirement already satisfied: pyasn1<0.7.0,>=0.6.1 in /usr/local/lib/python3.12/dist-packages (from pyasn1-modules>=0.2.1->google-auth>=2.15.0->google-generativeai) (0.6.3)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.20.0->google-api-core->google-generativeai) (3.4.6)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.20.0->google-api-core->google-generativeai) (2.5.0)\n"
          ]
        }
      ],
      "source": [
        "pip install google-generativeai python-telegram-bot"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ba0CrNO2rUXx",
        "outputId": "90a57db7-28fc-4a29-e3b5-feb657692b5a"
      },
      "outputs": [
        {
          "metadata": {
            "tags": null
          },
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Gemini bot ishga tushdi 🚀\n"
          ]
        },
        {
          "metadata": {
            "tags": null
          },
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "WARNING:tornado.access:403 POST /v1beta/models/gemini-2.5-flash:generateContent?%24alt=json%3Benum-encoding%3Dint (::1) 759.13ms\n"
          ]
        },
        {
          "metadata": {
            "tags": null
          },
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "ERROR: 403 POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?%24alt=json%3Benum-encoding%3Dint: Your API key was reported as leaked. Please use another API key.\n"
          ]
        }
      ],
      "source": [
        "from telegram import Update\n",
        "from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes\n",
        "import google.generativeai as genai\n",
        "import nest_asyncio\n",
        "nest_asyncio.apply()\n",
        "\n",
        "# 🔑 TOKENLAR\n",
        "TELEGRAM_TOKEN = \"8701140143:AAEwCRP87hD-nIfL4Mf43KGCVLJVNhkbDaY\"\n",
        "GEMINI_API_KEY = \"AIzaSyDsIfZYRcCpn8G6bU4IddZQrLAsfp1fxCQ\"\n",
        "\n",
        "# Gemini sozlash\n",
        "genai.configure(api_key=GEMINI_API_KEY)\n",
        "model = genai.GenerativeModel(\"gemini-2.5-flash\")\n",
        "\n",
        "BOT_USERNAME = \"@Eshmat_AI_bot\"\n",
        "\n",
        "SYSTEM_PROMPT = \"\"\"\n",
        "You are Eshmat AI, a smart Telegram assistant.\n",
        "\n",
        "Rules:\n",
        "- Always try to answer every question\n",
        "- If you don't know, explain or guess helpfully\n",
        "- Never stay silent\n",
        "- Answer clearly and helpfully\n",
        "- Reply in user's language\n",
        "\"\"\"\n",
        "def should_reply(update: Update):\n",
        "    msg = update.message\n",
        "\n",
        "    if msg.chat.type == \"private\":\n",
        "        return True\n",
        "\n",
        "    if msg.text and BOT_USERNAME.lower() in msg.text.lower():\n",
        "        return True\n",
        "\n",
        "    if msg.reply_to_message:\n",
        "        if msg.reply_to_message.from_user.username == BOT_USERNAME.replace(\"@\", \"\"):\n",
        "            return True\n",
        "\n",
        "    return False\n",
        "\n",
        "\n",
        "async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):\n",
        "\n",
        "    await update.message.chat.send_action(\"typing\")\n",
        "\n",
        "    user_text = update.message.text.replace(BOT_USERNAME, \"\").strip()\n",
        "\n",
        "    try:\n",
        "        prompt = SYSTEM_PROMPT + \"\\nUser: \" + user_text\n",
        "\n",
        "        response = model.generate_content(prompt)\n",
        "        reply = response.text\n",
        "\n",
        "    except Exception as e:\n",
        "        print(\"ERROR:\", e)\n",
        "        reply = \"Xatolik keyinroq urinib ko‘ring\"\n",
        "\n",
        "    await update.message.reply_text(reply)\n",
        "\n",
        "import asyncio\n",
        "\n",
        "async def main():\n",
        "  app = ApplicationBuilder().token(\"8701140143:AAEwCRP87hD-nIfL4Mf43KGCVLJVNhkbDaY\").build()\n",
        "  app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))\n",
        "  print(\"Gemini bot ishga tushdi 🚀\")\n",
        "  await app.run_polling()\n",
        "await main()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import google.generativeai as genai\n",
        "\n",
        "genai.configure(api_key=\"AIzaSyDsIfZYRcCpn8G6bU4IddZQrLAsfp1fxCQ\")\n",
        "\n",
        "try:\n",
        "    model = genai.GenerativeModel(\"gemini-2.5-flash\")\n",
        "    response = model.generate_content(\"Salom\")\n",
        "    print(\"✅ API aktiv\")\n",
        "    print(response.text)\n",
        "\n",
        "except Exception as e:\n",
        "    print(\"❌ API aktiv emas\")\n",
        "    print(\"ERROR:\", e)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "id": "c0QBIVR1Gp_f",
        "outputId": "389a897d-4a33-4d82-9a52-013a1a78d80a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ API aktiv\n",
            "Salom! Qalaysiz?\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOZMlBovZJNbW7oTTuHPRY0",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}