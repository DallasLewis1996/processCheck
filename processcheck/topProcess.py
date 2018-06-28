def topProcess(numOfProcesses):
    try:
        import psutil
        print('psutil found')
    except ImportError:
        raise RuntimeError('psutil missing!')
    from pprint import pprint as pp

    #using pretty print to organize to data; also sorts processes based on size: biggest first, smallest last
    pp([(p.info['name'] + "(" + str(p.pid) + "): {0:.2f}".format(p.info['memory_info'].rss / 1024 / 1024) + " MB") for p in sorted(psutil.process_iter(attrs=['name', 'memory_info']), key=lambda p: p.info['memory_info'])][-numOfProcesses:]) 
