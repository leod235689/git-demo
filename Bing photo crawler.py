import requests
payload = {'wd':'Python'}
r=requests.get('https://www.google.com.hk/?gws_rd=cr',params=payload)
r.url
