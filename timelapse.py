#!/user/bin/env python

import os
import time
import picamera
import datetime
import argparse

def main(captureTime=528.0, movieDuration=60, framerate=30, resolution=(1280,720),
        quality=85, startTime=None):
    """
    Record jpeg images to a /time-lapse folder based on the captureTime and movieDuration
    values, + any extra passed in args.  Saved files will overwrite any previous
    files left in that folder.

    Parameters:
    captureTime : float : Default 1.0 : How long should te recording go on for in HOURS.

    movieDuration : int : Default 60 : How long should the final movie last in SECONDS.
        For example, if you want the resultant movie to be 1 minute, that = 60 sec.

    framerate : int : Default 30 : Expected frames per second of the movie
        generated from these frames.  Used to calculate how often to take a pic.

    resolution : (x, y) : Default (1280, 720) : The resolution to capture at,
        default is 720p.  The cam can go higher of course, but this tends to fill
        up my sd card.

    quality : int : Default 85 : If the format is 'jpeg', set the quality, from
        1 to 100.

    startTime : datetime.datetime / None : If not none, an instance of a datetime.datetime
        class, specifying when to start the recording.
    """
    if startTime:
        assert isinstance(startTime, datetime.datetime), "startTime argument must be a datetime.datetime instance"

    captureTimeSec = int(captureTime * 60 * 60)
    movieFrames = int(movieDuration) * int(framerate)
    interval = float(captureTimeSec) / movieFrames
    totalPics = int(captureTimeSec / interval)

    timelapseDir = "/home/user/path/to/Raspylapse/generated_images"

    # en mi compu: /home/furenku/chamba/less/raspgif/Raspylapse/generated_images

    if not os.path.isdir(timelapseDir):
        os.mkdir(timelapseDir)

    print len([name for name in os.listdir(timelapseDir) if os.path.isfile(os.path.join(timelapseDir, name))])

    if startTime:
        now = datetime.datetime.now()
        print "Will start recording time-lapse on:", startTime
        while now < startTime:
            try:
                now = datetime.datetime.now()
            except KeyboardInterrupt:
                # User pressed ctrl+c
                print "Exit via user input"
                return

    print "Time-lapse begin! : Take a picture every %s seconds, for %s hours.  That's %s pictures!"%(interval, captureTime, totalPics)
    
    imagesGenerated = 0
    
    os.system("convert generated_images/*.jpeg -delay 20 -loop 0 html/gif/timelapse.gif")

    try:
        with picamera.PiCamera() as camera:
            print "Starting camera..."
            camera.resolution = resolution
            if format == 'jpeg':
                camera.quality = quality
            camera.start_preview()
            time.sleep(2)
            startT = time.time()
            print "Capture begin:"
            for filename in camera.capture_continuous('%s/timelapse{timestamp}.jpeg'% (timelapseDir)):
                print('\tCaptured %s' % filename)
                time.sleep(interval)
                timeNow = time.time()
                elapsedTime = timeNow - startT
                
                imagesGenerated=imagesGenerated+1

                if imagesGenerated % 5 == 0 :
                    os.system("convert generated_images/*.jpeg -delay 20 -loop 0 html/gif/timelapse.gif")


                if elapsedTime >= captureTimeSec:
                    break
                else:
                    percent = (elapsedTime / captureTimeSec)*100
                    print "\t\t%s / %s seconds, %.2f%% "%(int(elapsedTime), captureTimeSec, percent)
    except KeyboardInterrupt:
        print "Capture exited early..."
        return

    
    print "Capture complete!"

# If executed from the command line:
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Time for time-lapse!  '+
                                                 'To start recording at a certain time, pass in any or all '+
                                                 'of the time related args.  If no time-related args are '+
                                                 'passed in, recording will start immediately.')
    parser.add_argument('-ct', '--captureTime', metavar="float", type=float, help='in HOURS, default 1.0', default=1.0)
    parser.add_argument('-dur', "--duration", metavar="int", type=int, help='of final movie in SECOMDS, default 60', default=60)
    parser.add_argument('-fps', "--framesPerSecond", metavar="int", type=int, help='of final movie (default 30)', default=30)
    parser.add_argument('-xres', "--Xresolution", metavar="int", type=int, help='of image (default 1280)', default=1280)
    parser.add_argument('-yres', "--Yresolution", metavar="int", type=int, help='of image (default 720)', default=720)
    parser.add_argument('-q', "--quality", metavar="int", type=int, help='of jpeg from 1-100 (default 85)', default=85)
    parser.add_argument('-y', "--year", metavar="int", type=int, help='...to start recording', default=None)
    parser.add_argument('-m', "--month", metavar="int", type=int, help='...to start recording', default=None)
    parser.add_argument('-d', "--day", metavar="int", type=int, help='...to start recording', default=None)
    parser.add_argument('-hr', "--hour", metavar="int", type=int, help='...to start recording', default=None)
    parser.add_argument('-min', "--minute", metavar="int", type=int, help='...to start recording', default=None)
    parser.add_argument('-s', "--second", metavar="int", type=int, help='...to start recording', default=None)
    args = parser.parse_args()

    # Setup our start time if any time args are passed in:
    startTime = None
    if any((args.year, args.month, args.day, args.hour, args.minute, args.second)):
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        if args.year:
            year = args.year
        if args.month:
            month = args.month
        if args.day:
            day = args.day
        if args.hour:
            hour = args.hour
        if args.minute:
            minute = args.minute
        else:
            minute = 0
        if args.second:
            second = args.second
        else:
            second = 0
        startTime = datetime.datetime(year=year, month=month, day=day, hour=hour,
                                      minute=minute, second=second)

    main(args.captureTime, args.duration, framerate=args.framesPerSecond,
         resolution=(args.Xresolution, args.Yresolution), quality=args.quality,
         startTime=startTime)
