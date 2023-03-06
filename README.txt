Instructions:
1.	Clone repo from https://github.com/Ian-Goodall-Halliwell/York-Battery, If they want to fork it on their end to have it in their own lab repo that’s totally fine. Just make a new fork and everything else will be the same. 
2.	Make sure anaconda is installed (with PATH, if that’s not allowed let me know, but as far as I know it’s required for this to work.).
3.	Run the .bat files 0 to 3 in the main repo directory. If the task battery does not run on the 3rd file, let me know as there is some issue with the install. You can also run file 0 and it should reset everything.
4.	You can change the configuration by editing the file config.py in the main directory. After running that file, a config.yaml will be generated in the main directory, this will be used when running the battery.

This is all that is needed to run the battery, but if you want to have automated syncing of the local repository with the online repository, there are two last steps. This is very useful if there are multiple computers running the battery.

1.	Edit the file sync.bat in the main directory, change the path in line 1 to the absolute path of the task battery main directory. If you have questions let me know. You can also change the text "Sync from PC1-YORK" on each line where it’s present to something else. This is what will be displayed on the commit history, and can help to determine problem systems.
2.	This file will work if you want to manually click it after new data is entered, if you want to automate it, open up the default windows program “Task Scheduler”. You should be able to load the file “Data_sync.xml” in task scheduler. You may need a password for this, and you may need to edit the path in the actions tab. You can also change when syncs will occur by changing the triggers tab. All of this can be tricky so let me know if you need help with it. It looks like hieroglyphics and it took me a couple weeks to wrap my head around it, so no worries if you need a better description.

With all that done, you should be ok to collect data. For the analysis, just run Analysis/analysis.py from the main directory. This will create two files, accuracy.csv and output.csv. These will contain the accuracy data and the full ESQ data. I’m not sure how well the analysis.py will play with sparse task completion, so I may need to edit a few lines.

In general, the structure of the repo is like this.

/
 -Analysis		#Contains the analysis script, as well as coords.csv which holds the gradient coordinates for our scans.
 -Internal_Logs		#Contains the raw output of the terminal the battery is run in. This is not data but can help troubleshoot if things go wrong.
 -Tasks			#Contains all the important code and data.
 	-log_file		#Here is where the data lives, in shortened and long form
	-taskScripts		#This is all of the task code. Abandon all hope ye who enter here.
	-mainscript.py		#This is the central script that runs the battery. 

REQUIREMENTS: 

Anaconda



