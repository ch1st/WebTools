# -*- coding=utf-8 -*-
'''
Created on 2017.6.1

@author: 8
'''
import sys
import requests



class CheckUrl():
    def __init__(self):
        
        #try:
        print('''
                          _               _               _ 
                      ___| |__   ___  ___| | ___   _ _ __| |
                     / __| '_ \ / _ \/ __| |/ / | | | '__| |
                    | (__| | | |  __/ (__|   <| |_| | |  | |
                    \___ |_| |_|\___|\___|_|\_\\__,_ |_|  |_|--ch1st 2017.6.1
         ''')
        
           # print("The program required Python Version 3.0 or more than 3.0")
    def writeUrl(self,list):
        success=open(sys.argv[1]+'_success.txt','a+')      
        for i in list:
            success.write(str(i)+"\n")
    
    def input(self):
        try:
            if len(sys.argv[1])>0:
                aim=sys.argv[1]
                return aim
        except:
            print("please input your  websites path")
    def run(self):
        header={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding':'gzip, deflate, br',
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control':'max-age=0',
                }
        try:
            url=open(self.input(),'r')
            if sys.version_info[1]>=3:
                for line in url.readlines():
                    line=line.strip()
                    list=[]
                    try:
                        conn = requests.get(url="http://"+line,headers=header)
                        if conn.status_code==200:
                            list.append(line)
                            self.writeUrl(list)
                            print(line+" is ok")
                    except:
                        print("The URL status_code isn't 200")
                
                print("The success url was writed at success.txt")
                print("The Program is Over") 
            else:
                print("The program required Python Version 3.0 or more than 3.0")
                sys.exit()
        except Exception as e:
            print(e)
        finally:
            url.close()
    
   

if __name__=="__main__":
    try:
    	run=CheckUrl()
    	run.run()
       
            
    except:
    	print("exit")