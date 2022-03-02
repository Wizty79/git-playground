import requests 
from datetime import datetime 

class StubResponse(): 
    def json(self): 
        return {"a": 1, "b": 2} 

def stub(url, params): 
    return StubResponse() 

def test_get_json_data(monkeypatch): 
    # Arrange 
    url = 'https://path/to/some/api' 
    timestamp = datetime(2020, 1, 1) 
    monkeypatch.setattr(requests, 'get', stub) 
    
    # Act 
    response = get_json_data(url, {}, timestamp) 
    
    # Assert 
    assert response['a'] == 1 
    assert response['b'] == 2 
    assert response['client_download_timestamp'] == timestamp 
