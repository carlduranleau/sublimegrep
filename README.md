## Introduction

Here's a search and extract plugin for Sublime Text that allows to extract all lines of the current file that matches a specific pattern to a new file. For example, to extract all the line for a specific test in a Jenkins console log file, simply open the console.log file and use the plugin to search for the test name since it should be found in the SID part of each line.

## Installation

There's no script to run or complex installation program to run to install news plugins in Sublime Test. Simply copy the files to specific folders and the new feature will be available immediately.

1. Steps to install the Grep plugin:
2. Download the plugin files from here
3. Extract the files in this paths:
```
    ~/.config/sublime-text-3/Packages/plugins/grep.py
    ~/.config/sublime-text-3/Packages/plugins/grepregex.py
    ~/.config/sublime-text-3/Packages/Main.sublime-menu
    ~/.config/sublime-text-3/Packages/Default (Linux).sublime-keymap
```

Note that these paths are for Sublime Text 3 on Ubunbu 16.10, but files can be installed on any OS supporting Sublime Text 3 using specific OS paths. See Sublime Text documentation.
You should then see a new 'Plugins' menu with two options:

![New Plugins menu](doc/plugin_menu.png?raw=true)

## Usage

There's two options with this plugin:
* Grep = Plain text search
* Grep Regex => Regular expression search

To use the new features, simply open the source file in Sublime Text and select the wanted option from the Plugins menu. A bar will appear at the bottom to allow you to insert the search expression:

![Search bar](doc/plugin_search.png?raw=true)

Enter the search expression and hit ENTER. Depending on the size of the source file, it may take few seconds to parse. After the parsing is completed, a new file will open with all the lines matching the specified expression. Note that this file is not saved on disk. So you can save it, or launch another search for the results.

## Distribute and update!

Feel free to distribute and/or update this plugin. Thanks to you!
