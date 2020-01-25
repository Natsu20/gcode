# jupyter notebook tips
- command for remote access with jupyter notebook   
`$ local : ssh -L  8888:localhost:8888 -p <ssh port>  User_name@<IP addr>`  
`$remote : jupyter notebook --no-browser --port 8888`  
`$ local : http://localhost:8888`

- .ipynb file convert to .py file  
`jupyter nbconvert --to python ./bin/jupyter.py.ipynb`



