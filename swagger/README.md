## Swagger Codegen API to get CPU, DISK and MEMORY Info
  
* Three API endpoints are provided.

  * ```/api/cpu```
  
  * ```/api/disk```
  
  * ```/api/memory```
  
 
## Instructions for docker installation

* git clone the project.

* you should install docker.

* change the directory to **swagger** folder.

* Build the image from docker file

	* ``` make docker-build ```

* Start the service using following make command
  
  * ```make docker-start```

* Test the service using following curl commands
  
  
  * ```curl -H "Content-Type:application/json" -X GET http://localhost:8080/api/cpu```
  
  * ```curl -H "Content-Type:application/json" -X GET http://localhost:8080/api/disk```
  
  * ```curl -H "Content-Type:application/json" -X GET http://localhost:8080/api/memory```

  
* Get the container ID using following command
  
  * ```docker ps```

* Stop the service using following commands
  
  * ```make docker-stop```

* Optional starting mechanism (interactive mode)
  
  * ```make start``` 
  
  * ```make stop```
	
## Instructions for ubuntu without docker

* you should be running this program in python 2 environment.

* you should have default-jre installed.

* git clone the project.

* change the directory to swagger folder

* Ensure Python 2 environment is activated

	* ``` pyenv activate env2 (Refer handbook for details ```

* create the swagger server with following command
  
  * ```make service```

* run the swagger server with following command
  
  * ```make start```

* test the program using following command
  
  * ```make test-cpu```
  
  * ```make test-disk```
  
  * ```make test-memory```

* stop the service using following command
  
  * ```make stop```

* clean the server and client codes using following command
  
  * ```make clean```

## API informations : Data Services

### End Point : api/cpu
  
  * This endpoint gets the processor and system  information
 
  * Sample curl request
  
	  ```curl -H "Content-Type:application/json" -X GET http://localhost:8080/api/cpu ```

### End Point : api/disk
  
  * The endpoint returns disk information 
  
  * Sample curl request
  
	  ```curl -H "Content-Type:application/json" -X GET http://localhost:8080/api/disk ```
 
### End Point : api/memory

* The endpoint returns MEMORY information. 

* Sample curl request
	  
	  ``` curl -H "Content-Type:application/json" -X GET http://localhost:8080/api/memory ```
