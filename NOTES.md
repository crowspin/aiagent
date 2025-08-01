## Aside
This is my preferred note taking method when I'm working on a project, so I'm going to go back to it. PirateSoftware has his Dwayne the Rock Johnson; I've got my text-based brain dumps. Helps keep things organized in my head.  
Usually this involves checklists and idea tracking, but it'll just be for breadcrumbs where the boot.dev projects are concerned.

## C1-L5
A quick breakdown of the project so far:  
```
    We created a repo on Github  
    We created a folder on the local drive.  
    Using VSCode:  
        We ran the "new repo" commands provided by Github in the VSCode terminal to sync  
        the folder with the repo  
            echo "# aiagent" >> README.md  
            git init  
            git add README.md  
            git commit -m "first commit"  
            git branch - M main  
            git remote add origin https://github.com/crowspin/aiagent.git  
            git push -u origin main  
        Following Boot.Dev we:  
            uv init ../aiagent  
                    because we're already in the folder it'll try and make  
            uv venv  
            source .venv/bin/activate  
            uv add google-genai==1.12.1  
                    gross  
            uv add python-dotenv==1.1.0  
        App can now be run via.  
            uv run main.py  

    For the app thus far: we've had to register with [aistudio.google.com] to get an API key  
                    gross  
    Create a .env file for the API Key to be stored, then hide that file using .gitignore  

    In code: we need the os and dotenv imports for the hidden .env file, these presumably have  
    extra security measures for api keys and passwords and such. Otherwise what would be the  
    point compared to the constants.py we did in the Asteroids project?  
    The sys import is for sys.argv which gives us the command arguments  
    and the google imports are for the ai llm stuff  
                    gross  
        
    We call load_dotenv to place the .env values into an OS environment memory space (so then  
    it could be that the key needs to be accessible outside the applet for the ai system?),  
    set up the ai, and so far, just fire off a test prompt to a free-tier model. At first  
    the prompt was hardcoded, but now it comes from the first argument from the command line.  
```

## C1-L6
Just because I'm really proud of how quickly I've been able to move through the curriculum so far, I want to say 'out loud' that I'm going to be slowing down intentionally for the next week or so. As wicked cool as it would be to finish the whole jam in a single month instead of twelve, I don't really think the difficulty is going to stay low enough for me to support that pace. Even if Course 7 was a lot of (10/10) difficulty lessons. I've got a camping trip coming on the weekend after next, and I've worked with C++ enough to know I won't be able to take that course without a proper computer to compile my work. I guess the class might have a live-compiler, or just do text parsing, but I doubt it. So I'm going to finish this chapter for the morning, and save Course 9 for while I'm away and on my tablet. 
```
    Not really much in this lesson worth noting like this, just an argument flag capture
    Just felt obligated to have something related to the lesson itself under it's header
    hahaha
```

## C2-L3
```
    Had to add __pycache__ to .gitignore
        Not sure where those files are coming from yet, but they're auto generated, so
        probably not git-worthy
    config.py just has a max character read-length constant for get_file_contents
    \tests.py has some test cases for \functions
    lorem.txt is stock text
    contents of \calculator not generated/written by me

    get_files_info and get_file_content both have an instruction in their lessons to catch  
    ~other~ errors they aren't naming and I can't find in the docs so I've caught a possible  
    OSError in one, and done nothing in the other and I'm just gonna pray I guess. Might be  
    something with file permissions later, but unclear at this time.
```

## C2-L4
Yeah, so, it was bugging me about the whole "I'm supposed to catch errors and I can't figure out which ones (Lane?) means" thing. So I asked Boots. :deep_shame:  
In get_files_list I already had a try block over the potentially bad block, but I hadn't returned an error message, which was no bueno. And in get_files_info I had identified that open() was the likely offender, but I had done some googling and found what might have been outdated info that suggested that try..except and with.. blocks were incompatible. StackOverflow has failed me.
Anyhow, the error catches for those functions are now in place.
```
    New test package
    backup of lorem.txt because it's been overwritten
    write_file added
```

## C3-L4-a
I need to fire this off quickly before I head for work, but I can't submit the answer to the lesson at this time. The work for *this* lesson is fine, but it seems I'm getting the wrong output from run_python_file along STDOUT. Maybe I've not captured it correctly, I'm sure it'll be a one line fix, but I gotta run. Can't be late for the thing that pays my bills.

## C3-L4-b
I realized a few seconds after I posted that last commit that I'd copy-pasted my subprocess.run usage from the docs, and forgotten to actually pass it the python file. So after telling it to use python and run the file, now it works fine. One line, as predicted. :facepalm: