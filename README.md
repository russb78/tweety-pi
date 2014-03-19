# tweety-pi

A Raspberry Pi Camera project that automagically snaps wildlife photos and tweets the images to your chosen Twitter account.

### How it works
The project uses [modmypi.com](http://www.modmypi.com)'s [HC-SR501 PIR Infrared Motion Sensor](https://www.modmypi.com/pir-motion-sensor&filter_name=motion%20detect), the Raspberry Pi Camera board (using Dave Jones' excellent [picamera](https://github.com/waveform80/picamera) pure Python library) and [Tweepy](https://github.com/tweepy/tweepy) (Twitter for Python!). When the PIR senses motion a picture is taken and  posted to Twitter. 

Simply set the project up by your bird table, or window box and leave tweety-pi to do all the heavy lifting while you work, rest or [eat a Mars Bar](http://youtu.be/LTaCangOzCw?t=25s). Just make sure you've got plenty of bird seed!

###### I recommend commenting out the `update_twitter()` function until you've tweaked the sensitivity of your PIR motion sensor so you don't inadvertently abuse the Twitter API. 

----

This project was written by Russell Barnes for issue 138 of [Linux User & Developer magazine](http://www.linuxuser.co.uk).