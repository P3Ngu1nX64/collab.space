#Author: Darren Zhu
#Version: Alpha 20w15a
#Purpose: Removes .DS_Store files in directory

#Global path to Folder (Auto Fetch)
#MAINPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )/"

#Doesn't work at the moment, a simpler solution is provided.
#rm -f "${MAINPATH}.DS_Store"
#rm -f "${MAINPATH}*/.DS_Store"

#Code (only works when executed in its own directory)

find . -name ".DS_Store" -type f -delete
