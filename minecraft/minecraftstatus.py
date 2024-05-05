import json
import sys

from paesslerag_prtg_sensor_api.sensor.result import CustomSensorResult
from paesslerag_prtg_sensor_api.sensor.units import ValueUnit

from mcstatus import JavaServer

if __name__ == "__main__":
    try:
        data = json.loads(sys.argv[1])

        csr = CustomSensorResult(text="This sensor runs on %s" % data["host"])

        host = data["host"]

        try:
            port = int(data['params'])
        except:
            port = 25565

        print(f"host= {host} port= {port}")

        server = JavaServer.lookup(f"{host}:{port}")

        status = server.status()

        print(f"players= {status.players.online} max_players= {status.players.max}")

        csr.add_primary_channel(name="Players online",
                                value=status.players.online,
                                unit="Players",
                                is_limit_mode=True,
                                limit_max_warning=(status.players.max - 5),
                                limit_max_error=status.players.max,
                                limit_error_msg="Players is high")

        csr.add_channel(name="Latency",
                        value=server.ping(),
                        unit=ValueUnit.TIMERESPONSE)

        print(csr.json_result)

    except Exception as e:
        csr = CustomSensorResult(text="Python Script execution error")
        csr.error = "Python Script execution error: %s" % str(e)
        print(csr.json_result)
