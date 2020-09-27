# TWITTER CREDIBILITY RATING
Returns Twitter Credibility Ratings Object that includes hate, disaster, text_sentiment and
aggregated twitter credibility rating score.
Also you can test it by hitting the different features independently using these endpoints.

TWITTER_DISASTER_RATING_ENDPOINT = '/twitter/rating/disaster'
TWITTER_HATE_RATING_ENDPOINT = '/twitter/rating/hate'


## Installation
Install the required libraries

```sh
$ pip install -r requirements.txt
```

## Unit Testing

The various unit tests performed: 

1. Test to ensure function twitter_credibility_rating is working correctly.

## Running the tests
To run unit tests - 
```sh
$ pytest path/to/this/repository
```

## Static Code Analysis Tests
Static code analysis examines the code and provides an understanding of the code structure, and can help to ensure that the code adheres to industry standards. 

Below two linters have been for this purpose:

- **flake8**
- **pylint**

To perform code analysis tests using flake8 (will analyse all scripts in the repository):
```sh
$ flake8 --ignore F401, F403, F405, E731, W605, E722, E501 .
```

To perform code analysis tests using pylint:
```sh
$ pylint --output-format=text app/

```


## Deployment of API
Run the server
```sh 
$ python run.py
```
## Hitting the API
```python
import requests
 
import requests
obj = [{'text': ''}]
res = requests.post('http://13.235.17.80:8080/twitter/rating/all', json = obj).json()
```
## Authors
  
* **Ashutosh Vishnoi**