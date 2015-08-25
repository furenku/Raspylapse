gifshot.createGIF({
    gifWidth: 1280,
    gifHeight: 720,
    images: [
      //choose images dinamicaly from folder?
        'http://i.imgur.com/2OO33vX.jpg',
        'http://i.imgur.com/qOwVaSN.png',
        'http://i.imgur.com/Vo5mFZJ.gif'
    ],
    numFrames: 1000
}, function (obj) {
    if (!obj.error) {
        var image = obj.image, animatedImage = document.createElement('img');
        animatedImage.src = image;
        document.body.appendChild(animatedImage);
    }
});
