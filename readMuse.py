from pylsl import StreamInlet, resolve_stream
import time

data = []

streams = resolve_stream('type', 'EEG')
inlet = StreamInlet(streams[0])

for i in range(10):    
  sample, timestamp = inlet.pull_sample()
  data.append(timestamp)
  time.sleep(1)
  print(timestamp, sample)

print(data)