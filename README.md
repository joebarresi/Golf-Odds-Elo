# Golf-Odds-Elo

## How to Deploy Code to Amazon EC2 instance:
Just for basic understanding, we are running the code in main.py using mangum and nginx. We have an EC2 instance running that will actually run that code. I used this public tutorial: https://github.com/pixegami/fastapi-tutorial/blob/main/README.md

1. SSH into EC2 instance: Go to linux terminal and run: Ask me for the keypair file if you haven't yet
```
ssh -i ~/.ssh/keypair.pem ubuntu@<Instance Public IP>
```
2. Remove current Golf-Odds Repository and Clone our existing one:
```
git clone <repository-url>
```
3. Run the server: First type in tmux attach, this will take you a seperate terminal. Then run these:
```
sudo service nginx restart
cd <repository-name>
python3 -m uvicorn main:app
```
Leave by typing ctrl-B, then D

Biggest TODOs:
Front End
- Begin work on a simple react file that will just call our python server
- Simple navbar and title page
- deploy simple code
- 

Backend/API
- Have API call for books that are working/not working
- Optimize/Refactor Weils code to be as efficent as possible
- Start working on back-end node file that can: create scheduling of API calls and begin storing these odds into a dynamodb

