
import json
def main(): 
	data = [
        {'time': 1394984189, 'name': 'cpu', 'value': 12},
        {'time': 1394984190, 'name': 'cpu', 'value': 19}
        ]
	print json.dumps(data, indent=4) 
	data2 = {
        'key1' : [ 
        		{ 'time': 1394984189, 'name': 'cpu', 'value': 12 },
        		{ 'time': 1394984190, 'name': 'cpu', 'value': 19 }
        	],
        'key2' : [ 
        		{ 'time': 2, 'name': 'cpu' },
        		{ 'time': 3, 'name': 'cpu', 'value': 19 }
        	]
        }
	print json.dumps(data2, indent=4) 	
	
main()