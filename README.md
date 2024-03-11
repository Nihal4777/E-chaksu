# E - Cakṣu

The project aims at developing a smart eye called: E - Cakṣu, which can be used by visually impared people to overcome their viewing difficulty. The smart glasses for the visually impaired leverage Raspberry Pi Zero and it's camera module to offer comprehensive audio descriptions of the user's surroundings. This aids in navigation and is complemented by a Q&A feature, enabling users to interact with the environment. The project aims to empower visually impaired individuals through Google's Vertex AI, fostering greater independence and accessibility.

**Note:** This project contains the script which needs to be executed on Raspberry Pi Zero W which is connected with camera module and to circuit like shown below:

![Circuit design](https://github.com/Nihal4777/E-chaksu/assets/65150640/92936784-df69-4a8d-a588-673d46c64f62)


## Executing Instructions:
1. Place the Google Cloud Service Account credentials file in the same directory with the name *keys.json*
2. Connect the Raspberry PI Zero with Bluetooth Headset. Such that it connects automatically on starup.
3. Add the main.py in the startup script.
4. Reboot the Raspbery PI Zero
