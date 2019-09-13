# method format
'Hello, {} !'.format('Vasya')
'Hello, Vasya!'

'{0} , {1} , {2} '.format('a', 'b', 'c')
'a, b, c'

'{0} {1} {0} '.format('abra', 'cad')
'abracadabra'

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude} , {longitude} '.format(**coord)
'Coordinates: 37.24N, -115.81W'

coord = (3, 5)
'X: {0[0]} ; Y: {0[1]} '.format(coord)
'X: 3; Y: 5'


