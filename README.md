# Bot IP Detector

BotDetector is an automation project to detect bot IPs for Optimus. This project created with Selenium and Python, also using some
pip packages for parallelize run. Let's dive into it!

### Requirements

- Python 3.8.10
- Chrome
- PyCharm IDE

### How to clone / install BotDetector

Open your terminal, go to your favorite directory for projects, type  
`https://github.com/mfurkandemiral/BotDetector.git`  
and hit enter. BotDetector will be cloned current directory.

After cloning, open Bot Detector project with PyCharm IDE and wait for first indexing progress. When indexing is finished, IDE
auto detects `requirements.txt` file and asks for creating virtual environment. Click "OK" button, IDE will be created
virtual environment and automatically installs required pip packages. From this point you can run tests, but you need
one more thing, described in next step.
<hr>

**The sheet name must be [Sheet1](https://github.com/mfurkandemiral/BotDetector/blob/d86c02940f7b929cdb0151f371b54cb51168b23c/tests/bot_detector.py#L24)**

![image](https://user-images.githubusercontent.com/105215223/191691778-362798bd-85cb-409f-b190-a26f89b49874.png)
<hr>

**You should put your Excel file in the files folder and edit its name [here](https://github.com/mfurkandemiral/BotDetector/blob/d86c02940f7b929cdb0151f371b54cb51168b23c/tests/bot_detector.py#L16).**

![image](https://user-images.githubusercontent.com/105215223/191692897-221b6362-ff86-460a-b50b-48bcaf24c09b.png)

![image](https://user-images.githubusercontent.com/105215223/191701823-ee9117b3-483c-49ac-a718-9ed7dee59f6f.png)
![image](https://user-images.githubusercontent.com/105215223/191701427-1b73e9f1-ea63-432f-9106-46474fc0249a.png)

<hr>

**You should edit the name of the strings found column [here](https://github.com/mfurkandemiral/BotDetector/blob/d86c02940f7b929cdb0151f371b54cb51168b23c/tests/bot_detector.py#L24).**

![image](https://user-images.githubusercontent.com/105215223/191705425-0ab98498-9cbe-4fd8-9b47-2f458bb018f7.png)
![image](https://user-images.githubusercontent.com/105215223/191692715-6fcc0251-59c8-42bb-89a8-50ca486314a5.png)
<hr>

### How to run tests

Test files are located in `tests` directory. Open `bot_detector.py` file, right click anywhere on file and click "Run",
pytest progress will be starts without opening the browser.
<hr>

**Note:** You can add the [words](https://github.com/mfurkandemiral/BotDetector/blob/d86c02940f7b929cdb0151f371b54cb51168b23c/tests/bot_detector.py#L18) you want to search by separating them with commas.

![image](https://user-images.githubusercontent.com/105215223/191703589-9bccfee2-8e15-4aba-ad76-ef43d464e08a.png)
<hr>

**Note:** When your test is finished, the outputs will be written to the `output.xlsx` file.

If you've seen such an warning, it's worth checking out.

This warning comes when the ip site queried has no database.

![image](https://user-images.githubusercontent.com/105215223/191704487-d74572e7-917b-4f89-b0dc-67240254a3d4.png)
![image](https://user-images.githubusercontent.com/105215223/191705681-249f0113-884e-412a-9233-680aa1a287a5.png)
