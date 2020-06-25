# Web Scraping Mars
## Dynamic, real time browser automation and data collection
Latest news about Mars in a user interface.

### About
NASA publicises data on a varity of platforms, and this project pulls information with the Python Beautiful Soup library from several different websites. 

Data collected from these links:
https://mars.nasa.gov/news/
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
https://www.jpl.nasa.gov/
https://twitter.com/marswxreport?lang=en
https://space-facts.com/mars/
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars


### Screencast
<video width="320" height="240" controls>
  <source src="scrape_recording.mov" type="video/mp4">
</video>

### Deployment 
Localhost

I did have it deployed on Heroku at one point, but this proved problematic due to website updates breaking the code when they change format. For example, Twitter commonly changes css class names.

Run with "python app.py"  commandline.

### Frameworks
 Python
 Flask
 Bootstrap 4

### File Structure


### Landing Page
![](landing.png)

### Results
![](results.png)



Landing page:
<img width="1280" alt="screen shot 2019-01-13 at 12 55 16 pm" src="https://user-images.githubusercontent.com/32849807/51091356-a418a300-173e-11e9-95ec-0e4a5b95479c.png">

Results appearing on upper area of webpage after scraping:

<img width="615" alt="mars_webscrape_image" src="https://user-images.githubusercontent.com/32849807/51091370-d2967e00-173e-11e9-88af-4f1ff144d802.png">


Results appearing on lower part of page after scraping:

<img width="667" alt="mars_webscrape_image_2" src="https://user-images.githubusercontent.com/32849807/51091347-83e8e400-173e-11e9-978b-e08e8ab54919.png">
