# sm_stayawake
-----------------------------------------------------------------------------------
IMPORTANT: Follow all instructions and setup, otherwise sm_stayawake will not work.
-----------------------------------------------------------------------------------

About sm_stayawake:
1. The purpose of sm_stayawake is to keep modern studio monitor speakers from turning off into standby.
2. To Achieve this, sm_stayawake plays an inaudible 10Hz tone at 50 % volume for about 20 seconds. 
3. There are 4 sec fade in/outs to not produce a popping sound.

System Requierments: 
1. Windows 10/11
2. Windows media volume needs to be turned on and turned up (at a normal listening level) for sm_stayawake to function.
3. Interface volume needs to be turned up to a normal level.

How to use:
1. Opening sm_stayawake.exe will only run wake tone once.
2. In order to play sm_stayawake every 15 minutes it will need to be scheduled using Windows Task Scheduler.
3. Once set up, sm_stayawake will run automatically without user input.


----------------------------------------------
IMPORTANT SETUP: Steps to schedule using Windows Task Scheduler:
----------------------------------------------

1. Open Windows Task Scheduler:
	win + R
	Insert: taskschd.msc
	Enter

3. Navigate to: "Task Scheduler (local)>Task Scheduler Library"

4. Action>Create Basic Task

5. Name: sm_stayawake

6. Click: Next

7. Choose: When i log on

8. Click: Next

9. Start a program

10. Click: Next

11. Browse to extractionfolder/sm_stayawake.exe

12. Click: Next

13. Check "Open the properties dialog for this task when I click finish

14. Click: Finish

15. Triggers>Edit

16. Check "Repeat task every:" 

17. Select "15 minutes"

18. "for a duration of" Choose "indefinitely"

19. Click: OK

20. If using a laptop, go to "conditions" tab and choose the appropriate power options. 
	Standard settings only work while plugged in to AC power.

21. Click: OK

22. Restart PC. The Task should now be triggered, and continue to run every 15 minutes.

--------------
 Done! Enjoy!
--------------
