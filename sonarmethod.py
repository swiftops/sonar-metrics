import requests
import xmltodict
import sonarmap
from flask import jsonify

metriclist = {}

def getsonarmetrics(projectkey):
    try:
        for metrics in sonarmap.list:
            url = sonarmap.sonarmetricurl + projectkey + sonarmap.postfix + metrics
            resp = requests.get(url, params=None)
            query = xmltodict.parse(resp.text)
            value = query['svg']['g'][1]['text'][2]['#text']
            print(metrics, value)
            metriclist.update({metrics: value})
        
        metriclist.update({'URL': sonarmap.sonar_display_url + projectkey})
        list = {"success": "true",
                "data": metriclist, "error": {}}
        return jsonify(list)

    except Exception as e:
        response = {
            "success": "false",
            "data": {
                "Result": "Failed To get Result for SONAR"
            },
            "error": {"Message": str(e)}
        }
    return jsonify(response)
