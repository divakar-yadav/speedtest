# Internet Speedometer

It’s made of client server architecture and
I am using flask for server and server side rendering for showing speedometer UI.

**Server Libraries** - python, flask,flask-cors, Speedtest

**Client** - Html, Java Script

The UI for speedometer is rendered using server side rendering and to get the latest data it keeps pinging the server to get the latest updated internet speed.


Steps for starting up the server.

1. Install python3 (most OS already had it )
2. Install virtual environment (depends on OS)
3. get into directory
   `cd /speedtest`
4. activate the virtual environment
   `source env/bin/activate`
5. install the dependencies
   `pip3 install -r requirement.txt`
6. Run the server
   `python3 app.py`
