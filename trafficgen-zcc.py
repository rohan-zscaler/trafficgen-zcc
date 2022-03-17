while True:
 from selenium import webdriver
 from selenium.webdriver.common.keys import Keys
 from bs4 import BeautifulSoup
 import os, requests ,  time , random ,re, urllib3
 urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


 time.sleep(random.randint(2,10))


 options = webdriver.ChromeOptions()
 options.add_argument('ignore-certificate-errors' )
 options.add_argument('incognito' )
 options.add_argument('--no-sandbox')
 #Adding experimental_option to suppress bluetooth warnings
 options.add_experimental_option("excludeSwitches", ["enable-logging"])
 driver = webdriver.Chrome(options=options)



 # Pick one of the sites randomly from list below. If the website picked randomly by the script is having issues then use www.bbc.com as the backup site  
 # Then parse that site and pick random links from it to browse to

 list_of_sites  = [ 'https://www.google.com', 'https://www.aljazeera.com', 'https://www.microsoft.com',
 'https://www.tradingview.com', 'https://www.nyt.com', 'https://www.freecodecamp.org', 'https://www.alibaba.com',
'https://www.digg.com', 'https://theuselessweb.site/', 'https://www.africanews.com/' ,
 'https://www.wordpress.org', 'https://en.wikipedia.org/wiki/Special:Random',
'https://www.woot.com', 'https://www.reddit.com', 'https://www.imdb.com' ,
 'https://sfbay.craigslist.org', 'https://www.cam.ac.uk', 'https://netflix.com', 
'https://spain.com', 'https://www.androidcentral.com', 'https://ftv.com', 'https://twitter.com', 
'https://merriam-webster.com', 'https://twitter.com', 'https://geeksforgeeks.org', 'https://tokopedia.com', 
'https://spotify.com', 'https://shopify.com', 'https://archive.org', 
'https://pandora.com', 'https://tripadvisor.com', 'https://ebay.com', 
'https://nfl.com', 'https://hive.blog', 'https://www.gizmodo.com', 
'https://cnn.com', 'https://stackexchange.com', 'https://vice.com', 
'https://www.karate.com', 'https://msn.com', 'https://investopedia.com', 
'https://paypal.com', 'https://dc.gov', 'https://www.smartsheet.com/', 
'https://blog.jp', 'https://flights.google.com', 'https://pinimg.com', 
'https://tistory.com', 'https://livejournal.com', 'https://dell.com', 
'https://cbssports.com', 'https://messenger.com', 'https://loksatta.com', 
'https://wikipedia.org', 'https://www.similarweb.com', 'https://nih.gov', 
'https://nbc.com', 'http://amazonaws.com',   'https://yelp.com' , 'https://weebly.com'  ]
 site_to_query = random.choice(list_of_sites)
 print(site_to_query)
 try:
     r = requests.get(site_to_query, verify=False)
 except:
     r = requests.get('https://www.bbc.com', verify=False)
 finally:
     try:
         soup = BeautifulSoup(r.text, "html.parser")
         links=[]
         for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
             links.append(link.get('href'))
         print("\nall links from the page ->\n")
         print (links)
         number_of_links_to_browse=5
         links = random.sample(links , k=number_of_links_to_browse)
         print("\nlinks that the script will attempt to load ->\n")
         print(links)
     except:
         driver.close()
         


 # Actual Selenium code below ->
 
 if (len(links)>=number_of_links_to_browse):
   

  try:
      driver.set_page_load_timeout(10)
      driver.get ('http://example.com')
      time.sleep(5)
      try:
          for l in links:
              driver.get(l)
      except:
          print ("###error encountered in accessing one of the links###")
          pass 
     # driver.close()
  except:
      #browserExe = "chrome.exe"
      #os.system("pkill "+browserExe)
      #os.system("taskkill /f /im "+browserExe)
      driver.close()
      continue







  list_of_malicious_repos  = [ 'https://raw.githubusercontent.com/Ultimate-Hosts-Blacklist/MalwareDomainList.com/master/domains.list' ,
                               'https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links/output/domains/ACTIVE/list',
                               'https://blocklistproject.github.io/Lists/alt-version/malware-nl.txt',
                               'https://blocklistproject.github.io/Lists/alt-version/phishing-nl.txt',
                               'https://blocklistproject.github.io/Lists/alt-version/crypto-nl.txt'
                              ]

  malicious_repo_to_query = random.choice(list_of_malicious_repos)
  driver.set_page_load_timeout(20)
  numner_of_mal_links_to_try=5
  print("entering malicious links portion")
  #malicious_list[40:] below is getting rid of header lines from the list  e.g. when it was created etc.
  try:
      r_mal = requests.get(malicious_repo_to_query, verify=False)
      malicious_list= []
      for line in r_mal.iter_lines():
          malicious_list.append(line)
      malicious_list=[x.decode('utf-8') for x in malicious_list[40:]]
      malicious_list = [ 'http://' + str(x) if not str(x).startswith('http') else str(x) for x in malicious_list ]
      #Picking a number of random malicious links after formatting them above
      malicious_list = random.sample(malicious_list , k=numner_of_mal_links_to_try)
      print("\n List of malicious sites to visit-> \n")
      print(malicious_list)
      for mal_l in malicious_list:
          try:
              print(mal_l)
              driver.get(mal_l)
          except:
              driver.close()
              os.system("taskkill /f /im  chrome.exe")
              os.system("taskkill /f /im  chromedriver.exe")
              
  except:
      print("##Hit exception in  Malicious code portion##")
