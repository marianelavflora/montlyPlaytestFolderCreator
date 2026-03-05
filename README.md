
# montly Playtest Folder Creator
This is a productivity tool I developed to optimize my daily workflow as a Game QA Engineer. Instead of manually creating directories for every test session, this script handles the entire monthly organization in seconds.

#Key Features
1. Smart Calendar Integration: Automatically detects the current month and year (e.g., 03_March).
2. Business Day Logic: Only creates folders for Monday through Friday, skipping weekends.
3. Standardized QA Hierarchy: Generates nested folders for Sessions (1-3) and Matches (1-3) to keep test artifacts organized.
4. The folder gets created whetever you run the script (found this was easier for me)  

 <img width="564" height="748" alt="Screenshot 2026-03-05 134721" src="https://github.com/user-attachments/assets/1c310f49-2d14-4e76-9b10-81445eefbfa7" />


# How it works
1. Run: python dailyPlaytestFolderCreator.py
2. The script identifies the current month and generates the structure in your defined path.
3. The file explorer opens automatically so you can start dropping your logs and captures immediately.
