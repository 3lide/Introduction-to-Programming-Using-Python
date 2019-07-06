def footToMeter(foot):
    return 0.305 * foot

def meterToFoot(meter):
    return meter / 0.305

print('-'*121)
print("{:^29s}|{:^29s}| |{:^29s}|{:^29s}".format("Feet", "Meters", \
    "Meters", "Feet"))
print('-'*121)
for i in range(1, 11):
    print("{:^29.1f}|{:^29.1f}|".format(i, footToMeter(i)), 
    end = ' ')
    print("|{:^29.1f}|{:^29.3f}".format(5*i+15, meterToFoot(5*i+15)))

print('-'*121)