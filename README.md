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
Screencast of web app here: <a href="https://sherirosalia.github.io/Web_Scraping/"> Web Scraping Mars </a>

### Deployment 
Localhost

Run by inputting "python app.py" in bash or terminal.

This was hosted externally for a while, but  proved problematic due to the changes on the sites being scraped.  For example, Twitter commonly changed the tweet css class names, and when it did the script broke. 

### Frameworks
 Python
 Flask
 Bootstrap 4

### File Structure
The directory "mars_webscrape directory" contains scripts and templates

### Landing Page
<img src = "https://github.com/sherirosalia/Web_Scraping/blob/master/landing.png" width="400" alt="landing page">

### Info Table
<img src = "https://github.com/sherirosalia/Web_Scraping/blob/master/%20results.png" width="400" alt="table of results">

### Large Image
<img src = "https://github.com/sherirosalia/Web_Scraping/blob/master/result_img.png" width="400" alt="first large image">

### Mars Image
<img src = "https://github.com/sherirosalia/Web_Scraping/blob/master/mars_img.png" width="400" alt="mars sphere">

