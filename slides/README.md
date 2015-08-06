This directory contains images and rest source for making a pdf presentation.
The Python script "time_compare.py" in the parent directory creates png and svg
images that we use in this pdf.

Create a pdf of these slides with the command: rst2pdf -e inkscape -b1 -s slides.style slides.rst
Create an S5 html slide output with the command (not using for conference): rst2s5 slides.rst -d slides.html