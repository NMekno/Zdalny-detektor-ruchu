import serial

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

serial_port = 'COM4'
baud_rate = 9600
write_to_file_path = "output.txt"

output_file = open(write_to_file_path, "w")
ser = serial.Serial(serial_port, baud_rate)
while True:
    line = ser.readline()
    line = line.decode("utf-8")
    deleteContent(output_file)
    print(line)
    output_file.write(line)
output_file.close()