import sys
import argparse
from icmplib import ping


parser = argparse.ArgumentParser(description='Format: perf.py -l -j host')
parser.add_argument('-l', '--latency', type=float, default='60',
                    help='Max latency limit before considered critical')
parser.add_argument('-j', '--jitter', type=float, default='30',
                    help='Max jitter limit before considered critical')
parser.add_argument('host', metavar='host',
                   help='The host address that will be tested')

args = parser.parse_args()

if __name__ == '__main__':
    res = ping(args.host)

    if not res.is_alive:
        print('Host is unreachable.')
        sys.exit(2)

    rtt_status = 'OK' if res.avg_rtt <= args.latency else 'NOT_OK'
    jitter_status = 'OK' if res.jitter <= args.jitter else 'NOT_OK'
    print(f'HOST {rtt_status} - rtt={res.max_rtt} ms | {jitter_status} - jitter={res.jitter} ms')
