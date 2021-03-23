# shear_moment_deflection_calculator
#### Video Powerpoint:  https://youtu.be/aXabdBjnFXQ
#### Description:
For this project, I decided to pay tribute to my previous career path of structural engineering. Part of the fundamentals of structural analysis include calculating 
the shear, moment, and deflection of various beam conditions and scenarios. These equations are defined within the American Institute of Steel
Construction manual along with many more calculations and equations. In order to simplify the process, I decided to make a website using Javascript, HTML,
python, flask, and CSS that will take input values from the user and provide the answers to all of the shear, moment, and deflection equations applicable
to the specific beam condition chosen.

The files have been sorted into a static folder and a template folder. The static folder holds all of the images of the various beam conditions, as well as
the shear and moment diagrams on each calculation webpage. The static folder also holds the style file where the overall template for every webpage was defined
along with the calculation page format defined under the "main" tags. The template folder holds all of the HTML files for the homepage, beam condition pages,
and each of the calculation pages. The beam condition pages are separated into simple beams, cantilever beams, beams fixed at one end and supported at the other,
beams fixed at both ends, overhanging beams, and continuous beams. There are a total of 32 calculation pages to cover every scenario as provided in the AISC
manual. A python file is also included to define all of the application routes to be assigned to each page and link.

Each of the beam condition pages have a smiliar format with a title giving a brief description of the type of beam condition, as well as links to the different
calculation scenarios. Each of the links that take the user to a calculation page, are an image of the exact beam condition that the calculation is for. When
the user hovers their mouse over the image, an overlay will fade in and provide a description of the beam condition. Upon clicking the image and overlay, the
link will take the user to the appropriate calculation page.

Each calculation page is set up very similarly with a title giving a brief description of the beam condition, an image showing the beam condition, the shear
diagram, and the moment diagram, text boxes for the user to input the necessary variables, and a button to sumbit the form. Upon submitting the necessary input
variables, the program will take in the variables, apply them to the programmed equations and produce the solutions. The solutions will then be displayed on the
calculation webpage for the user to take the solutions, and go on to use them however they want.
