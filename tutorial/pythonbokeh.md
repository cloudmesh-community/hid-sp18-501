?raw=true
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
-------------------------- 

The following steps are required to create a chart with Bokeh:

1. Import the function for the kind of chart you want to create

2. Prepare the data

3. Set the output mode for the chart

4. Create the chart styling

5. Create the chart visualization.

Please, follow the pyhton codes below to generate a chart using Bokeh:

Step 1: Import the function(s)

    #import library
     from bokeh.charts import Bar, output_file, show #use output_notebook to visualize it in notebookreport.tex

Step 2: Prepare the data

    #Prepare data (dummy data)
    data = {"y": [1, 2, 3, 4, 5]}
    
Step 3: Set Output mode (In this case as HTML)
 
    #Output to Line.HTML
    output_file("lines.html", title="line plot example") #put output_notebook() for notebook
    
Step 4: Create the Chart Styling

    #create a new line chat with a title and axis labels
    p = Bar(data, title="Line Chart Example", xlabel='x', ylabel='values', width=400, height=400)

Step 5: Visualize the chart
    
    #print chart
    show(p)
    
Committing the code above will display the visaulization of the desired chart.
    
    

    
    
    
    

