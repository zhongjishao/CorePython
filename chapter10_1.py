# practice,read a file and sum the number included in this file
# author: jeremy
# date:2018-09-26

def safe_float(obj):
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = diag
    return retval


def main():
    log = open('log.txt',  'w')
    try:
        ccfile = open('ccfile.txt', 'r')
    except IOError, e:
        log.write('ccfile is not exist\n')
        log.close()
        return
    txns = ccfile.readlines()
    ccfile.close()
    total = 0.0
    log.write('account log\n')

    for eachLine in txns:
        result = safe_float(eachLine)
        if isinstance(result, float):
            total = total + result
            log.write('%.2f data processed\n' % result)
        else:
            log.write('ignored: %s'% result)
    print ('$%.2f (new balance)' % (total))
    log.close()


if __name__ == '__main__':
    main()
