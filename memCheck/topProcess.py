def topProcess(numOfProcesses):
    import psutil

    ad_pids = []
    procs = []
    for p in psutil.process_iter():
        with p.oneshot():
            try:
                mem = p.memory_full_info()
                info = p.as_dict(attrs=['name', 'memory_info'])
            except psutil.AccessDenied:
                ad_pids.append(p.pid)
            except psutil.NoSuchProcess:
                pass
            else:
                p._uss = mem.uss
                if not p._uss:
                    continue
                p._info = info
                procs.append(p)
    procs.sort(key=lambda p: p._uss, reverse=True)
    for p in procs[:numOfProcesses]:
        print(p._info['name'] + "(" + str(p.pid) + "): {0:.2f}".format(p._uss / 1024 / 1024) + " MB")
    if ad_pids:
        print("warning: access denied for %s pids" % (len(ad_pids)),
            file=sys.stderr)
