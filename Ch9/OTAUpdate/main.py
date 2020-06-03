from ota_update.main.ota_updater import OTAUpdater


 def download_and_install_update_if_available():
     o = OTAUpdater('url-to-your-github-project')
     o.download_and_install_update_if_available('wifi-ssid', 'wifi-password')


 def start():
     # your custom code goes here. Something like this: ...
     # from main.x import YourProject
     # project = YourProject()
     # ...


 def boot():
     download_and_install_update_if_available()
     start()


 boot()