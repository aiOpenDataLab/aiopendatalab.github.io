import sys, os
import argparse, logging
import threading
import config
from datetime import datetime
import inspect


def usage():
    print('Welcome to Synthentic Data Generator')
    print('data_gen.py --help')


def get_stocks(options):
    import yfinance as yf
    #from pandas_datareader import data as pdr
    print (f"options={options}")
    print(f'Category={options.category}')
    print(f'Output={options.output}')
    print(f'output_size={options.output_size}')
    print(f'Stock_source={config.stock}')
    #msft = yf.Ticker("MSFT")
    # get all stock info
    #print(f'msft={msft.info}')
    #yf.pdr_override()
    # download dataframe
    #data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
    #data = pdr.get_data_yahoo("SPY", period='5month')
    #pdr.get_data_yahoo()
    #tickers = yf.Tickers('msft aapl googl')
    data = yf.download('msft aapl googl', period='1wk')
    print(f'data={data}')
    f = open('output/test_finance.csv','w')
    data.to_csv(f)
    f.close()
    

    '''
    my_parser.add_argument('--input', action='store', type=int, nargs=3)
example:python nargs_example.py --input 42 42 42
[42, 42, 42]
'''

def menu():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-?", "--help", action="help", help="show this help message and exit")
    parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", help="increase output verbosity")
    parser.add_argument("-d", "--debug", action="store_true", dest="debug", help="show debug messages")
    #parser.add_argument("-h", "--host", action="append", dest="hostname", help="Provide remote host. Otherwise using config.py")
    parser.add_argument("-u", "--user", action="store", dest="username", help="Provide username of remote host. Otherwise using config.py")
    parser.add_argument("-p", "--pass", action="store", dest="password", help="Provide password of remote host. Otherwise using config.py")
    parser.add_argument("-f", "--file", action="append", dest="log_file", help="Provid log file to be monitor")
    parser.add_argument("-c", "--category", choices=['stock','weather'], dest="category", help="Provide 1 or more category", default='stock')
    parser.add_argument("-o", "--output", choices=['json','csv'], dest="output", help="Provide an output format.", default='json')
    parser.add_argument("-s", "--size", choices=['small','medium','large'], dest="output_size", help="Provide an output size.", default='small')
    #parser_sleep.set_defaults(func=sleep)
    #extra OPTION FOR COPY, TIME_RANGE, ETC COPY=ENABLE, TIME_RANGE_FROM=1hr TIME_RANGE_END=30MIN, ETC

    parser.add_argument('extra', nargs='*')
    options = parser.parse_args()

    print("extra type=%s, value=%s" % (type(options.extra), options.extra))
    if options.extra !=None:
        for item in options.extra:
            print("item=%s"%item)
            key,value = item.split("=")
            #FILTER_OPTIONS[key] = value

    # Set-up logger
    verbose = bool(os.environ.get('VERBOSE', options.verbose))
    debug = bool(os.environ.get('DEBUG', options.debug))
    if verbose or debug:
        logging.basicConfig(stream=sys.stdout)
        root = logging.getLogger()
        root.setLevel(logging.INFO if verbose else logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO if verbose else logging.DEBUG)
        ch.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(name)s: %(message)s'))
        root.addHandler(ch)
    else:
        logging.basicConfig(stream=sys.stderr)

    if options.category:
        print(f'category={options.category}')
    else:
        print("Arg=%s is not supported" % options)
        usage()
    print("hostname=%s" % (config.stock))
    get_stocks(options)
    #inspect.getargspec()
    #arg_spec = inspect.getargspec(options.func)
    #if arg_spec.keywords:
        ## convert args to a dictionary
    #    args_for_func = vars(args)
    #    print(f'args_for_func={args_for_func}')

    #load_config()



def load_config():
    print("############## CONFIGURATION #################")
    print("Stock=%s" % category)
    print("Weather=%s" % config.weather)
    #print("NEGATIVE_KEYWORD=%s" % config.NEGATIVE_KEYWORDS)
    print("##############################################\n")


usage()
menu()
#main_thread()
#auth = Authentication("orch-90","tetter")
#print(auth.execute("ls /tmp/"))

'''
hostname="orch-90"
username= "tetter"
auth = Authentication(hostname,username)
ssh = auth.connect()
#print("ssh=%s"%ssh)
obj = Execution(ssh,None,None)
filename = "%s/rpm_upgrade.log.3"%config.LOG_DIR
out_file = "%s/log.out"%config.LOG_DIR
time_range ="25M"
#start_time="date -v -%s '+%Y-%m-%dT%H:%M"%time_range    #mac
#print("start_time=%s"%start_time)

now = datetime.now()
#end_time = now.strftime("%Y-%m-%dT%H:%M")
end_time = now.strftime(config.LOG_TIME_FORMAT[0])
print("date and time:%s"%end_time)

##resp = obj.get_lines_between_timestamps("2020-07-10 10:20","2020-07-14 12:10",filename)
##resp = obj.get_lines_between_timestamps("2020-07-10 12:10","2020-07-14 10:21",filename,True)
exp_size=8867
#print(obj.get_filesize(filename,exp_size))
#obj.get_lines_between_timestamps(filename,out_file,"start_line","end_line") #OK
obj.get_lines_from_time(filename,out_file,time_range,end_time,search_str="five") # from 1min,5min, 10min
'''

