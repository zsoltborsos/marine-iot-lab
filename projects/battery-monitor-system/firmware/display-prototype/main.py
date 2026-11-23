from batterymonitor import BatteryMonitor

bm = BatteryMonitor(debug=True, display=True)

try:
    asyncio.run(bm.run())
except KeyboardInterrupt:
    print('Interrupted')
finally:
    _ = asyncio.new_event_loop()
