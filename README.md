# ADDED 
# Conversation-Mode and Actionable Notifications with TTS/STT

I have added a few lines in the Core/__init__.py which allow the following:
- Integrated the possibility to activate an Conversationmode<p>
How to?<br>
   - At first you need to install the integration pyscript, which allowed you to use my **get_mp3_duration_streamassist_.py** Script. https://github.com/custom-components/pyscript
   - Then you must copy the **get_mp3_duration_streamassist_.py** in the **homeassistant/pyscript.**
   - Export and save the TTS mp3 URL to open it with the script get_mp3_duration_streamassist_.py and read the file length, which is needed to automatically reactivate the microphone at the end of the TTS.
   - You need to create an helper where you can save the URL from the TTS mp3 file. It is copied to the following helper entity **input_text.url_stream_assist** If you want a different name, you have to change the name in the Core/__init__.py script.   
   - You need to create an helper where you can save the duration from the TTS mp3 file. It is copied to the following helper entity **timer.extract_mp3_time_streamassist**. If you want a different name, you have to change the name in the get_mp3_duration_streamassist_.py script.
   - An additional automation (automation_conversation.txt) is then used to start the script **get_mp3_duration_streamassist_.py** and then another script **script.streamassistlivingroom** is used to restart the microphone at STT without a wakeword.<br>

   **However, this only happens if you want it to, an additional helper is created for this purpose, which can be activated by voice, a real switch on the wind, NFC, etc. In my automation example input_boolean.conversation_livingroom)**

- Changed the music type from **audio** to **music**, so now the STT Start Media File can played on devices with the KIOSK Mode and still can use with the cameras i tested.

- Now you can do Actionable Notifications with TTS/STT with the Assist

   How to?<br>
   - You need to create an helper where you can save the STT-Text from youre sentences. It is copied to the following helper entity **input_text.stt_streamassist** If you want a different name, you have to change the name in the Core/__init__.py script.
   - You can still use this helper, but i create a second helper, where i clone the answer again in **input_text.stt_streamassist_answer** after the TTS Assist Question **STT Streamassist Answer_copy**. A Example Script is attached **actionable script Test**.<br>

   However, there is still a problem, because the question that is generated at the beginning is not run via Stream Assist but via the direct HA pipeline, I cannot read out the length of the mp3 file. I have not yet found a way to retrieve the URL from the internal pipeline. If anyone here has a solution, please let me know.
<br>
<br>
<br>

**The use of the scripts and integration is at your own risk. They work well for me. However, this is no guarantee that it will work everywhere. In any case, make a backup beforehand**


