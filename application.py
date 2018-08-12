import os

from flask import Flask, session, render_template, request
from flask_socketio import SocketIO, emit
from models import *

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


messages = []


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        name = request.form.get("name")
        newMessage = Message(name=name, text=text)
        messages.append(newMessage)

    return render_template("message_page.html", messages=messages)


# Make singular chat page that everyone can message on in real time
    # Make a message submission that gets added to the page
    # Make the page update with the info in real time
    # Dont refresh page but just add
    # Make messages persist even when page closes
    # Allow multiple people to access the same page
    # Allow users to display their name alongside their message
    # Allow users to customize their __name__

# Make multiple pages for different chats
    #Make the chatroom name display at top of pages
    #make chatroom appear off to side of pages
    #Make channel be remembered when the page is re-opened
    #allow user to create a new channel


#limit chatroom data to 100 messages

#decide on some sort of personalization at this point
