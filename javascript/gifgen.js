gifshot.createGIF({
    gifWidth: 1280,
    gifHeight: 720,
    images: [
      //choose images dinamicaly from folder?
        
	    '/time-lapse/timelapse0001.jpeg',
		'/time-lapse/timelapse0002.jpeg',
		'/time-lapse/timelapse0003.jpeg',
		'/time-lapse/timelapse0004.jpeg',
		'/time-lapse/timelapse0005.jpeg',
		'/time-lapse/timelapse0006.jpeg',
        '/time-lapse/timelapse0007.jpeg', 
        '/time-lapse/timelapse0008.jpeg',
        '/time-lapse/timelapse0009.jpeg',
        '/time-lapse/timelapse0010.jpeg',
        '/time-lapse/timelapse0011.jpeg',
        '/time-lapse/timelapse0012.jpeg',
        '/time-lapse/timelapse0013.jpeg',
    ],
    numFrames: 1000
}, function (obj) {
    if (!obj.error) {
        var image = obj.image, animatedImage = document.createElement('img');
        animatedImage.src = image;
        document.body.appendChild(animatedImage);
    }
});
