Clash of Clans Player Tag and Clan Tag Sequencer
-------
Use this tool to locate old players and clans, so that you can contribute to the game's history or save historical artifacts from destruction!**

This is a [very primitive] tool written in Python. I have not determined if it works the same way today, but for the oldest accounts and clans from 14 June - 1 August 2012, it is 100% accurate.


**DISCLAIMER
-------
Supercell deletes accounts after 6 years of inactivity. This means Supercell can delete historically significant clans if there is no other account in the clan to which the deleted account can pass its Leader role. 

THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY. This material is unofficial and is not endorsed, affiliated with, sponsored, or specifically approved by Supercell and Supercell is not responsible for it. For more information see [Supercell's Fan Content Policy.](https://www.supercell.com/fan-content-policy)

REQUIREMENTS
-------
I would recommend an IDE (Integrated Development Environment) because it is the easiest to install and operate. You can also use it for activities other than this one.
1. Install an IDE like [VSCodium](https://github.com/VSCodium/vscodium/releases) on your system.
2. Make sure you have the stuff for Python installed in the IDE (a good IDE would prompt you when you try working with a .py file)

RANGE_SEQUENCER.PY USAGE (most useful)
-------
In an IDE:
1. Open the .py file in your IDE (can be done from the File tab of the IDE)
2. Enter the bottom range of tags you want to see. Example: if you want to see the first account's tag, type "1" without the quotes and click your Enter key.
3. Enter the top range of tags you want to see. Example: if you want to see the everything up to and including the 5000th account's tag, type "5000" without the quotes and click your Enter key.
4. A tags.txt file should be exported to the same directory in which the range_sequencer.py file resides.
5. Open the tags.txt file and profit

INDIVIDUAL_SEQUENCER.PY USAGE (less useful, would give you your base 256 binary if you're interested)
-------
In an IDE:
1. Open the .py file in your IDE (can be done from the File tab of the IDE)
2. You will get two choices, 0 for tag to number, and 1 for number to tag. CHOOSE CHOICE "0" without the quotes. The program wants a base 256 binary for choice 1 and you do not have that number.
3. Enter your tag and click your Enter key.
4. Program will tell you your base 256 binary array for your player tag.
5. You will see a string of numbers like 0, 0, 0, 0, 0, 0, 0, 0 but with real numbers in it.
6. Convert to a useful number. Ex: 0, 0, 0, 0, 0, 1, 1, 1 = (1 * (256^2)) + (1 * (256^1)) + (1) = 65,793.
7. What does the number mean? Well, if a player tag ever resolved to this binary, then it would be the 65793rd account, but the binary array is made-up, so it wouldn't.

CONTACT
-----
Instagram: [@bxns.coc](https://www.instagram.com/bxns.coc/)
