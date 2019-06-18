#!/usr/bin/python3
import subprocess
import requests

subprocess.run(['sudo', 'apt-get', 'update'])
subprocess.run(['sudo', 'apt-get', '-y', 'upgrade'])
#This is a simple script to update Visual Studio Code for debian based os's (Specifically xUbuntu in my case).
#Get the latest release from the vscode site
version_info = subprocess.check_output(['code','-v'])
sys_current = version_info\
            .decode('utf-8')\
            .split('\n')
ver_major = sys_current[0].split('.')[0]
ver_minor = sys_current[0].split('.')[1]

response = requests.get('https://code.visualstudio.com/updates')
code_version = response.url.split('/')[-1]

if 'v{}_{}'.format(ver_major, ver_minor) != code_version:
    update_url = 'https://vscode-update.azurewebsites.net/latest/linux-deb-x64/stable'
    output_loc = '/tmp/code_latest_amd64.deb'
    subprocess.run(['wget', update_url, '-O', output_loc])
    subprocess.run(['dpkg', '-i', output_loc])
    subprocess.run(['rm', output_loc])

subprocess.run(['sudo', 'apt-get', '-y', 'autoremove'])
