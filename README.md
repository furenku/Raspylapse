#timelapse.py:


##Setup 


###Dependencies:

Install Image Magick

`sudo apt-get install imagemagick


###Set-up

1. Clone repo

	`git clone https://github.com/furenku/Raspylapse.git`


2. Enter project

	`cd Raspylapse`


3. create symlink to project's 'html' folder inside server's public web folder (example: /var/www/ )

	`sudo ln -s html /var/www/time-lapse`


4. Change code's path to match your filesystem's

	`timelapseDir = "your/path"`


5. Run ze code:

	`python timelapse.py`


5. Check if gif created successfully

	`ls html/gif`


6. Point browser to http://localhost/time-lapse (or wherever you put it)



Code was based around this example:
http://picamera.readthedocs.org/en/release-1.0/recipes1.html#capturing-timelapse-sequences
