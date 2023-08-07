import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import time
from datetime import date
import wget
import os
import requests
import json
import sys

def send_teams(webhook_url:str, content:str, title:str, color:str="000000") -> int:
    """
      - Send a teams notification to the desired webhook_url
      - Returns the status code of the HTTP request
        - webhook_url : the url you got from the teams webhook configuration
        - content : your formatted notification content
        - title : the message that'll be displayed as title, and on phone notifications
        - color (optional) : hexadecimal code of the notification's top line color, default corresponds to black
    """
    response = requests.post(
        url=webhook_url,
        headers={"Content-Type": "application/json"},
        json={
            "themeColor": color,
            "summary": title,
            "sections": [{
                "activityTitle": title,
                "activitySubtitle": content
            }],
        },
    )
    return response.status_code # Should be 200
    
def cve_printer(url):
    url1=url
    movie_request_page=requests.get(url1)
    if (movie_request_page):
        pass
    movie_request_parsed=BeautifulSoup(movie_request_page.text,"html.parser")
    str_movie_request_parsed=str(movie_request_parsed)
    mrc=movie_request_parsed.find(class_="col-sm-12 col-lg-3")
    str_movie_request_parsed
    mrc_1=str(mrc).replace('There are <strong data-testid="vuln-matching-records-count">','')
    mrc_1=mrc_1.replace('<div class="col-sm-12 col-lg-3">','')
    mrc_1=mrc_1.replace('</strong> matching records.','')
    mrc_1=mrc_1.replace('<div id="results-numbers-panel">','')
    mrc_1=mrc_1.replace('Displaying matches <strong data-testid="vuln-displaying-count-from">1</strong> through <strong data-testid="vuln-displaying-count-through">20</strong>.','')
    mrc_1=mrc_1.replace('</div>','')
    mrc_1=mrc_1.replace('</div>','')
    mrc_1=mrc_1.replace('\n','')
    #(mrc_1)
    #mrc_1=int(mrc_1)
    #print(type(mrc_1))
    #print(mrc_1)
    #page_count=mrc_1/20
    #page_count_suffix=str(page_count).split('.')
    #if page_count_suffix[1]==0:
    #    page_count=int(page_count_suffix[0])
    #else:
    #    page_count=int(page_count_suffix[0])+1
    #print(page_count)
    #for j in range(0,page_count):
    #    print(j)
    cve_table=movie_request_parsed.find(class_="table table-striped table-hover")
    cv_table_str=str(cve_table).replace('<table class="table table-striped table-hover" data-testid="vuln-results-table">','<table class="table table-striped table-hover"  border="1" data-testid="vuln-results-table" width=100%>')
    return cv_table_str

    
        
a=['https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Abusiness_client','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Agui_for_windows','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Aonedrive','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Aedge','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Agoogle&cpe_product=cpe%3A%2F%3Agoogle%3Achrome','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Akeepass&cpe_product=cpe%3A%2F%3Akeepass%3Akeepass','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3A7-zip&cpe_product=cpe%3A%2F%3A7-zip%3A7zip','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Aadobe&cpe_product=cpe%3A%2F%3Aadobe%3Alivecycle_designer_es4','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Afilezilla-project&cpe_product=cpe%3A%2F%3Afilezilla-project%3Afilezilla_client','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Agnupg&cpe_product=cpe%3A%2F%3Agnupg%3Agnupg','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Agpg4win&cpe_product=cpe%3A%2F%3Agpg4win%3Agpg4win','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3A365_apps','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Aremote_desktop_connection','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Anotepad-plus-plus&cpe_product=cpe%3A%2F%3Anotepad-plus-plus%3Anotepad++','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Avisual_studio','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Aoracle&cpe_product=cpe%3A%2F%3Aoracle%3Ajdk','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Akofax&cpe_product=cpe%3A%2F%3Akofax%3Akofax','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Ateams','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Asql_server','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Ahana_database','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Ahana','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Anodejs&cpe_product=cpe%3A%2F%3Anodejs%3Anode.js','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Aexcel','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Anodejs&cpe_product=cpe%3A%2F%3Anodejs%3Anode.js','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Aword','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Askype','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Awindows','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Awindows_10','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Aoffice_365','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Aoutlook','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Apowerpoint','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Apowershell','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Aremote_desktop','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Aremore_desktop_connection','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Amicrosoft&cpe_product=cpe%3A%2F%3Amicrosoft%3Aremote_desktop_connection_manager','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Afiori','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Afiori_launchpad','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Agui','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Ahana','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Asuccessfactors','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Awebdispatcher','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Aweb_dynpro_abap','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Aweb_dispatcher','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Aui','https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&isCpeNameSearch=false&cpe_vendor=cpe%3A%2F%3Asap&cpe_product=cpe%3A%2F%3Asap%3Aweb_dispatcher_and_internet_communication_manager']
listedProducts=['sap:business_client','sap:gui_for_windows','microsoft:onedrive','microsoft:edge','google:chrome','keepass:keepass','7-zip:7zip','adobe:livecycle_designer_es4','filezilla-project:filezilla_client','gnupg:gnupg','gpg4win:gpg4win','microsoft:365_apps','microsoft:remote_desktop_connection','notepad-plus-plus:notepad\+\+','microsoft:visual_studio','oracle:jdk','kofax:kofax','microsoft:teams','microsoft:sql_server','sap:hana_database','sap:hana','nodejs:node.js','microsoft:excel','nodejs:node.js','microsoft:word','microsoft:skype','microsoft:windows','microsoft:windows_10','microsoft:office_365','microsoft:outlook','microsoft:powerpoint','microsoft:powershell','microsoft:remote_desktop','microsoft:remore_desktop_connection','microsoft:remote_desktop_connection_manager','sap:fiori','sap:fiori_launchpad','sap:gui','sap:hana','sap:successfactors','sap:webdispatcher','sap:web_dynpro_abap','sap:web_dispatcher','sap:ui','sap:web_dispatcher_and_internet_communication_manager']
print(len(a))
for i in range(0,len(a)):
    y=a[i]
    p=listedProducts[i]
    x=cve_printer(y)
    buffer_var='<table class="table table-striped table-hover"  border="1" data-testid="vuln-results-table" width=100% ><thead><tr><td colspan="2">&nbsp;</td></tr><tr><th nowrap="nowrap" bgcolor="GreenYellow">'+p+'<i class="fa fa-bug fa-flip-vertical"></i></th></tr><tr><td colspan="2">&nbsp;</td></tr></thead></table>'
    x=buffer_var+x
    print(len(x))
    content=x
    title='@SIEM Reports -> CVE-alert : '+str(date.today())
    webhook_url='https://zalaris.webhook.office.com/webhookb2/ea84b4d0-079f-4fd8-b41d-b30d94612269@a16eb8e2-803d-4f22-849c-f3f335a60a39/IncomingWebhook/d7621bdbf5234abe93ccaf5a5c4768c5/f9164535-24c6-4bdf-924b-c341cbf08ede'
    send_teams(webhook_url,content,title,"000000")

