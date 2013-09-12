cardNum = 1
port = 1
fVlan = 2
lVlan = 21
f = open('/Users/bogorman/config.txt', 'w')
while(port <= 48):
        f.write('int e 10' + str(cardNum) + '/1/' + str(port) + '\r\n')
        f.write('switch trunk all vlan rem 2-4094\r\n')
        f.write('switch trunk all vlan 1001-1125\r\n')
        if(cardNum == 1):
                f.write('switch trunk all vlan add 1001-1125\r\n')
        elif(cardNum == 2):
                f.write('switch trunk all vlan add 1001-1125\r\n')
        elif(cardNum == 3):
                f.write('switch trunk all vlan add 1001-1125\r\n')
        elif(cardNum == 4):
                f.write('switch trunk all vlan add 1001-1125\r\n')
        if(port == 48 and cardNum < 4):
                port = 1
                cardNum = cardNum + 1
        else:
                port = port + 1
print "bacon"

