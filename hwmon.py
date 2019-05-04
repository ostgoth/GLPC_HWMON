import psutil
import configargparse


def check_if_empty_arg_list(namespace):
    dct = vars(namespace)
    for key in dct:
        if dct[key]:
            break
    print('Script should be run with arguments. Use --help to get argument list')


p = configargparse.ArgParser()
p.add_argument('-c', '--cpu', action='store_true', help='CPU metrics')
p.add_argument('-m', '--mem', action='store_true', help='memory metrics')
args = p.parse_args()

if args.cpu:
    print(psutil.cpu_times())
if args.mem:
    print(psutil.virtual_memory(), psutil.swap_memory())

check_if_empty_arg_list(args)

