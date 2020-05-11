# lazyweek
I tried searching for the generator that would help me ease the process of writing the weekly report for my credit-bearing internship, but I couldn't find one. One of my ideas was to use ML to create a tool which would create a make-sensible lie. However, I don't know ML yet, so that's out the window right away. Another idea is to create a tool which would randomly choose a sentence from a pool of sentences and just put a random keyword into KEYWORD place. So that's what I did.

## How to use it?
For that you only need python3. If I did everything properly, there are no other dependencies to it. To use it, just type into terminal:
```
git clone https://github.com/KtlTheBest/lazyweek.git
cd lazyweek
python3 main.py
```
If everyting works properly, it would create a report named `1.report` in a folder named `sample_project`. Each consecutive run increments the number of the report.

## How it works?
The code needs several files to operate: config file, openers file, phrases file and keywords file. Soon I will add a header and finisher files. They will contain a text that would be added before and after the report. You can use it to automatically put the week number, week date range or other important information you think is needs to be added.

To create openers and phrases file, you need to put a bunch of phrases that you want to appear in your report. If you want to put some keyword inside a sentence, you need to write `KEYWORD` (all in CAPS). The difference between openers and phrases is that there is always one opener per report. That's just how it is. To delimit the phrases, use `;`. The code will take everything except the `;` (including the spaces and newlines!!). That's just how it is.

To create a keywords file, need to put a bunch of keywords one after another and delimit them with `;`.

> Important note: the openers, phrases and keywords files must be non-empty (e.g. contain at least one phrase or keyword). That's just how it is.

You can specify which files to use, by specifying with command-line arguments or by changing `config.py` file. I believe that everything is pretty simple there.

## Okay, what's next?
So, I've written the alpha version of it, but there are still things that I need to finish, namely:
 - Test whether the command line arguments work properly
 - Write a help message and add -h/--help argument
 - Add header parsing (half-way done)
 - Add proper keyfile syntax
 - Add proper documentation
 - Add automatic export into file formats such as `.doc`, `.docx`, `.odt` and `.pdf`.
