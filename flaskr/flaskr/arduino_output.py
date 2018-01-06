import serial
import time

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

serial_port = 'COM4'
baud_rate = 9600
licznik = 1
write_to_file_path = "output" + str(licznik) + ".txt"
start = time.time()
reduction = 0

PERIOD_OF_TIME = 120 
time_frontier = start + PERIOD_OF_TIME

# file initialisation
output_file = open(write_to_file_path, "w")
output_file.write("0")
output_file.close()
start2 = 0
ser = serial.Serial(serial_port, baud_rate)
while True:
    
    if time.time() > time_frontier:
        licznik += 1
        write_to_file_path = "output" + str(licznik) + ".txt"
        start = time.time()
        reduction += line
        time_frontier = start + PERIOD_OF_TIME
        # while True:
        #     try:
        #         output_file = open(write_to_file_path, "w+")
        #         print(0)
        #         output_file.write("0")
        #         output_file.close()
        #     except Exception as e:
        #         continue
        #     else:                
        #         break
    line = ser.readline()
    line = int(line.decode("utf-8")) - reduction
    output_file = open(write_to_file_path, "w")
    deleteContent(output_file)
    print(line)
    output_file.write(str(line))
    output_file.close()
    time.sleep(0.5)