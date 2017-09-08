



if __name__ == '__main__':
    import platform , os , subprocess
    #Linux
    #Windows
    sys = platform.system()
    if sys == 'Linux' :
        #print('ok')
        pass
    elif sys == 'Windows' :
        print('Windows')

    stock_name = 'sssss'
    path = os.getcwd() + '/report/%s'
    stock_dirctory = path % stock_name
    # 打印当前路径
    #print(stock_dirctory)


    #命令行
    os.system('pwd')
    os.system('echo $PATH')
    subprocess.call(['echo','PATH' ])




















