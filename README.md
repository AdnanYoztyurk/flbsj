# flbsj
Python script to find large files (150 MB used as the cap) in specific folders and save the list to a CSV file.

# Situation
Our department has a common storage area to save files like important documents, scripts, databases. Sometimes we need to scan and flag all files when we are experiencing free disk space issues or need to change mappings of connections to databases. 

# Approach
I created this very simple and stupid script in a short time. It works relatively fast for marking files larger than 150MB and writing to a CSV file.

# Result
Team used the output to delete unnecessary files to free up the disk. Also, I slightly modified the script to change hostnames, which took 30 minutes. I hope you find it useful and would like to use some parts of the script.

# Author
Adnan Yoztyurk
