Visualization Using Bokeh
=============

Bokeh is an interactive visulaization library that
targets modern web browsers for visualization~\cite{hid-sp18-501-bokeh}.

Bokeh works by allowing multiple language bindings (e.g. Python or R)
that produce a JSON file which then presents data to the modern browser
~\cite{hid-sp18-501-vidhya}

In this tutorial, we will go through how to use python scripts to produce
different charts in Bokeh.

To use Bokeh, please follow this link to install https://bokeh.pydata.org/en/latest/

Creating Charts with Bokeh
============= 

The following steps are required to create a chart with Bokeh:

1. Import the function for the kind of chart you want to create

2. Prepare the data



    report.tex

which you are not allowed to edit.

Make sure you run 

    make check
    
which provides a conveneient way to check your latex code. Naturally you 
need to have the full version of LaTeX whcih includes chktex which 
make check calls.

Compiling the report
--------------------

We included a simple Makefile in the directory and if you have LaTeX
properly installed you can use it from commandline to create the
report.pdf:

    make

Please remember that you MUST NOT commit the report.pdf file to the
reporsitory. If we detect thsi we will remove it and do not review
your paper. This is to avoid that students submit papers that actually
do not compile in LaTeX. Make sure you paper always compiles.

This will also generate a simple check on some common issues. The 
log file is located in 

    report-latex.log
    
After the compilation is over.

    
Adding your own packages
------------------------

If you need to add additional usepackages, you need to ask for
approval first. You may not modify the color of hyperlinks or place
the figures in the text. But otherwise there will most likely be no
conflicts. To avoid any issue, check it first and ask for final
approval.

