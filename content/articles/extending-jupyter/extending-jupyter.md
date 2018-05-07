Title: Extending the jupyter notebook 
author: Olamilekan Wahab
Slug: extending-jupyter
categories: python jupyter ipython software tool
Date: 2018-03-17
Tags: Python, Jupyter, Ipython , Software, Tool
image: jupyter.png
Status: draft


Originally called IPython when the only supported platform was python, the jupyter notebook is the go-to platform for interactive programming in various scripting languages. The currently supported 
languages include [python](https://mybinder.org/v2/gh/ipython/ipython-in-depth/master?filepath=binder/Index.ipynb), [R](https://mybinder.org/v2/gh/binder-examples/r/master?filepath=index.ipynb), [Julia](https://mybinder.org/v2/gh/binder-examples/julia-python/master?filepath=julia.ipynb).

>>> Fun Fact :  The name Jupyter is an acronym of these 3 languages :  **JU**lia,  **PYT**hon, and  **R**.

Some of the most used features of the jupyter notebook include keyboard shortcuts, pretty display, magic commands, shells, kernel supports,document exports, live coding and a host of other features
mentioned in this blogpost [here](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)


# What led to this article?

Last week, I was working in a notebook and needed to:  
I. Dynamically skip some cells

![Problem 1](/images/jupyter-problem-1.png) 



Problem 1: Going to the cell and selecting "Run Cell" would have taken care of this but it wasn't dynamic. 
          
II. Run some cells before others 

![Problem 2](/images/jupyter-problem-2.png) Problem 2



III. Trigger a run in a cell from another cell.



After looking at all keyboard shortcuts and features in jupyter, I realized there was no available support for this. 


Luckily for me, after digging deeper, I came across [this PyConUK talk](http://2017.pyconuk.org/sessions/talks/extending-jupyter-notebook/) that introduced the idea of extending jupyter and this 
was where I kicked off my research into this topic

The rest of the article would be laid out this way:

1. Terminologies

       i. Notebook Document
                
       ii. Kernels
            
2. Kernel Extensions
    
3. IPython Kernel Extensions
    
4. Notebook Extensions
    
5. Notebook Server Extensions



### **Terminologies**

### Notebook Document

A notebook document is the entry point of code in a jupyter notebook. Produced by the jupyter notebook app, notebook documents are made of executable cells that support code and text(in 
various formats) entry in various formats. These cells are draggable and can output code results in various formats(plots, images, texts, tables e.t.c)


### Kernels